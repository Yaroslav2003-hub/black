import telebot
import mysql.connector

#БД:
conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', port='3306', database='telegram')
cur = conn.cursor()

def insertfunc(val):
    sql = "INSERT INTO messaging VALUES(%s, %s, %s)"
    cur.execute(sql, val)
    conn.commit()

#функции для работы:
def proverka(list, id):
    k = int(0)
    sovp = int(0)
    for k in range (0, (len(list))):
        if id == list[k]:
            sovp+=1
    if sovp == 0: 
        return 0
    else:
        return 1
def brute_search(list, item):
    for i in range (0, len(list)):
        if item == list[i]:
            item1 = i
    return item1
#подключение файла с паролем:
f = open("password.txt", "r")
password = f.read()

bot = telebot.TeleBot('1108938461:AAHbRO5dGtudQdbPV0qP11ZKDvKINw6PNi8')  #поддержка

online = []

quest1 = []
quest2 = []
helpers = []

#команды для старта работы бота:
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Щоб отримати консультацію тех. підтримки натисність /helper , та дочекайтесь підключення спеціаліста.")
@bot.message_handler(commands=["login"])
def login_to_TS(message):
    if (proverka(online, message.chat.id) == 0):
        bot.send_message(message.chat.id, "Введіть пароль авторизації")
        bot.register_next_step_handler(message, password_func)
    else:
        bot.send_message(message.chat.id, "Ви авторизовані. Вийти з системи /logout")
def password_func(message):
    if message.text == password:
            bot.send_message(message.chat.id, "Авторизація успішна")
            online.append(message.chat.id)           
    else:
        bot.send_message(message.chat.id, "Не правильний пароль")


@bot.message_handler(commands=["logout"])
def logout(message):
    if message.chat.id in online: 
        online.pop(brute_search(online, message.chat.id))
        bot.send_message(message.chat.id, "Ви вийшли з ситеми")
    else:
        bot.send_message(message.chat.id, "Ви не авторизовані, авторизуйтесь /login")

@bot.message_handler(commands=["helper"])
def helper(message):
    quest1.append(message.chat.id)
    bot.send_message(message.chat.id, "Підключаємо спеціаліста.")
    bot.register_next_step_handler(message, request)
    bot.register_next_step_handler(message, messanger)
    for i in range (0, len(online)):
        bot.send_message(online[i], "Запит на підключення, щоб відповісти /connect")
def request(message):
    for i in range (0, len(online)):
        bot.send_message(online[i], "Запит на підключення, щоб відповісти /connect")

@bot.message_handler(commands=["connect"])
def connect(message):
    if message.chat.id in online:
        if (len(quest1) > 0):
            online.pop(brute_search(online, message.chat.id))
            helpers.append(message.chat.id)
            quest2.append(quest1[0])
            quest1.pop(0)
            bot.send_message(message.chat.id, ("Зв'язок встановлено. щоб закінчити діалог натисніть /finish" + str(quest2[(brute_search(helpers, message.chat.id))])))
            bot.send_message(quest2[(brute_search(helpers, message.chat.id))], "Спеціаліста підключено!")
            if (len(quest1) > 0):
                bot.register_next_step_handler(message, request)
        else:
            bot.send_message(message.chat.id, "Відсутні запити")
    else:
        bot.send_message(message.chat.id, "Щоб отримати консультацію написніть /helper , та дочекайтесь підключення спеціаліста.")

@bot.message_handler(content_types=["text"])
def messanger(message):
    if ((message.text == '/finish') and (message.chat.id in helpers)):
        online.append(message.chat.id)
        r = brute_search(helpers, message.chat.id)
        m = quest2[r]
        quest2.pop(r)
        helpers.pop(r)
        bot.send_message(message.chat.id, 'Повернення в список підключення.')
        bot.send_message(m, 'Дякуємо за ваше звернення, якщо виникли додаткові питання скористайтесь /helper .')

        if len(quest1) > 0:
            bot.register_next_step_handler(message, request)
    else:
        if message.chat.id in quest2:            
            bot.send_message(helpers[(brute_search(quest2, message.chat.id))], message.text)
            qwe= [message.chat.id, message.text, helpers[(brute_search(quest2, message.chat.id))]]
            insertfunc(qwe)
        if ((message.chat.id in helpers) and (brute_search(helpers, message.chat.id) < len(quest2))):
            bot.send_message(quest2[(brute_search(helpers, message.chat.id))], message.text)
            qwe= [message.chat.id, message.text, quest2[(brute_search(helpers, message.chat.id))]]
            insertfunc(qwe)
if __name__ == '__main__':
    bot.infinity_polling()

