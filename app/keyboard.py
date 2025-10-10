from app.config import CONTENT_OPTIONS, COST_PER_REGULAR_GENERATION, UNLOCK_IMAGE
from app.functions import create_keyboard_from_list
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# reply keyboard with options
show_options = create_keyboard_from_list(CONTENT_OPTIONS)


# keyboard with offer to pay for image
def pay_for_generation(unique_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"✨ {UNLOCK_IMAGE} {COST_PER_REGULAR_GENERATION} ⭐",
                    pay=True,
                    callback_data=f"PAY_FOR_IMAGE_{unique_id}",
                )
            ]
        ]
    )
