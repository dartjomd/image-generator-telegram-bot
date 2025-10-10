import asyncio
import os
from aiogram.filters import Command
from aiogram.exceptions import TelegramAPIError
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,
    CallbackQuery,
    LabeledPrice,
    PreCheckoutQuery,
)
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Bot, Router
from app import functions
from app.config import (
    AMOUNT_OF_FREE_IMAGES,
    CATEGORIES,
    CONTENT_OPTIONS,
    COST_PER_CUSTOM_GENERATION,
    COST_PER_REGULAR_GENERATION,
    CUSTOM_PROMPT_TITLE,
    GENERATION_TIME,
    GO_TO_REFUND,
    HELP_MESSAGE,
    OHTER_CATEGORY,
    PAYMENT_ERROR,
    PICTURE_REQUEST_ERROR,
    PREVIOUS_PICTURE_IS_LOCKED,
    PRIVACY_POLICY_MESSAGE,
    REFUND_MESSAGE,
    SUPPORT_MESSAGE,
    TYPE_CUSTOM_CATEGORY,
    WELCOME_MESSAGE,
    IMAGE_CAPTION,
    PICUTRE_IS_ALREADY_GENERATING,
)
from app.functions import generate_image_url
import app.keyboard as kb
from app.UsersController import UsersController
from app.GenerationsController import GenerationsController

load_dotenv()
ADMIN_ID = int(os.environ.get("ADMIN_ID"))
TEMP_GENERATION = {}


# FUNCTION: send unlocked image to user
async def send_unlocked_image(
    message: Message, final_image_url: str, caption=IMAGE_CAPTION
) -> None:
    await message.answer_photo(
        photo=final_image_url,
        caption=caption,
        reply_markup=kb.show_options,
        parse_mode="Markdown",
    )


# FUNCTION: offer to pay to unlock image
async def offer_to_pay(message: Message, u_id: int):
    await message.answer(
        text="<i>She is ready...</i>",
        reply_markup=kb.pay_for_generation(u_id),
        parse_mode="html",
    )


# FUNCTION: handle start generating image
async def _start_image_generation(
    message: Message, prompt: str, category: str, state: FSMContext
):
    image_url: None | str = None

    # check if user is already generating a picture
    u_id = message.from_user.id

    # set IS_GENERATING to true in database
    UsersController.change_user_generating(user_id=u_id, is_generating=1)

    # send status message
    status_message = await message.answer(
        GENERATION_TIME,
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove(),
    )

    try:
        # execute Replicate request in another thread
        image_url = await asyncio.to_thread(generate_image_url, prompt)

        # send photo
        if not image_url:
            raise ("no image_url")

        # create new generation
        GenerationsController.create_generation(u_id, image_url, category)

        # check user total images error
        user_total_images = GenerationsController.get_user_total_generations(u_id)
        if not user_total_images:
            await message.answer(
                PICTURE_REQUEST_ERROR,
                reply_markup=kb.show_options,
            )
            raise ("user_total_images is False")

        if user_total_images <= AMOUNT_OF_FREE_IMAGES:
            # send trial image
            await send_unlocked_image(
                message,
                final_image_url=image_url,
                caption=functions.get_trial_image_caption(total=user_total_images),
            )

            # EXPLICITLY resolve pending generation for trial picture
            GenerationsController.resolve_generation(u_id)
        else:
            # send message to offer to pay
            await offer_to_pay(message, u_id)

    except Exception as e:
        print(f"Error in generation image: {e}")
        await message.answer(
            PICTURE_REQUEST_ERROR,
            reply_markup=kb.show_options,
        )

    finally:
        # set IS_GENERATING = 0 in database
        UsersController.change_user_generating(user_id=u_id, is_generating=0)

        # resolve state
        await state.clear()

        # delete status message
        await message.bot.delete_message(
            chat_id=message.chat.id,
            message_id=status_message.message_id,
        )


class PromptStates(StatesGroup):
    """define states"""

    waiting_for_preference = State()
    waiting_for_custom_prompt = State()


router = Router()


