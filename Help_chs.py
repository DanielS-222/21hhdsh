pip3 install pytelegrambotapi
import telebot

bot = telebot.TeleBot('5796080651:AAFuVvBSF3leFbo_uRzQNZGh1ItNNT1qpG4')
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Кто такой Валера Борисов')
        btn2 = types.KeyboardButton('Кто такой Дмитриев Данила')
        btn3 = types.KeyboardButton('Кто такой Сафиуллин Даниэль')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup) #ответ бота
        
    elif message.text == 'Кто такой Валера Борисов':
        bot.send_message(message.from_user.id, 'Валерий, Среднего телосложения, любит приору и Свету, готов жить в кайф и хавать шашлык, любимый жанр - золотой дождь', parse_mode='Markdown')
    elif message.text == 'Кто такой Дмитриев Данила'':
        bot.send_message(message.from_user.id, 'Данила, любит очень Дашу, обожает машины, эстет курения. Потенциал качка, ему нужен данобол, любит 99, Любимый жанр: ЛеSби', parse_mode='Markdown')

    elif message.text == 'Кто такой Сафиуллин Даниэль':
        bot.send_message(message.from_user.id, 'Любит Лизу, не АУЕ, хочет иметь машину, любит засматриваться на мальчиков, среднего телосложения, Любит шаурму, любимый жанр:gеи. ', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть?':
        
