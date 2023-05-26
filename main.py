from info import *
bot = telebot.TeleBot (took) 
@bot. message_handler (func=lambda m  : true)
def rm(m) : 
       bot.reply_to(m,m)
       bot.infinity_polling()