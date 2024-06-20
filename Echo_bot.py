from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime

# Bot tokenini o'zingizning tokeningiz bilan almashtiring
TOKEN = '6989440381:AAEJpCSN73Qk-3LVQoFeVYjPWV92n3WPn34'


# /start komandasi uchun callback funksiyasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_first_name = update.message.from_user.first_name
    await update.message.reply_text(f'Salom, {user_first_name}! Bu bot haqida ma`lumot uchun /help tugmasini bosing')


# /help komandasi uchun callback funksiyasi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Bu bot sizning xabarlaringizni qaytaradi. /time komandasini yuboring hozirgi vaqtni olish uchun.')


# /time komandasi uchun callback funksiyasi
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await update.message.reply_text(f'Hozirgi vaqt: {current_time}')


# Echo xabarlar uchun callback funksiyasi
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


def main() -> None:
    # Botning application ob'ektini yaratamiz
    application = Application.builder().token(TOKEN).build()

    # Handlerlarni ro'yxatga qo'shamiz
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", time_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Botni boshlaymiz
    application.run_polling()


if __name__ == '__main__':
    main()
