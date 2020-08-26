import telebot
import mysql.connector
from telebot import types


bot = telebot.TeleBot('1326123436:AAERCbZ2FNkCg_G0jqb59bAmsg_Rh2Tnd4c')

connect = mysql.connector.connect(host='127.0.0.1', user='root', password='', port='3306', database='telegram')
cur = connect.cursor()

