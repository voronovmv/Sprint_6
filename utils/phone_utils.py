import re


def normalize_ru_phone(raw: str) -> str:
    digits = re.sub(r"\D", "", raw or "")

    if digits.startswith("7"):
        digits = digits[1:]
    elif digits.startswith("8"):
        digits = digits[1:]

    if len(digits) < 10:
        raise ValueError("Недостаточно цифр для российского номера")

    digits = digits[:10]
    return "+7" + digits