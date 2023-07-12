#!/bin/bash
import os
import sqlite3
import requests
import asyncio
import zipfile
import time
from json import loads
from datetime import datetime
from telebot import TeleBot, types
from requests import Session, get
import urllib

ID_CREATOR = 5343627558
ID_ADMINISTRATOR = 6058001952
ID_MEMBER_WORK_ACCOUNT = 6330333806

db = sqlite3.connect("users.db", check_same_thread=False)
sql = db.cursor()

bot = TeleBot("5558923660:AAG2Ncy1Q0aXhYYt5LLqxwjOs1njNxh7roI", parse_mode="HTML")

@bot.message_handler(commands=["start"])
def __start__(message):
    if message.from_user.id == ID_ADMINISTRATOR:
        folder_path = './BASE/'
        file_count = len(os.listdir(folder_path))
        for data in range(51):
            sql.execute("SELECT giv_base FROM users WHERE computer = ?", (data,))
            user = sql.fetchone()
            if user is not None:
                try:
                    if str(user[0]) == "0":
                        pass
                    else:
                        os.system(f"echo Ноутбук: {str(data)} -- Баз выдано: {str(user[0])} >> information.txt")
                except:
                    pass
        try:
            file_path = './information.txt'
            with open(file_path, 'rb') as file:
                bot.send_document(message.chat.id, file, reply_to_message_id=message.message_id)
                os.system("rm -rf information.txt")
        except:
            pass

        folder_path = './BASE'
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        size_in_mb = total_size / (1024 * 1024)
        bot.send_message(message.chat.id, f"""<b>Здраствуйте {message.from_user.first_name}</b>
<b>Отчёт:</b>
<b>Баз осталось:</b> <code>{file_count}</code>
<b>Размер базы</b> <code>{folder_path}</code><b>:</b> <code>{size_in_mb:.2f}</code><b>МБ из</b> <code>200</code><b>МБ</b>""")
    elif message.from_user.id == ID_CREATOR:
        folder_path = './BASE/'
        file_count = len(os.listdir(folder_path))
        for data in range(51):
            sql.execute("SELECT giv_base FROM users WHERE computer = ?", (data,))
            user = sql.fetchone()
            if user is not None:
                try:
                    if str(user[0]) == "0":
                        pass
                    else:
                        os.system(f"echo Ноутбук: {str(data)} -- Баз выдано: {str(user[0])} >> information.txt")
                except:
                    pass
        try:
            file_path = './information.txt'
            with open(file_path, 'rb') as file:
                bot.send_document(message.chat.id, file, reply_to_message_id=message.message_id)
                os.system("rm -rf information.txt")
        except:
            pass

        folder_path = './BASE'
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        size_in_mb = total_size / (1024 * 1024)
        bot.send_message(message.chat.id, f"""<b>Здраствуйте {message.from_user.first_name}</b>
<b>Отчёт:</b>
<b>Баз осталось:</b> <code>{file_count}</code>
<b>Размер базы</b> <code>{folder_path}</code><b>:</b> <code>{size_in_mb:.2f}</code><b>МБ из</b> <code>200</code><b>МБ</b>""")
    elif message.from_user.id == ID_MEMBER_WORK_ACCOUNT:
        bot.send_message(message.chat.id, """<b>Для получения базы пишем
номер ноутбука и текст база
Пример: 15 база</b>""")
    else:
        bot.send_message(message.chat.id, "<b>Доступ запрещён\nОтправляю Telegram данные разработчику...</b>")
        bot.send_message(ID_CREATOR, """<b>Попытка входа:</b>
<b>TelegramID:</b> <code>{}</code>
<b>Имя:</b> <code>{}</code>
<b>Фамилия:</b> <code>{}</code>
<b>UserName:</b> @{}

Command: /start""".format(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
        bot.send_message(ID_ADMINISTRATOR, """<b>Попытка входа:</b>
<b>TelegramID:</b> <code>{}</code>
<b>Имя:</b> <code>{}</code>
<b>Фамилия:</b> <code>{}</code>
<b>UserName:</b> @{}

Command: /start""".format(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))

@bot.message_handler(commands=["del"])
def __delete__(message):
    if message.from_user.id == ID_ADMINISTRATOR:
        markup = types.InlineKeyboardMarkup()
        yes = types.InlineKeyboardButton('Да', callback_data='yes')
        no = types.InlineKeyboardButton('Нет', callback_data='no')
        markup.add(yes, no)
        count = 0
        for a in os.listdir("./BASE"):
            count = count + 1
        bot.send_message(ID_ADMINISTRATOR, f"<b>Отправить базу которая осталась? \nОсталось: [{str(count)}]</b>", reply_markup=markup)
    elif message.from_user.id == ID_CREATOR:
        markup = types.InlineKeyboardMarkup()
        yes = types.InlineKeyboardButton('Да', callback_data='yes')
        no = types.InlineKeyboardButton('Нет', callback_data='no')
        markup.add(yes, no)
        count = 0
        for a in os.listdir("./BASE"):
            count = count + 1
        bot.send_message(ID_CREATOR, f"<b>Отправить базу которая осталась? \nОсталось: [{str(count)}]</b>", reply_markup=markup)
    else:
        pass
@bot.message_handler(commands=['send'])
def send(message):
    if message.from_user.id == ID_ADMINISTRATOR or message.from_user.id == ID_CREATOR:
        try:
            MESSAGE = f"{message.text}".split("/send ")[1]
            bot.send_message(ID_CREATOR, "<b>Сообщение отправлено...</b>")
            bot.send_message(ID_MEMBER_WORK_ACCOUNT, """<b>{}</b>""".format(MESSAGE))
        except:
            bot.send_message(message.chat.id, "<b>Произошла ошибка отправки...</b>")
    else:
        bot.send_message(message.chat.id, "<b>Доступ запрещён\nОтправляю Telegram данные разработчику...</b>")
        bot.send_message(ID_CREATOR, """<b>Попытка отправки сообщения:</b>
<b>TelegramID:</b> <code>{}</code>
<b>Имя:</b> <code>{}</code>
<b>Фамилия:</b> <code>{}</code>
<b>UserName:</b> @{}

Command: /send""".format(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))


@bot.message_handler(commands=['rename'])
def rename(message):
    if message.from_user.id == ID_ADMINISTRATOR or message.from_user.id == ID_CREATOR:
        try:
            dir = './BASE'
            old_file = os.path.join(dir, '{}'.format(f"{message.text}".split("/rename ")[1].split(" ")[0]))
            new_file = os.path.join(dir, '{}'.format(f"{message.text}".split("/rename ")[1].split(" ")[1]))

            os.rename(old_file, new_file)
            bot.send_message(message.chat.id, "<b>Переименовано</b>")
        except:
            bot.send_message(message.chat.id, """<b>Ошибка
Для того что-бы переименовать файл
нужно создавать его одним словом.
Пример:</b>
    <i>новый_файл.txt --> Это верно.
    новый файл.txt --> Это не верно.</i>""")
    else:
        bot.send_message(message.chat.id, "<b>Доступ запрещён\nОтправляю Telegram данные разработчику...</b>")
        bot.send_message(ID_CREATOR, """<b>Попытка удаления файла:</b>
<b>TelegramID:</b> <code>{}</code>
<b>Имя:</b> <code>{}</code>
<b>Фамилия:</b> <code>{}</code>
<b>UserName:</b> @{}

Command: /rename \n{}""".format(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text))

@bot.message_handler(commands=['delete'])
def delete(message):
    if message.from_user.id == ID_ADMINISTRATOR or message.from_user.id == ID_CREATOR:
        try:
            FILE = f"{message.text}".split("/delete ")[1]
            os.remove("./BASE/{}".format(FILE))
            bot.send_message(ID_ADMINISTRATOR, "<b>Удалён файл:</b> <code>{}</code>".format(FILE))
            bot.send_message(ID_CREATOR, "<b>Удалён файл:</b> <code>{}</code>".format(FILE))
        except:
            bot.send_message(message.chat.id, "<b>Файл не найден.</b>")
    else:
        bot.send_message(message.chat.id, "<b>Доступ запрещён\nОтправляю Telegram данные разработчику...</b>")
        bot.send_message(ID_CREATOR, """<b>Попытка удаления файла:</b>
<b>TelegramID:</b> <code>{}</code>
<b>Имя:</b> <code>{}</code>
<b>Фамилия:</b> <code>{}</code>
<b>UserName:</b> @{}

Command: /delete""".format(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
        bot.send_message(ID_ADMINISTRATOR, """<b>Попытка удаления файла:</b>
<b>TelegramID:</b> <code>{}</code>
<b>Имя:</b> <code>{}</code>
<b>Фамилия:</b> <code>{}</code>
<b>UserName:</b> @{}

Command: /delete""".format(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
# @bot.message_handler(commands=['number'])
# def number(message):
#     number = "{}".format(message).split("/number ")[1]
#     headers = {
#                 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
#     }
#     url = "https://nums.hanumi.net/api/get_info?phone=79009527108".format(number)
#     req = requests.get(url, headers=headers, proxies={"http": "https://87.103.133.243:4444"}).text

#     time_zone = loads(requ).get("time_zone")
#     operator =  loads(requ).get("operator")
#     region =  loads(requ).get("region")
#     print(f"""<b>Регион:</b> <code>{region}</code>
# <b>Оператор:</b> <code>{operator}</code>
# <b>Часовой пояс:</b> <code>+{time_zone}</code>""")
@bot.message_handler(commands=['list'])
def list_db(message):
    if message.from_user.id == ID_ADMINISTRATOR or message.from_user.id == ID_CREATOR:
        try:
            FILES = os.listdir("./BASE/")
            ARRAY_LIST = []
            for index, FILES in enumerate(FILES):
                ARRAY_LIST.append(f"{index+1})  {FILES}")

            result = "\n".join(ARRAY_LIST)
            bot.send_message(message.chat.id, f"<b>{result}</b>")
        except:
            bot.send_message(message.chat.id, "<b>Файлов нету</b>")
    else:
        bot.send_message(message.chat.id, "<b>Доступ запрещён\nОтправляю Telegram данные разработчику...</b>")
        bot.send_message(ID_CREATOR, """<b>Попытка входа:</b>
<b>TelegramID:</b> <code>{}</code>
<b>Имя:</b> <code>{}</code>
<b>Фамилия:</b> <code>{}</code>
<b>UserName:</b> @{}

Command: /list""".format(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
        bot.send_message(ID_ADMINISTRATOR, """<b>Попытка входа:</b>
<b>TelegramID:</b> <code>{}</code>
<b>Имя:</b> <code>{}</code>
<b>Фамилия:</b> <code>{}</code>
<b>UserName:</b> @{}

Command: /list""".format(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
@bot.message_handler(commands=['unzip'])
def handle_unzip(message):
    dir_ = os.listdir("./")
    if "база.zip" in dir_:
        chat_id = message.chat.id
        zip_path = 'база.zip'
        extract_dir = './BASE/'

        bot.send_chat_action(chat_id, 'typing')

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            total_files = len(file_list)
            extracted_files = 0
            progress_message = bot.send_message(chat_id, '<code>0%</code> <b>файлов распаковано</b>')

            for file in file_list:
                zip_ref.extract(file, extract_dir)
                extracted_files += 1
                progress = f'<code>{int(extracted_files/total_files*100)}%</code> <b>файлов распаковано</b>'
                bot.edit_message_text(progress, chat_id, progress_message.message_id)

        bot.send_message(chat_id, '<b>Распаковка архива завершена</b>')
        os.system("rm -rf база.zip")
    else:
        bot.send_message(message.chat.id, "<b>Архив .zip не найден</b>")
@bot.message_handler(content_types=['document'])
def handle_document(message):
    if message.from_user.id == ID_ADMINISTRATOR:
        if message.document.mime_type == "application/zip":
            folder_path = './'
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(file_path)
            size_in_mb = total_size / (1024 * 1024)
            if size_in_mb >= 200:return bot.send_message(message.chat.id, f"<b>База переполнена:</b> <code>{size_in_mb}</code><b>MB</b>")
            file_info = bot.get_file(message.document.file_id)
            file_name = message.document.file_name
            file_url = f"https://api.telegram.org/file/bot5558923660:AAG2Ncy1Q0aXhYYt5LLqxwjOs1njNxh7roI/{file_info.file_path}"

            file_path = './' + file_name
            urllib.request.urlretrieve(file_url, file_path)

            bot.send_message(message.chat.id, f"<b>Файл </b><code>{file_name}</code> <b>.zip введите команду /unzip</b>")
        else:
            folder_path = './BASE/'
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(file_path)
            size_in_mb = total_size / (1024 * 1024)
            if size_in_mb >= 200:return bot.send_message(message.chat.id, f"<b>База переполнена:</b> <code>{size_in_mb}</code><b>MB</b>")
            file_info = bot.get_file(message.document.file_id)
            file_name = message.document.file_name
            file_url = f"https://api.telegram.org/file/bot5558923660:AAG2Ncy1Q0aXhYYt5LLqxwjOs1njNxh7roI/{file_info.file_path}"

            file_path = './BASE/' + file_name
            urllib.request.urlretrieve(file_url, file_path)

            bot.send_message(message.chat.id, f"<b>Файл </b><code>{file_name}</code> <b>.zip введите команду /unzip</b>")
    else:
        bot.send_message(message.chat.id, f"<b>К сожалению только администратор может загрузить файл.</b>")


@bot.message_handler(content_types=["text"])
def message(message):
    if "база" in message.text.lower():
        BASE = os.listdir("./BASE/")
        message_requests = f"{message.text}".split(" ")
        message_number_computer = message_requests[0]
        try:
            number_device = int(message_number_computer)
        except:return bot.send_message(message.chat.id, "<b>Не распознано,\nвозможно введённые данные\nне являються числом.</b>", reply_to_message_id=message.message_id)
        sql.execute("SELECT * FROM users WHERE computer = {}".format(message_number_computer))
        if sql.fetchone() is None:return bot.send_message(message.chat.id, "<b>Устройство под номеров [</b><code>{}</code><b>] не найдено...</b>".format(number_device), reply_to_message_id=message.message_id)
        if message_requests[1].lower() == "база":
            if len(BASE) <= 5:
                bot.send_message(ID_CREATOR, "<b>Внимание осталось {} баз</b>".format(len(BASE)))
                bot.send_message(ID_ADMINISTRATOR, "<b>Внимание осталось {} баз</b>".format(len(BASE)))
            if message.from_user.id == ID_MEMBER_WORK_ACCOUNT:
                try:
                    if len(BASE) == 0:return bot.send_message(ID_MEMBER_WORK_ACCOUNT, "<b>База закончилась,\nобратитесь к программисту...</b>", reply_to_message_id=message.message_id)
                except:return bot.send_message(ID_MEMBER_WORK_ACCOUNT, "<b>База закончилась,\nобратитесь к программисту...</b>")
            else:
                pass
            bot.send_message(ID_MEMBER_WORK_ACCOUNT, "База загружаеться...")
            file_path = './BASE/{}'.format(BASE[0])
            folder_path__ = './BASE/'
            COUNT_BASE = len(os.listdir(folder_path__))
            try:
                with open(file_path, 'rb') as file:
                    bot.send_message(ID_CREATOR, f"<b>Ноутбук</b> <code>{message_number_computer}</code> <b>взял базу [</b><code>{file.name}</code><b>].\nБаз осталось: </b><code>{COUNT_BASE-1}</code>")
                    bot.send_message(ID_ADMINISTRATOR, f"<b>Ноутбук</b> <code>{message_number_computer}</code> <b>взял базу [</b><code>{file.name}</code><b>].\nБаз осталось: </b><code>{COUNT_BASE-1}</code>")
                    sql.execute("UPDATE users SET giv_base = giv_base + 1 WHERE computer = {}""".format(message_number_computer))
                    db.commit()
                    bot.send_document(message.chat.id, file, reply_to_message_id=message.message_id)
                    os.remove(file.name)
            except:
                bot.send_message(ID_MEMBER_WORK_ACCOUNT, "<b>Подождите 10 секунд вносятся изменения...</b>")
    elif "базу" in message.text.lower():
        BASE = os.listdir("./BASE/")
        message_requests = f"{message.text}".split(" ")
        message_number_computer = message_requests[0]
        try:
            number_device = int(message_number_computer)
        except:return bot.send_message(message.chat.id, "<b>Не распознано,\nвозможно введённые данные\nне являються числом.</b>", reply_to_message_id=message.message_id)
        sql.execute("SELECT * FROM users WHERE computer = {}".format(message_number_computer))
        if sql.fetchone() is None:return bot.send_message(message.chat.id, "<b>Устройство под номером [</b><code>{}</code><b>] не найдено...</b>".format(number_device), reply_to_message_id=message.message_id)
        if message_requests[1].lower() == "базу":
            if len(BASE) <= 5:
                bot.send_message(ID_CREATOR, "<b>Внимание осталось {} баз</b>".format(len(BASE)))
                bot.send_message(ID_ADMINISTRATOR, "<b>Внимание осталось {} баз</b>".format(len(BASE)))
            if message.from_user.id == ID_MEMBER_WORK_ACCOUNT:
                try:
                    if len(BASE) == 0:return bot.send_message(ID_MEMBER_WORK_ACCOUNT, "<b>База закончилась,\nобратитесь к программисту...</b>", reply_to_message_id=message.message_id)
                except:return bot.send_message(ID_MEMBER_WORK_ACCOUNT, "<b>База закончилась,\nобратитесь к программисту...</b>")
            else:
                pass
            bot.send_message(ID_MEMBER_WORK_ACCOUNT, "База загружаеться...")
            file_path = './BASE/{}'.format(BASE[0])
            folder_path__ = './BASE/'
            COUNT_BASE = len(os.listdir(folder_path__))
            with open(file_path, 'rb') as file:
                bot.send_message(ID_CREATOR, f"<b>Ноутбук</b> <code>{message_number_computer}</code> <b>взял базу [</b><code>{file.name}</code><b>].\nБаз осталось: </b><code>{COUNT_BASE}</code>")
                bot.send_message(ID_ADMINISTRATOR, f"<b>Ноутбук</b> <code>{message_number_computer}</code> <b>взял базу [</b><code>{file.name}</code><b>].\nБаз осталось: </b><code>{COUNT_BASE}</code>")
                sql.execute("UPDATE users SET giv_base = giv_base + 1 WHERE computer = {}""".format(message_number_computer))
                db.commit()
                bot.send_document(message.chat.id, file, reply_to_message_id=message.message_id)
                os.remove(file.name)


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == 'yes':
        sql.execute("UPDATE users SET giv_base = 0")
        db.commit()
        BASE = os.listdir("./BASE/")
        if not BASE:
            bot.send_message(call.message.chat.id, "<b>К сожалению база пуста...</b>")
        else:
            bot.send_message(call.message.chat.id, "<b>Отправка базы...</b>")
            for FILES in BASE:
                bot.send_document(call.message.chat.id, open(f"./BASE/{FILES}", 'rb'))
    elif call.data == 'no':
        BASE = os.listdir("./BASE/")
        for DELETE in BASE:
            os.remove("./BASE/{}".format(DELETE))
            print("remove ./BASE/{}".format(DELETE))
        bot.answer_callback_query(call.id, 'База удалена')

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=1)