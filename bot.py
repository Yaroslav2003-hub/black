import telebot
import mysql.connector
from telebot import types


bot = telebot.TeleBot('1326123436:AAERCbZ2FNkCg_G0jqb59bAmsg_Rh2Tnd4c')

connect = mysql.connector.connect(host='127.0.0.1', user='root', password='', port='3306', database='telegram')
cur = connect.cursor()

<<<<<<< HEAD
def connection(val):
    sql = "INSERT INTO users VALUES(%s, %s, %s, %s, %s)"
    cur.execute(sql, val)
    conn.commit()
    conn.commit()
=======
>>>>>>> 6eb0cf00825b1d7fc590465ea8beee30b3452c61
