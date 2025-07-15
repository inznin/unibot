from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7775669039:AAEN6c7X9nYMAka2Dm5BPHxM2AL4svQtWLg'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("فیزیولوژی", callback_data='physiology')],
        [InlineKeyboardButton("آناتومی", callback_data='anatomy')],
        [InlineKeyboardButton("بیوشیمی", callback_data='biochemistry')],
        [InlineKeyboardButton("بافت‌شناسی", callback_data='histology')],
        [InlineKeyboardButton("جنین‌شناسی", callback_data='embryology')],
        [InlineKeyboardButton("اصول خدمات سلامت", callback_data='health')]
    ]
    await update.message.reply_text("لطفاً درس مورد نظر را انتخاب کنید:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"شما انتخاب کردید: {query.data}")

if name == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()