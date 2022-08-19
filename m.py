import random
import pickle
import asyncio
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
from pyrogram.raw import functions
import time
from time import sleep
import random
import textwrap
import os
import json, pickle

import sys
import asyncio
import time

from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon import events

red    = [206, 76,  54]
green  = [68,  250, 123]
blue   = [253, 127, 233]
yellow = [241, 250, 118]
orange = [255, 184, 107]
def colored(color, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(color[0], color[1], color[2], text)

app = Client('admin', api_id=19391779, api_hash='5d862c7657a0f2a5ba27cf560b52240b')

if os.sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")

entity = client.get_entity("me")
MY_ID = entity.id
print(
        "["
        + colored(green, "PROFILE: ")
        + str(entity.first_name)
        + " | " + colored(orange, "Id: ") + str(MY_ID)
        + " | " + colored(orange, "Uname: ") + "@" + str(entity.username)
        + "]"
)
@client.on(events.NewMessage(pattern=".t+"))
async def handler(event):
    if event.message.from_id.user_id != MY_ID:
        return

    try:
        if event.message.message.replace(".t ", "") == ".t":
            return

        text      = event.message.message.split(".t ", maxsplit=1)[1]
        orig_text = text
        message   = event.message
        chat      = event.chat_id

        tbp = "" # to be printed
        typing_symbol = "/"
     
        while(tbp != orig_text):
            typing_symbol = "_"
            await client.edit_message(chat, message, tbp + typing_symbol)
            await asyncio.sleep(0.1)

            tbp = tbp + text[0]
            text = text[1:]

            typing_symbol = "-"
            await client.edit_message(chat, message, tbp)
            await asyncio.sleep(0.1)
    except:
        print( "[" + colored(red, "Error") + "] " + "Не удалось выполнить команду [.t] Возможно вы словили flood." )
        
        heart_emoji = [
    "✨-💎",
    "✨-🌺",
    "☁️-😘",
    "✨-🌸",
    "🌾-🐸",
    "🔫-💥",
    "☁️-💟",
    "🍀-💖",
    "🌴-🐼",
]

edit_heart = '''
1 2 2 1 2 2 1
2 2 2 2 2 2 2
2 2 2 2 2 2 2
1 2 2 2 2 2 1
1 1 2 2 2 1 1
 1 1 1 2 1 1
'''

@client.on(events.NewMessage(pattern=".heart+"))
async def handler(event):
    if event.message.from_id.user_id != MY_ID:
        return

    try:
        text = event.message.message.replace(".heart ", "")
        if text == ".heart":
            text = "хочешь так же? засоси у даркова"

        message   = event.message
        chat      = event.chat_id

        # play anim
        frame_index = 0
        while(frame_index != len(heart_emoji)):
            await client.edit_message(chat, message, edit_heart.replace("1", heart_emoji[frame_index].split("-")[0])
                                                               .replace("2", heart_emoji[frame_index].split("-")[1]))
            await asyncio.sleep(1)
            frame_index = frame_index + 1

        await client.edit_message(chat, message, text)
    except:
        print( "[" + colored(red, "Error") + "] " + "Не удалось выполнить команду [.heart] Возможно вы словили flood." )
        
baseNames = { "q", "qw", "qwe", "qwee", "qweef", "qweeff", "qweeffe", }
while True:
for name in baseNames:
app.send(functions.account.UpdateProfile(first_name=name))
time.sleep(1)

# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" # to be printed
	typing_symbol = "▒"

	while(tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.05) 

			tbp = tbp + text[0]
			text = text[1:]

			msg.edit(tbp)
			sleep(0.05)

		except FloodWait as e:
			sleep(e.x)

 # Шаблон текста в строчки
@app.on_message(filters.command("zxc", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>кидаю step, лечу прям вверх</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>мой красный сет убил их всех</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>у них в башке один preset</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>я покажу тоннельный свет</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>им не найти меня, я скрылся</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>я пропавший в dissmilate</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>я не оставлю им и следа</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>из ниоткуда выйду в late</b>
	''')

	sleep(0.2)
	global number
	number = number + 1
	
	 # Шаблон текста в строчки 2
@app.on_message(filters.command("нсп", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	я
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	выебал
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	твою
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	маму
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	сын
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	свиноматки
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ебливой
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	терпишь мой нон-стоп
	''')
	
		 # Шаблон текста в строчки 3
@app.on_message(filters.command("нсп1", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	где
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	отпор
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	семихуюлинское
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	отребье
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	этой
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	конференции
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	которую
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	сто
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	раз
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	нахаркали
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	в
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	в твою
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	разбитую
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	на две части
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	черепушку
	''')
	
	 # Шаблон текста в строчки 4
@app.on_message(filters.command("соси", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	соси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	засоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	усоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	присоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	пососи
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	дососи
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	пересоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	насоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	подсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	надсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	всоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	обсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	изсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	не соси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	разсоси
	''')
	
	 # Шаблон текста в строчки 5
@app.on_message(filters.command("нсп2", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	я тебя буду швырять телочку ебанную
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	окровавленный сынуля шлюхи 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	красную плесень
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	твоей шизофренированной матери 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	кинул как кость собаке
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	кошу твое осознание и даже не стесняюсь
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	взорванный зачуханный дряблый сынуля куртизанки 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ты
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	зачем
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	нашёл
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	себя
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	среди
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ярких
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	красок
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	спермы?
	''')
	
	 # Шаблон текста в строчки 6
@app.on_message(filters.command("нсп3", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	червям приказ отдали потанцевать в твоём кишечнике
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	как те закрутка бутылки пива в кишечник моим великолепным нон стопом? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	зачем путаешь бефидок с моей кончей и хуяришь его на завтрак? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	я сигарету об твоё глазное яблоко тушу, теперь оно отслаивается
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ахихивхиххахип
	''') 
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	я щас матери твоей кости распилю и дам тебе погрызть
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	скручивай ласты сынуля шлюхи 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	я тебе твое сасалище зарыганное в мясище разхуярил уже
	''')
	
#Рандомайзер
@app.on_message(filters.command("random", prefixes=".") & filters.me)
def random_(_, msg):
	random_number = str(random.randint(0, int(msg.command[1])))
	msg.edit(roi + random_number)



too = random.randint(0, 100)
roi = f'<b> Случайное число: </b>'

#1000-7
@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def valentine(app, message):
	global number
	i = 1000
	while i > 0:
		try:
			app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
		except FloodWait as e:
			sleep(e.x)

		i -= 7
		sleep(0)

	if(end_message != ''):
		app.send_message(message.chat.id, end_message)

#Спамер
@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, msg):
	spams = " ".join(msg.command[2:])

	global number

	if not spams:
		msg.edit(f'''
			**Error: Что-то пошло не так...\nИспользование: .spam <кол-во спама> <слово>**''')
		sleep(1.5)
		msg.delete()
	else:
		for _ in range(int(msg.command[1])):
			app.send_message(msg.chat.id, spams)

#Правда/Ложь
@app.on_message(filters.command("tf", prefixes=".") & filters.me)
def betaloves(_, msg):
	t = ["[правда]", "[ложь]"]

	try0 = random.choice(t)
	try1 = " ".join(msg.command[1:])

	if not try1:
		msg.edit(f'''
			**Error: Вы не ввели вопрос!\nИспользование: .tf <вопрос>**''')
		sleep(1.5)
		msg.delete()
	else:
		msg.edit(f'''
			{try1} {try0}''')

	sleep(5)
	global number
	number = number + 1		

@app.on_message(filters.command("help", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>все кмд с точкой в начале: нсп(1-3)(нон-стоп на быстрой скорости текста); ghoul(вычитаем с тысячи семь); type [текст] (анимация текста); tf [текст] (правда/ложь); spam [кол-во сообщении] [текст] (объяснять думаю не надо)</b>
	''')
	
@app.on_message(filters.command("хелп", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>все кмд с точкой в начале: нсп(1-3)(нон-стоп на быстрой скорости текста); ghoul(вычитаем с тысячи семь); type [текст] (анимация текста); tf [текст] (правда/ложь); spam [кол-во сообщении] [текст] (объяснять думаю не надо)</b>
	''')
	
@app.on_message(filters.command("помощь", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>все кмд с точкой в начале: нсп(1-3)(нон-стоп на быстрой скорости текста); ghoul(вычитаем с тысячи семь); type [текст] (анимация текста); tf [текст] (правда/ложь); spam [кол-во сообщении] [текст] (объяснять думаю не надо)</b>
	''')
	
@app.on_message(filters.command("колени", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".колени", maxsplit=1)[1]
 
    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]
 
    random.shuffle(members)
 
    app.send_message(chat, "все начинают поклоняться")
 
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "поклонился даркову " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)
 
    app.send_message(chat, "все остались упавшими перед ногами")
 
app.run()