#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webbrowser
import telebot
import json


global palabra
palabra = " "
bot = telebot.TeleBot("916466394:AAGPERvk72AuupiUQhsg7b5XkHnPIzY-v2I")
json_keyboard = json.dumps({'keyboard': [["Filter Time"], ["Filtro duration"], ["Filtro charasteristic"], ["Filtro relevance"]],
                            'one_time_keyboard': True,
                            'resize_keyboard': True})
json_keyboard1 = json.dumps({'keyboard': [["directly"], ["filters"]],
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
    bot.reply_to(message, " You want to find directly or put filters?¿ ", reply_markup = json_keyboard1)


@bot.message_handler(func=lambda message: True)
def eleccion1(message):
    global palabra
    if str(message.text) == str("directly"):
        webbrowser.open("https://www.youtube.com/results?search_query=" + palabra,new=2,autoraise=True)

    elif str(message.text) == str("filters"):
        bot.reply_to(message, "esperate, estamos en proceso tiempo al tiempo ")

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
