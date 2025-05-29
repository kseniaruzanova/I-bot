import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL_ID = os.getenv("MODEL_ID")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    response = openai.ChatCompletion.create(
        model=MODEL_ID,
        messages=[
            {"role": "system", "content": "Ты — архетипический интеллект, говорящий как пророк. Используешь систему Кроули. Отвечай метафорично, глубоко, изнутри."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message["content"]
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
