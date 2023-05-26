from info import *
bot = telebot.TeleBot (took) 
@bot. message_handler (func=lambda m  : true)
def rm(m) : 
       bot.reply_to(m,m)
       bot.infinity_polliimport telebot 
from telebot import types,TeleBot
bot=TeleBot("6296366259:AAF9kDYm0VXqFUHBP0FEpAkGW-Fg5-aZrPU")

back = types.InlineKeyboardButton(text="raad", callback_data = "b1")  #رعد هوا الزر نفسة 

@bot.message_handler(commands=['start'])
def start(message) :
	 b=types.InlineKeyboardMarkup() 
	 b.row_width = 1
	 b.add(back) 
	 bot.reply_to(message,f"aporaad", reply_markup=b) #ابو رعد هوا اسم الزر 
	  
@bot.callback_query_handler(func=lambda call: True) 
def qwere(call):
	if call.data == "b1": 
	    bot.send_message(call.message.chat. id, f"arslan") #ارسلان هوا اجابة الزر 
@bot.message_handler(func=lambda message: message.text == "هلا")
def reply_to_specific_message(message):
    bot.reply_to(message, "اهلين ") 
@bot.message_handler(func=lambda message: message.text == "كيفك")

def reply_to_specific_message(message):
    bot.reply_to(message, "الحمد لله  \nوانت كيفك")  
@bot.message_handler(func=lambda message: message.text == "بخير")
def reply_to_specific_message(message):
    bot.reply_to(message, "تدوم عافيتك  ") 
@bot.message_handler(func=lambda message: message.text == "ابو رعد ")
def reply_to_specific_message(message):
    bot.reply_to(message, "والنعم فيك سيد الرجال  ") 
 # replace CORRECT_ANSWER with the correct answer
correct_answer = "ابو رعد السرحي"

@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.reply_to(message, "Welcome! Please answer the following question:")

@bot.message_handler(func=lambda message: True)
def check_answer(message):
  if message.text == correct_answer:
   bot.reply_to(message, "Congratulations, you gave the correct answer!")
  else:
   bot.reply_to(message, "Sorry, your answer is incorrect. Please try again.") 

bot.import telebot 
from telebot import types,TeleBot
bot=TeleBot("6296366259:AAF9kDYm0VXqFUHBP0FEpAkGW-Fg5-aZrPU")

back = types.InlineKeyboardButton(text="raad", callback_data = "b1")  #رعد هوا الزر نفسة 

@bot.message_handler(commands=['start'])
def start(message) :
	 b=types.InlineKeyboardMarkup() 
	 b.row_width = 1
	 b.add(back) 
	 bot.reply_to(message,f"aporaad", reply_markup=b) #ابو رعد هوا اسم الزر 
	  
@bot.callback_query_handler(func=lambda call: True) 
def qwere(call):
	if call.data == "b1": 
	    bot.send_message(call.message.chat. id, f"arslan") #ارسلان هوا اجابة الزر 
@bot.message_handler(func=lambda message: message.text == "هلا")
def reply_to_specific_message(message):
    bot.reply_to(message, "اهلين ") 
@bot.message_handler(func=lambda message: message.text == "كيفك")

def reply_to_specific_message(message):
    bot.reply_to(message, "الحمد لله  \nوانت كيفك")  
@bot.message_handler(func=lambda message: message.text == "بخير")
def reply_to_specific_message(message):
    bot.reply_to(message, "تدوم عافيتك  ") 
@bot.message_handler(func=lambda message: message.text == "ابو رعد ")
def reply_to_specific_message(message):
    bot.reply_to(message, "والنعم فيك سيد الرجال  ") 
 # replace CORRECT_ANSWER with the correct answer
correct_answer = "ابو رعد السرحي"

@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.reply_to(message, "Welcome! Please answer the following question:")

@bot.message_handler(func=lambda message: True)
def check_answer(message):
  if message.text == correct_answer:
   bot.reply_to(message, "Congratulations, you gave the correct answer!")
  else:
   bot.reply_to(message, "Sorry, your answer is incorrect. Please try again.") 

bot.polling()

  polling()

  ng()
