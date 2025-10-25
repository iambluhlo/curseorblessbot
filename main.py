from myenv import API_KEY
import telebot
from telebot import types
import random as rd
import curses 


bot = telebot.TeleBot(API_KEY.API_TOKEN, parse_mode=None)



curses_list = [line.strip() for line in curses.curses_raw.splitlines() if line.strip()]


markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('نفرین')
itembtn2 = types.KeyboardButton('سعادت')
itembtn3 = types.KeyboardButton('رندوم')
markup.add(itembtn1, itembtn2, itembtn3)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.reply_to(message, "Hello", reply_markup=markup)
    return chat_id
      



	
    
@bot.message_handler(func=lambda message: True)
def echo(message):
    chat_id = message.chat.id
    msg = message.text
    if msg == "سعادت":
        user_curse = rd.randint(0,59)
        bot.send_message(chat_id, curses_list[user_curse])



bot.infinity_polling()