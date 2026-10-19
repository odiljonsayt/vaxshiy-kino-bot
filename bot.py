import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
CHANNEL_URL = "https://t.me/vaxshiy_kino"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

WELCOME_TEXT = (
    "🎬 <b>VAXSHIY KINO</b>\n\n"
    "Kino olamiga xush kelibsiz! 🍿\n\n"
    "Tarjima kinolar, qo‘rqinchli filmlar va boshqa kino yangiliklarini "
    "kanalimizdan topishingiz mumkin.\n\n"
    "Mualliflik huquqini hurmat qiling va filmlarni qonuniy tomosha qilish "
    "manbalaridan foydalaning.\n\n"
    "👇 Kanalimizga o‘tish uchun quyidagi tugmani bosing:"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📺 KANALGA O‘TISH", url=CHANNEL_URL)]
    ])
    if update.message:
        await update.message.reply_text(
            WELCOME_TEXT,
            reply_markup=keyboard,
            parse_mode="HTML",
            disable_web_page_preview=True,
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Botdan foydalanish juda oson: /start buyrug‘ini bosing, "
            "keyin «📺 KANALGA O‘TISH» tugmasini tanlang."
        )

def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN topilmadi. .env faylini yarating yoki BOT_TOKEN "
            "muhit o‘zgaruvchisini sozlang."
        )

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    logger.info("Vaxshiy Kino bot ishga tushmoqda...")
    app.run_polling()

if __name__ == "__main__":
    main()
