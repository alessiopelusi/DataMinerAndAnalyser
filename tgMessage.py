import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time


def text(p):
    link=('https://www.amazon.it/dp/'+p['asin']+'?tag=offerteondema-21&psc=1')
    text = "🛒 {}\n\n".format(p['title'].replace('<', ''))
    text += "       💰 {} invece di {}\n".format(p['strikePrice'],p['oldPrice'])
    text += f"       👉🏻 <a href='{link}'>Apri su Amazon</a>\n\n"
    text += "🔶 <a href='https://t.me/offerteondemand'>Segnalata su Offerte On Demand</a>"
    print(text)
    return text

def inline_buttons():
    keyboard = [
        [InlineKeyboardButton("🗣 Invita un amico 🗣", url="https://t.me/+N5mVbdJbgehlMWI0")],
    ]
    buttons = InlineKeyboardMarkup(keyboard)
    return buttons

def telegramMessage(prodotto):
    TOKEN_bot = "<TELEGRAM_TOKEN_BOT>"
    chat_channel = "<CHANNEL_CHAT_ID>"
    bot = telegram.Bot(token=TOKEN_canaleFeedback)
    bot.sendPhoto(chat_canaleFeedback, caption=text(prodotto), photo=open('imageModifyCSS/local.jpg','rb'),  reply_markup = inline_buttons(), parse_mode=telegram.ParseMode.HTML)