import random


def generate_person_data(seed: int) -> dict:
    """
    Возвращает dict, ключи которого ожидает order.fill_personal_data(**person)
    """
    rnd = random.Random(seed)

    names = ["Иван", "Петр", "Алексей", "Максим", "Никита", "Дмитрий"]
    surnames = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Орлов"]
    streets = ["Ленина", "Пушкина", "Советская", "Мира", "Гагарина", "Невский проспект"]
    metros = ["Черкизовская", "Сокольники", "Комсомольская", "ВДНХ", "Тверская", "Парк культуры"]

    name = rnd.choice(names)
    surname = rnd.choice(surnames)
    address = f"ул. {rnd.choice(streets)}, д. {rnd.randint(1, 120)}, кв. {rnd.randint(1, 200)}"
    metro = rnd.choice(metros)

    # Телефон в формате 89XXXXXXXXX (часто проще проходит маску)
    phone = "89" + "".join(str(rnd.randint(0, 9)) for _ in range(9))

    return {
        "name": name,
        "surname": surname,
        "address": address,
        "metro": metro,
        "phone": phone,
    }


def generate_rent_data(seed: int) -> dict:
    """
    Возвращает dict, ключи которого ожидает OrderPage2ndStep.fill_rent_data(**rent)
    """
    rnd = random.Random(seed)

    periods = [
        "сутки",
        "двое суток",
        "трое суток",
        "четверо суток",
        "пятеро суток",
        "шестеро суток",
        "семеро суток",
    ]

    # Берём безопасный день месяца 1..28, чтобы реже упираться в "вне месяца"
    date_day = rnd.randint(1, 28)
    period = rnd.choice(periods)
    color = rnd.choice(["black", "grey"])
    comment = f"Тестовый комментарий #{seed}"

    return {
        "date_day": date_day,
        "period": period,
        "color": color,
        "comment": comment,
    }