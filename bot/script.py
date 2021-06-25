import telebot
import pymysql
import random
bot = telebot.TeleBot("1861147345:AAFlnrsXuft-vBCYxxmJrZE76L9ZljQ7VZU")

users = {}

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, "Привет, я бот для Викторин\nНапишите /add для добавления вопроса в викторину")
    users[str(message.from_user.id)] = {}

@bot.message_handler(commands=["add"])
def add(message):
    bot.send_message(message.from_user.id, "Вы решили добавить вопрос! Пожалуйста, введите текст вопроса")
    bot.register_next_step_handler(message, getQuestionText)

@bot.message_handler(commands=["quiz"])
def quiz(message):
    bot.send_message(message.from_user.id, "Давайте начнем викторину! Сколько вопросов вы хотите?")
    bot.register_next_step_handler(message, getQuizCount)

def getQuizCount(message):
    users[str(message.from_user.id)]["count"] = int(message.text)
    sql = "SELECT * FROM `Questions`"
    connection = pymysql.connect(host="141.8.192.37",
                                user="a0221501_quiz", 
                                database="a0221501_quiz", 
                                password="ivgpuquiz2021")
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        users[str(message.from_user.id)]["questions"] = cursor.fetchall()
    users[str(message.from_user.id)]["asked"] = set()
    while len(users[str(message.from_user.id)]["asked"]) != users[str(message.from_user.id)]["count"]:
        questionIndex = random.randint(0, len(users[str(message.from_user.id)]["questions"]))
        if(questionIndex not in users[str(message.from_user.id)]["asked"]):
            users[str(message.from_user.id)]["asked"].add(questionIndex)
    for i in users[str(message.from_user.id)]["asked"]:
        bot.send_message(message.from_user.id, users[str(message.from_user.id)]["questions"][i]["Question"])
#         bot.register_next_step_handler(message, getAnwer)


# def getAnwer(message):
    

def getQuestionText(message):
    users[str(message.from_user.id)]["question"] = message.text
    bot.send_message(message.from_user.id, "Отлично! Теперь введите правильный ответ!")
    bot.register_next_step_handler(message, getAnswerText)

def getAnswerText(message):
    users[str(message.from_user.id)]["answer"] = message.text
    bot.send_message(message.from_user.id, "Отлично! Идет добавление вопроса в базу...")
    sql = "INSERT INTO `Questions` (`Question`, `Answer`, `Author`) VALUES (%s, %s, %s)"
    connection = pymysql.connect(host="141.8.192.37",
                                user="a0221501_quiz", 
                                database="a0221501_quiz", 
                                password="ivgpuquiz2021")
    with connection.cursor() as cursor:
        cursor.execute(sql, (users[str(message.from_user.id)]["question"], users[str(message.from_user.id)]["answer"], message.from_user.id))
        connection.commit()
        bot.send_message(message.from_user.id, "Вопрос успешно добавлен в базу!")

bot.polling(none_stop=True)