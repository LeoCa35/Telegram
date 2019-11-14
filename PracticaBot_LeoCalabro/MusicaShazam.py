#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webbrowser
import telebot
import json


global palabra
palabra = " "
bot = telebot.TeleBot("916466394:AAGPERvk72AuupiUQhsg7b5XkHnPIzY-v2I")
json_keyboard = json.dumps({'keyboard': [["TimeUpload"], ["Duration"], ["Charasteristic"], ["Relevance"]],
                            'one_time_keyboard': True,
                            'resize_keyboard': True})
json_keyboardTimeUpload = json.dumps({'keyboard': [["Last Hour"], ["Today"], ["This week"], ["This month"], ["This year"]],
                            'one_time_keyboard': True,
                            'resize_keyboard': True})
json_keyboardDuration = json.dumps({'keyboard': [["Short"], ["Long"]],
                            'one_time_keyboard': True,
                            'resize_keyboard': True})
json_keyboardCharasteristic = json.dumps({'keyboard': [["On Live"], ["HD"], ["Subtitles"], ["HDR"], ["Creative Commons"]],
                            'one_time_keyboard': True,
                            'resize_keyboard': True})
json_keyboardRelevanced = json.dumps({'keyboard': [["Visits"], ["Classificacion"], ["Time Upload"]],
                            'one_time_keyboard': True,
                            'resize_keyboard': True})

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(
	    message, " Say me the name of the song that you want to find it with comand /music and the name of the song")


@bot.message_handler(commands=['music'])
def buscarYoutube(message):
    global palabra
    palabra = message.text[7:]
    bot.reply_to(message, " You want to find directly(/directly) or put filters(/filters)?¿ ")#, reply_markup = json_keyboard1)
    #bot.reply_to("To go directly write /directly if you want to put a filter write /filters")


@bot.message_handler(commands=['directly'])
def directo(message):
    global palabra
    webbrowser.open("https://www.youtube.com/results?search_query=" + palabra,new=2,autoraise=True)

@bot.message_handler(commands=['filters'])
def filtros(message):

    bot.send_message(message.chat.id, "What filter you want to introduce?¿ ",  reply_markup = json_keyboard)
    print(message.text)
    if (str(message.text) == "TimeUpload"):
        print("a")
        bot.send_message(message.chat.id, "Specifyme type of filter TimeUpload ", reply_markup = json_keyboardTimeUpload)
        filterTimeUpload(message)
        # filterDuration(message)
    elif str(message.text) == str("Filter duration"):
        pass



@bot.message_handler(func=lambda message: True)
def filterTimeUpload(message):
    global palabra

    if str(message.text) == str("Last Hour"):
        print("a")
        webbrowser.open("https://www.youtube.com/results?search_query=" + str(palabra)+"&sp=EgQIARAB",new=2,autoraise=True)
    elif str(message.text) == str("Today"):
        webbrowser.open("https://www.youtube.com/results?search_query=" + str(palabra)+"&sp=EgQIAhAB",new=2,autoraise=True)
    elif str(message.text) == str("This week"):
        webbrowser.open("https://www.youtube.com/results?search_query=" + str(palabra)+"&sp=EgQIAxAB",new=2,autoraise=True)
    elif str(message.text) == str("This month"):
        webbrowser.open("https://www.youtube.com/results?search_query=" + str(palabra)+"&sp=EgQIBBAB",new=2,autoraise=True)
    elif str(message.text) == str("This year"):
        webbrowser.open("https://www.youtube.com/results?search_query=" + str(palabra)+"&sp=EgQIBRAB",new=2,autoraise=True)


"""
@bot.message_handler(func=lambda message: True)
def filterDuration(message):
    global palabra
    bot.reply_to(message, "hola")
"""





"""
@bot.message_handler(func=lambda message: True)
def eleccion1(message):
    global palabra
    if str(message.text) == str("directly"):
        webbrowser.open("https://www.youtube.com/results?search_query=" + palabra,new=2,autoraise=True)

    elif str(message.text) == str("filters"):
        bot.reply_to(message, "esperate, estamos en proceso tiempo al tiempo ")
"""
    # Muestra los botones(directly, filters)

# ,reply_markup=json_keyboard1
"""
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
"""
# @bot.message_handler(func=lambda message: True)
# def respuestaBro(message):
#	bot.reply_to(message, + " Mate")
#
bot.polling()
