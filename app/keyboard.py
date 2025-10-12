from app.config import CONTENT_OPTIONS, UNLOCK_IMAGE
from app.functions import calculate_price, create_keyboard_from_list
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.GenerationsController import GenerationsController


# reply keyboard with options
show_options = create_keyboard_from_list(CONTENT_OPTIONS)


# keyboard with offer to pay for image
def pay_for_generation(unique_id: int) -> InlineKeyboardMarkup:
    # get image category
    # category = GenerationsController.get_generation_by_id(unique_id)

    # if not category:
    #     print("unexpected error in calculating price")
    #     return False

    # price = calculate_price(category)

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"✨ {UNLOCK_IMAGE} ✨",
                    pay=True,
                    callback_data=f"PAY_FOR_IMAGE_{unique_id}",
                )
            ]
        ]
    )
