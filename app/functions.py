from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import replicate
import os
from app.config import (
    AMOUNT_OF_FREE_IMAGES,
    COST_PER_REGULAR_GENERATION,
    EXCLUDE,
    IMAGE_CAPTION,
)

REPLICATE_CLIENT = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))


def generate_image_url(prompt: str) -> str | None:
    try:
        output = REPLICATE_CLIENT.run(
            "aisha-ai-official/miaomiao-harem-illustrious-v1:d74eab7842eca403256b37c4276e0c19b83aa124cc5d102d15d9327a6d14ad02",
            input={
                "prompt": prompt,
                "vae": "MiaoMiao-Harem-Illustrious-v1",
                "width": 768,
                "height": 1024,
                "model": "MiaoMiao-Harem-Illustrious-v1",
                "negative_prompt": EXCLUDE,
            },
        )

        if output and len(output) > 0:
            return output[0].url

    except Exception as e:
        print(f"Error in generate_image_url: {e}")
        return None


def create_keyboard_from_list(items: list[str]) -> ReplyKeyboardMarkup:
    buttons: list[KeyboardButton] = [KeyboardButton(text=item) for item in items]
    row_items: int = 2
    rows: list[list[KeyboardButton]] = []

    for i in range(0, len(buttons), row_items):
        row = buttons[i : i + row_items]
        rows.append(row)

    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)


async def generate_image():
    content = await replicate.run(
        "aisha-ai-official/miaomiao-harem-illustrious-v1:d74eab7842eca403256b37c4276e0c19b83aa124cc5d102d15d9327a6d14ad02",
        input={"prompt": "an iguana on the beach, pointillism"},
    )
    with open("output.png", "wb") as f:
        f.write(content[0].read())


def get_trial_image_caption(total: int) -> str:
    remaining = AMOUNT_OF_FREE_IMAGES - total
    if remaining == 0:
        return f"{IMAGE_CAPTION}\nIt was your last trial waifu. Next one is {COST_PER_REGULAR_GENERATION}⭐"
    else:
        return f"{IMAGE_CAPTION}\nYou have {remaining}🔥 trials left"


def create_users_table(users: list[any]) -> str:
    # Формируем отчет
    report_lines = ["📊 *User Statistics Report*", "---"]

    # Заголовок таблицы для удобства чтения
    report_lines.append("```")
    report_lines.append("ID                 | Pics | Gen | Open")
    report_lines.append("-------------------|------|-------|---------")

    # Итерируемся по данным и форматируем каждую строку
    for user in users:
        user_id = str(user[0])
        total_pics = str(user[2])
        is_generating = "✅" if user[1] else "❌"
        is_unlocked = "✅" if user[3] else "🔒"

        # Форматируем строку: ID (обрезаем до 12 символов, чтобы поместилось) | Pic | Gen | Unlock
        report_lines.append(
            f"{user_id[:10].ljust(10)} | {total_pics.rjust(4)} | {is_generating.center(3)} | {is_unlocked.center(7)}"
        )

    final_report = "\n".join(report_lines)
    report_lines.append("```")
    return final_report
    # Отправляем отчет в чат, используя MarkdownV2 для моноширинного текста
    # и избегая превышения лимита на длину сообщения (4096 символов).
