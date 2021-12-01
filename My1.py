import telebot
from telebot import types

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("👀 Репозиторий Дмитрия")
	item2 = types.KeyboardButton("😎 Написать Дмитрию")

	markup.add(item1, item2)


	bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}! Меня зовут Альф! Я хороший друг Дмитрия Учанина и, по совместительству, его помощник! Попробуйте поздороваться! А еще, Вы можете понажимать кнопочки)".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#приветствие
@bot.message_handler(content_types=['text'])

def hipeople(message):
		if message.text == '👀 Репозиторий Дмитрия':
			bot.send_message(message.chat.id, 'https://github.com/Altfanat')
		elif message.text == '😎 Написать Дмитрию':
			bot.send_message(message.chat.id, 'http://t.me/uchanin')
		elif message.text.lower() == 'hi' or message.text.lower() == 'hello' or message.text.lower() == 'yo': \
				bot.reply_to(message, 'Привет! Я тебя понял, но давай по-русски, я только учусь)')
		elif message.text.lower() == 'привет' or message.text.lower() == 'прива' or message.text.lower() == 'прив' \
or message.text.lower() == 'здравствуйте' or message.text.lower() == 'здравствуй' or message.text.lower() == 'здарова' \
or message.text.lower() == 'здаров' or message.text.lower() == 'хай' or message.text.lower() == 'йоу': \
bot.reply_to(message, 'Привет!')
		else:
			bot.send_message(message.chat.id, 'Пока не знаю, что на это ответить 😔')

bot.polling(none_stop=True)