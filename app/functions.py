from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import replicate
import os
import logging
from app.config import (
    CUSTOM_PROMPT_TITLE,
    IMAGE_CAPTION,
)

from dotenv import load_dotenv

load_dotenv()
AMOUNT_OF_FREE_IMAGES = int(os.getenv("AMOUNT_OF_FREE_IMAGES"))
COST_PER_CUSTOM_GENERATION = os.getenv("COST_PER_CUSTOM_GENERATION")
COST_PER_REGULAR_GENERATION = os.getenv("COST_PER_REGULAR_GENERATION")
REPLICATE_CLIENT = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

# Configure logging to ensure it is captured by journalctl
logging.basicConfig(level=logging.ERROR)


def generate_image_url(prompt: str) -> str | None:
    # 1. DEBUG: Check if Replicate API token is not None
    if not os.getenv("REPLICATE_API_TOKEN"):
        logging.error("REPLICATE_API_TOKEN is missing!")
        return None

    try:
        # 2. DEBUG: Log that the call has been initiated
        logging.error(f"Calling Replicate with prompt: {prompt}")

        output = REPLICATE_CLIENT.run(
            "black-forest-labs/flux-1.1-pro",
            input={
                "prompt": prompt,
                "aspect_ratio": "1:1",
                "output_format": "webp",
                "output_quality": 80,
                "safety_tolerance": 2,
                "prompt_upsampling": True,
            },
        )

        # 3. DEBUG: Print the raw response to see its structure
        logging.error(f"Replicate RAW Output received: {output}")

        if output.url:
            return output.url
        else:
            raise ("no image url error")

    except Exception as e:
        # 4. LOGGING: Print full error traceback
        logging.error(f"CRITICAL ERROR in generate_image_url: {e}", exc_info=True)
        return None

    return None  # Return None if something went wrong


def create_keyboard_from_list(items: list[str]) -> ReplyKeyboardMarkup:
    buttons: list[KeyboardButton] = [KeyboardButton(text=item) for item in items]
    row_items: int = 2
    rows: list[list[KeyboardButton]] = []

    for i in range(0, len(buttons), row_items):
        row = buttons[i : i + row_items]
        rows.append(row)

    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)


def get_trial_image_caption(total: int) -> str:
    remaining = AMOUNT_OF_FREE_IMAGES - total
    if remaining == 0:
        return f"{IMAGE_CAPTION}\nIt was your last trial waifu."
    else:
        return f"{IMAGE_CAPTION}\nYou have {remaining}🔥 trials left"


def create_users_table(users: list[any]) -> str:
    # Generate report
    report_lines = ["📊 *User Statistics Report*", "---"]

    # Table header for better readability
    report_lines.append("```")
    report_lines.append("ID                 | Pics | Gen | Open")
    report_lines.append("-------------------|------|-------|---------")

    # Iterate through data and format each row
    for user in users:
        user_id = str(user[0])
        total_pics = str(user[2])
        is_generating = "✅" if user[1] else "❌"
        is_unlocked = "✅" if user[3] else "🔒"

        # Format row: ID (trimmed to 10 chars) | Pic | Gen | Unlock
        report_lines.append(
            f"{user_id[:10].ljust(10)} | {total_pics.rjust(4)} | {is_generating.center(3)} | {is_unlocked.center(7)}"
        )

    final_report = "\n".join(report_lines)
    report_lines.append("```")
    return final_report
    # Send report to chat using MarkdownV2 for monospaced text
    # while ensuring message length limit (4096 characters) is not exceeded


# FUNCTION: calculate price for image
def calculate_price(category: str) -> int:
    price = COST_PER_REGULAR_GENERATION
    if category == CUSTOM_PROMPT_TITLE:
        price = COST_PER_CUSTOM_GENERATION
    return price
