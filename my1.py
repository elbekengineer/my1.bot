


import telebot

from telebot import types
vaqt = "Bomdod - 06:10, Peshin - 13:00, Asr - 17:20, SHom - 18:50 , Hufton - 20:20 ,               14 , 20- MART"

photo_url = 'https://ibb.co/7xV7KDGs'

bot = telebot.TeleBot("5377853626:AAHscLeK1OZniqmV8cEICvz_BYPXZkTqbms")

@bot.message_handler(commands=['start'])
def hello(message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
	keyboard.add(types.KeyboardButton('Namoz vaqtlari'), types.KeyboardButton('Taqvim'))
	bot.send_message(message.chat.id,f'Assalomu aleykum  {message.from_user.first_name}!', reply_markup=keyboard)

@bot.message_handler(content_types = ['text'])
def get_user_text(message):
	if message.text == 'Taqvim':
		bot.send_photo(message.chat.id, photo_url, caption='Ramazon Taqvimi')
	elif message.text == 'Namoz vaqtlari':
		bot.send_message(message.chat.id,vaqt)
	if message.text == "Jaga":
		bot.send_message(message.chat.id,"Agar kelsa kallamni kesaman deydigan odam")
	if message.text == "Futbol":
		bot.send_message(message.chat.id,"Juma kuni 22:00 da SHavqiy maydonida")
	if message.text == "+":
		bot.send_message(message.chat.id,"aka siz zuri siz")
	if message.text == "futbol":
		bot.send_message(message.chat.id,"Juma kuni 22:00 da SHavqiy maydonida")
	if message.text == "Multoni":
		bot.send_message(message.chat.id,"Kelib chiqishi Multon shahridan bulgan,bir halqning nomi ")
	if message.text == "-":
		bot.send_message(message.chat.id,"Sizga soglik tilaymiz")
	if message.text == "++":
		bot.send_message(message.chat.id,"Sizga ikktami")
	if message.text == "jaga":
		bot.send_message(message.chat.id,"Iftor qachon endi")
	if message.text == "ха":
		bot.send_message(message.chat.id,"kuz tegmasin")
	if message.text == "Ха":
		bot.send_message(message.chat.id,"kuz tegmasin")
	if message.text == "Ha":
		bot.send_message(message.chat.id,"kuz tegmasin")
	if message.text == "ha":
		bot.send_message(message.chat.id,"kuz tegmasin")
	if message.text == "Футбол":
		bot.send_message(message.chat.id,"Juma kuni 22:00 da SHavqiy maydonida")
	if message.text == "футбол":
		bot.send_message(message.chat.id,"Juma kuni 22:00 da SHavqiy maydonida")
	if message.text == "Жага":
		bot.send_message(message.chat.id,"Agar kelsa kallamni kesaman deydigan odam")
	if message.text == "жага":
		bot.send_message(message.chat.id,"Agar kelsa kallamni kesaman deydigan odam")
	if message.text == "jaga aka":
		bot.send_message(message.chat.id,"Iftor qachon endi")
	if message.text == "Jaga aka":
		bot.send_message(message.chat.id,"Iftor qachon endi")
	if message.text == "Мултони":
		bot.send_message(message.chat.id,"Kelib chiqishi Multon shahridan bulgan,bir halqning nomi ")
	if message.text == "мултони":
		bot.send_message(message.chat.id,"Kelib chiqishi Multon shahridan bulgan,bir halqning nomi ")
#	f'Assalomu aleykum  {message.from_user.first_name}!', reply_markup=keyboard)
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
	bot.send_message(message.chat.id, 'Gap yuq !')


@bot.message_handler(content_types=['voice'])
def get_user_voice(message):
	bot.send_message(message.chat.id,'Jaga akam nima desalar shu')



bot.polling(none_stop=True)