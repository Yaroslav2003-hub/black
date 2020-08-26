import telebot
import mysql.connector
from telebot import types


bot = telebot.TeleBot('1326123436:AAERCbZ2FNkCg_G0jqb59bAmsg_Rh2Tnd4c')

conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', port='3306', database='telegram')
cur = conn.cursor()

def insert_func(val):
    sql = "INSERT INTO users VALUES(%s, %s, %s, %s, %s)"
    cur.execute(sql, val)
    conn.commit()


@bot.message_handler(commands=['start'])
def start_func(message):
    sql = ("SELECT * FROM users WHERE telegram_id = %s ")
    data = [message.chat.id]
    cur.execute(sql, data)
    result = cur.fetchall()
    if len(result) > 0:
        bot.send_message(message.chat.id, 'Здравствуйте! Добро пожаловать в казино!')
    else:
        data1 = [message.chat.id, 0, 0, 0, 0]
        insert_func(data1)
        bot.send_message(message.chat.id, 'Здравствуйте! Добро пожаловать в казино!')



if __name__ == '__main__':
    bot.infinity_polling()