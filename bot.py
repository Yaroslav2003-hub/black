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
        keyboard1 = telebot.types.ReplyKeyboardMarkup()
        keyboard1.row('Играть')
        keyboard1.row('Кабинет')
        bot.send_message(message.chat.id, 'Здравствуйте! Добро пожаловать в казино!', reply_markup=keyboard1)
        bot.register_next_step_handler(message, select_move)
    else:
        data1 = [message.chat.id, 0, 0, 0, 0]
        insert_func(data1)
        keyboard1 = telebot.types.ReplyKeyboardMarkup()
        keyboard1.row('Играть')
        keyboard1.row('Кабинет')
        bot.send_message(message.chat.id, 'Здравствуйте! Добро пожаловать в казино!', reply_markup=keyboard1)
        bot.register_next_step_handler(message, select_move)

def select_move(message):
    if message.text == 'Играть':
        pass
    elif message.text == 'Кабинет':       
        pass

if __name__ == '__main__':
    bot.infinity_polling()