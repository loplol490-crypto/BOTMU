async def handle_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    # LANGUAGE (БЕЗ МЕНЮ)
    if data == "lang_ru":
        context.user_data["lang"] = "ru"
        await query.edit_message_text("Язык выбран 🇷🇺")

    elif data == "lang_en":
        context.user_data["lang"] = "en"
        await query.edit_message_text("Language selected 🇬🇧")

    elif data == "lang_kg":
        context.user_data["lang"] = "kg"
        await query.edit_message_text("Тил тандалды 🇰🇬")

    # MENU (ОСТАВЛЯЕМ КАК БЫЛО)
    elif data == "guide":
        await query.edit_message_text("🗺 Гид по Кыргызстану", reply_markup=main_menu())

    elif data == "food":
        await query.edit_message_text("🍜 Еда Кыргызстана", reply_markup=main_menu())

    elif data == "transport":
        await query.edit_message_text("🚌 Транспорт Кыргызстана", reply_markup=main_menu())

    elif data == "settings":
        await query.edit_message_text("⚙️ Настройки", reply_markup=main_menu())
