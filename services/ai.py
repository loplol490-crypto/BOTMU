import random

# память пользователей (пока в RAM)
user_memory = {}


def get_memory(user_id: int):
    if user_id not in user_memory:
        user_memory[user_id] = {
            "name": None,
            "topic": None
        }
    return user_memory[user_id]


async def get_ai_response(message: str, user_id: int) -> str:
    text = message.lower().strip()
    memory = get_memory(user_id)

    # --- имя пользователя ---
    if "меня зовут" in text:
        name = text.replace("меня зовут", "").strip()
        memory["name"] = name
        return f"🤝 Приятно познакомиться, {name}! Теперь я буду обращаться к тебе по имени."

    # --- привет ---
    if any(x in text for x in ["привет", "салам", "hello", "hi"]):
        if memory["name"]:
            return f"👋 Привет, {memory['name']}! Куда отправимся по Кыргызстану?"
        return "👋 Привет! Я твой AI-друг и гид по Кыргызстану 🇰🇬"

    # --- Бишкек ---
    if "бишкек" in text:
        memory["topic"] = "bishkek"
        return random.choice([
            "🏙 Бишкек — столица Кыргызстана. Хочешь, покажу интересные места?",
            "🏙 В Бишкеке советую Ошский базар и парк Панфилова.",
            "🏙 Могу составить маршрут по Бишкеку на 1 день."
        ])

    # --- Иссык-Куль ---
    if "иссык" in text:
        memory["topic"] = "issyk-kul"
        return random.choice([
            "🌊 Иссык-Куль — одно из самых красивых мест в Центральной Азии.",
            "🌊 Там есть пляжи, горы и крутые пансионаты.",
            "🌊 Хочешь — подберу тебе отдых на Иссык-Куле."
        ])

    # --- еда ---
    if any(x in text for x in ["еда", "поесть", "кухня", "бешбармак", "лагман"]):
        memory["topic"] = "food"
        return random.choice([
            "🍜 В Кыргызстане обязательно попробуй бешбармак и лагман.",
            "🍜 Кыргызская кухня очень сытная и вкусная 😄",
            "🍜 Могу подсказать лучшие кафе в Бишкеке."
        ])

    # --- транспорт ---
    if any(x in text for x in ["такси", "автобус", "маршрутка", "транспорт"]):
        memory["topic"] = "transport"
        return random.choice([
            "🚌 В Бишкеке удобно ездить на маршрутках и такси.",
            "🚕 Такси дешёвое и быстрое через приложения.",
            "🚌 Могу объяснить маршрут куда угодно."
        ])

    # --- продолжение темы ---
    if any(x in text for x in ["ещё", "подробнее", "расскажи"]):
        if memory["topic"] == "bishkek":
            return "🏙 Ещё в Бишкеке есть площадь Ала-Тоо и Дубовый парк."
        if memory["topic"] == "issyk-kul":
            return "🌊 На Иссык-Куле есть Чолпон-Ата и красивые каньоны."
        if memory["topic"] == "food":
            return "🍜 Ещё попробуй курут, самсу и плов по-кыргызски."
        if memory["topic"] == "transport":
            return "🚌 Маршрутки в Бишкеке ходят почти везде и стоят дёшево."

    # --- fallback (если не понял) ---
    return random.choice([
        "🤖 Я пока учусь, но уже могу быть твоим гидом по Кыргызстану 🇰🇬",
        "💬 Спроси меня про Бишкек, еду, транспорт или Иссык-Куль.",
        "🌍 Я твой AI-друг — просто напиши, что тебе интересно."
    ])
