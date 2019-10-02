import telebot

bot = telebot.TeleBot("916466394:AAGPERvk72AuupiUQhsg7b5XkHnPIzY-v2I")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Leo tio eres el mejor.")

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)
@bot.message_handler(func=lambda message: True)
def respuestaBro(message):
	bot.reply_to(message, + " Mate")

bot.polling()