# on START show keyboard with categories
@router.message(Command("start"))
async def handle_start(message: Message, state: FSMContext):
    # user id
    u_id = message.from_user.id

    # check if user exists and create user if not
    if not UsersController.user_exists(u_id):
        UsersController.create_user(u_id)

    # send OPTIONS keyboard
    await message.answer(
        WELCOME_MESSAGE, reply_markup=kb.show_options, parse_mode="html"
    )

    # set state to wait for category
    await state.set_state(PromptStates.waiting_for_preference)


# send user his ID
@router.message(Command("myid"))
async def handle_user_id(message: Message):
    await message.answer(
        text=f"Here is your personal ID. Use it wisely: {message.from_user.id}",
        reply_markup=kb.show_options,
    )


# help command
@router.message(Command("help"))
async def handle_help(message: Message):
    await message.answer(
        text=HELP_MESSAGE, parse_mode="html", reply_markup=kb.show_options
    )


# support command
@router.message(Command("support"))
async def handle_help(message: Message):
    await message.answer(
        text=SUPPORT_MESSAGE, parse_mode="html", reply_markup=kb.show_options
    )


# privacy policy command
@router.message(Command("privacy"))
async def handle_help(message: Message):
    await message.answer(
        text=PRIVACY_POLICY_MESSAGE, parse_mode="html", reply_markup=kb.show_options
    )


# terms of use command
@router.message(Command("tos"))
async def handle_help(message: Message):
    await message.answer(
        text=PRIVACY_POLICY_MESSAGE, parse_mode="html", reply_markup=kb.show_options
    )


# refund command
@router.message(Command("refund"))
async def handle_help(message: Message):
    await message.answer(
        text=REFUND_MESSAGE, parse_mode="html", reply_markup=kb.show_options
    )


