from myenv import API_KEY
import telebot


bot = telebot.TeleBot(API_KEY.API_TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello")
	
bot.infinity_polling()