# ADMIN COMMANDS
# Admin command to display all user statistics
@router.message(Command("admin_users"))
async def handle_admin_users(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    users = UsersController.get_all_extended_users()

    if not users:
        await message.answer(
            "⚠️ No users found in the database.", reply_markup=kb.show_options
        )
        return

    # form table with users statistics
    final_report = functions.create_users_table(users)

    try:
        await message.answer(final_report, parse_mode="html")
    except TelegramAPIError as e:
        print(e)
        # Если отчет слишком длинный, отправляем упрощенную версию или ошибку
        await message.answer(
            f"✅ Report generated, but it was too long ({len(final_report)} chars) to send as one message."
        )
    finally:
        await message.answer(text=f"Total users: {len(users)}")


# handle all categories and custom prompt input (CONSOLIDATED LOGIC)
@router.message(F.text)
async def handle_categories(message: Message, state: FSMContext):
    msg: str = message.text
    current_state: str = await state.get_state()
    is_category = msg in CONTENT_OPTIONS
    u_id = message.from_user.id
    if UsersController.is_user_generating(u_id):
        await message.answer(PICUTRE_IS_ALREADY_GENERATING)
        return None

    # check if user paid for previous image
    if not GenerationsController.is_user_allowed_to_generate(u_id):
        await message.answer(PREVIOUS_PICTURE_IS_LOCKED)
        await offer_to_pay(message, u_id)
        return None

    # 1. HANDLE CUSTOM PROMPT TEXT INPUT (The key fix)
    if current_state == PromptStates.waiting_for_custom_prompt.state:
        if not is_category:
            # Input is the user's custom prompt text (e.g., "My powerful dragon").
            # This logic block replaces the old handle_preference function.
            await _start_image_generation(
                message=message,
                prompt=message.text,
                category=CUSTOM_PROMPT_TITLE,
                state=state,
            )
            return
        # If the state is active AND the message IS a category (user clicked a button),
        # the code continues below to reset the flow and start standard generation.

    # 2. ARBITRARY TEXT (Input is not a category AND state is not active)
    if not is_category:
        await message.answer(text=OHTER_CATEGORY, reply_markup=kb.show_options)
        return

    # 3. MESSAGE IS CUSTOM PROMPT BUTTON (Input is "Кастомный промпт")
    if msg == CUSTOM_PROMPT_TITLE:

        # offer user to type custom prompt
        await message.answer(text=TYPE_CUSTOM_CATEGORY)
        # change state to await custom prompt
        await state.set_state(PromptStates.waiting_for_custom_prompt)
        return

    # 4. MESSAGE IS A REGULAR CATEGORY BUTTON
    # (Input is e.g., "Природа", resetting the state if necessary)
    await _start_image_generation(
        message=message, prompt=CATEGORIES[msg], category=msg, state=state
    )


@router.callback_query(F.data.startswith("PAY_FOR_IMAGE_"))
async def handle_pay_button_callback(callback_query: CallbackQuery, bot: Bot):
    # handle shining button
    await callback_query.answer()

    u_id: int = callback_query.from_user.id
    generation: list[any] = GenerationsController.get_generation(u_id)

    # resolve pending generation
    GenerationsController.resolve_generation(u_id)

    # check if there is pending generation for user
    if not generation:
        await callback_query.message.answer(
            text=PAYMENT_ERROR, reply_markup=kb.show_options
        )
        return

    uniq_id: str = str(generation[0])

    TEMP_GENERATION[uniq_id] = generation
    category: str = generation[3]

    # calculate price
    price = COST_PER_REGULAR_GENERATION
    if category == CUSTOM_PROMPT_TITLE:
        price = COST_PER_CUSTOM_GENERATION

    # remove PAY button after it is clicked
    await bot.edit_message_reply_markup(
        chat_id=u_id, message_id=callback_query.message.message_id, reply_markup=None
    )

    # handle invoice
    await bot.send_invoice(
        chat_id=u_id,
        title=f"Unlock: {category}",
        description="Pay, to see her beauty",
        provider_token=None,
        currency="XTR",
        prices=[
            LabeledPrice(
                label=f"{price} ⭐",
                amount=price,
            )
        ],
        payload=uniq_id,
        is_flexible=False,
        start_parameter="ai_reveal",
    )


# handle PreChekoutQuery
@router.pre_checkout_query(lambda query: True)
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    unique_id = pre_checkout_query.invoice_payload
    u_id = pre_checkout_query.from_user.id

    # resolve pending generation
    GenerationsController.resolve_generation(u_id)

    if unique_id in TEMP_GENERATION:
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    else:

        await bot.answer_pre_checkout_query(
            pre_checkout_query.id, ok=False, error_message=PAYMENT_ERROR
        )

        await bot.send_message(
            chat_id=u_id,
            text=PAYMENT_ERROR,
            reply_markup=kb.show_options,
            parse_mode="Markdown",
        )


# handle Successful payment and send UNFILTERED image
@router.message(F.successful_payment)
async def successful_payment_handler(message: Message, bot: Bot):
    u_id = message.from_user.id
    unique_id = message.successful_payment.invoice_payload

    # resolve pending generation
    GenerationsController.resolve_generation(u_id)

    # check if user has pending generation
    if unique_id not in TEMP_GENERATION:
        await message.answer("❌ Ooops..", reply_markup=kb.show_options)
        await issue_refund(
            bot=bot,
            u_id=u_id,
            telegram_charge_id=message.successful_payment.telegram_payment_charge_id,
            chat_id=message.chat.id,
        )
        return None

    # remove pending generation
    generation_data = TEMP_GENERATION.pop(unique_id)

    # send unfiltered image to user
    await send_unlocked_image(message, final_image_url=generation_data[2])


# handle refund
async def issue_refund(bot: Bot, u_id: int, telegram_charge_id: str, chat_id: int):
    # resolve pending generation
    GenerationsController.resolve_generation(u_id)

    try:
        success = await bot.refund_star_payment(
            user_id=u_id, telegram_payment_charge_id=telegram_charge_id
        )

        if success:
            await bot.send_message(
                chat_id,
                "✅ Don't worry, the funds were returned",
                reply_markup=kb.show_options,
            )
            return True
        else:
            await bot.send_message(chat_id, GO_TO_REFUND, reply_markup=kb.show_options)
            return False

    except TelegramAPIError as e:
        await bot.send_message(chat_id, GO_TO_REFUND, reply_markup=kb.show_options)
        return False
