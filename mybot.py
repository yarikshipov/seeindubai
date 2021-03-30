# Подключаем Telegram API 
import telebot
import os
from flask import Flask, request
import logging

# Подключаем библиотеку для создания кнопок
from telebot import types
 
# Объявляем бота
bot = telebot.TeleBot('1739533668:AAFABHGc2LmgWEzKCHF7uz-wFFtCWMSZF2I')

def create_keyboard():
    # Создаём тип для кнопок
    keyboard = types.InlineKeyboardMarkup()
    # Создаём кнопку 
    btn1 = types.InlineKeyboardButton(text="1", callback_data="1")
    # Создаём кнопку 
    btn2 = types.InlineKeyboardButton(text="2", callback_data="2")
    # Создаём кнопку 
    btn3 = types.InlineKeyboardButton(text="3", callback_data="3")
    # Создаём кнопку 
    btn4 = types.InlineKeyboardButton(text="4", callback_data="4")
    # Создаём кнопку 
    btn5 = types.InlineKeyboardButton(text="5", callback_data="5")
    # Создаём кнопку 
    btn6 = types.InlineKeyboardButton(text="6", callback_data="6")
    # Создаём кнопку 
    btn7 = types.InlineKeyboardButton(text="7", callback_data="7")
    # Создаём кнопку 
    btn8 = types.InlineKeyboardButton(text="8", callback_data="8")
    # Создаём кнопку 
    btn9 = types.InlineKeyboardButton(text="9", callback_data="9")
    # Создаём кнопку 
    btn10 = types.InlineKeyboardButton(text="10", callback_data="10")
    # Добавляем кнопку в специальный список
    keyboard.row(btn1, btn2, btn3, btn4, btn5)
    keyboard.row(btn6,btn7,btn8,btn9,btn10)
    # Возвращаем кнопки
    return keyboard

# Обозначаем чтобы функция срабатывала при команде /start
@bot.message_handler(commands=['start'])
# Объявляем функцию
def start_bot(message):
    # Создаём кнопки
    keyboard = create_keyboard()
    # Отправляем сообщение пользователю
    bot.send_message(
        message.chat.id, # Идентификатор ID
        "Привет, вот список 10 достопремечательностей Дубая, которые ты обязан посетить. Нажми на кнопку ниже, чтобы узнать больше", # Текст сообщения
        reply_markup=keyboard # Кнопки
    )

# Декоратор который означает для получения каких-то значений  
@bot.callback_query_handler(func=lambda call: True)
# Создаём функцию
def callback_inline(call):
    # Делаем кнопки
    keyboard = create_keyboard()
    # Проверяем есть ли сообщение
    if call.message:
        # Если значение кнопки равно одному то
        if call.data == "1":
            # Открываем картинку 1
            img = open('1.jpg', 'rb')
            # Отправляем картинку
            bot.send_photo(
                chat_id=call.message.chat.id, # Идентификатор чата 
                photo=img, # Картинка
                caption="Бурдж-Халифа - сверхвысотный небоскрёб высотой 828 метров в Дубае (ОАЭ), самое высокое и самое многоэтажное здание, самое высокое сооружение, единственный 828-метровый и 163-этажный небоскрёб в мире. Уступчатая форма здания напоминает сталагмит", # Текст к картинки
                reply_markup=keyboard # Кнопки
            )
            # Закрываем картинку
            img.close()
        elif call.data == "2": #Если значение равно двум то
            # Открываем картинку 2
            img = open('2.jpg', 'rb')
            # Отправляем картинку
            bot.send_photo(
                chat_id=call.message.chat.id, # Идентификатор чата 
                photo=img, # Картинка
                caption="Фонтан Дубай — музыкальный фонтан, расположенный в искусственном озере площадью свыше 12 га рядом с небоскрёбом Бурдж-Халифа в центре Дубая", # Текст к картинки
                reply_markup=keyboard # Кнопки
            )
            # Закрываем картинку
            img.close()
        elif call.data == "3": #Если значение равно трем то
            # Открываем картинку 3
            img = open('3.jpg', 'rb')
            # Отправляем картинку
            bot.send_photo(
                chat_id=call.message.chat.id, # Идентификатор чата 
                photo=img, # Картинка
                caption="The Dubai Mall — самый крупный торгово-развлекательный центр в мире, расположенный в даунтауне Дубай",
                reply_markup=keyboard # Кнопки
            )
            # Закрываем картинку
            img.close()
        elif call.data == "4": #Если значение равно трем то
            # Открываем картинку 3
            img = open('4.jpg', 'rb')
            # Отправляем картинку
            bot.send_photo(
                chat_id=call.message.chat.id, # Идентификатор чата 
                photo=img, # Картинка
                caption="Dubai Miracle Garden -то один из крупнейших в мире цветочных парков, который за буквально несколько лет своей работы сумел заслужить внимание мировой общественности, и стал одним из ключевых объектов привлечения туристов в Дубай",
                reply_markup=keyboard # Кнопки
            )
            # Закрываем картинку
            img.close()
        elif call.data == "5": #Если значение равно трем то
            # Открываем картинку 3
            img = open('5.jpg', 'rb')
            # Отправляем картинку
            bot.send_photo(
                chat_id=call.message.chat.id, # Идентификатор чата 
                photo=img, # Картинка
                caption="Global Village Дубай (Всемирная деревня) – это грандиозная ярмарка, которая раньше работала во время зимнего торгового фестиваля (проводится каждый год), а теперь, в связи с большой популярностью, проводится с ноября по апрель.",
                reply_markup=keyboard # Кнопки
            )
            # Закрываем картинку
            img.close()
        elif call.data == "6": #Если значение равно трем то
            # Открываем картинку 3
            img = open('6.jpg', 'rb')
            # Отправляем картинку
            bot.send_photo(
                chat_id=call.message.chat.id, # Идентификатор чата 
                photo=img, # Картинка
                caption="С момента открытия в 2018 году Dubai Frame стала излюбленным местом гостей и жителей города. Необычное архитектурное сооружение в парке Zabeel Park служит своеобразным «мостом» между прошлым и настоящим Дубая.",
                reply_markup=keyboard # Кнопки
            )
            # Закрываем картинку
            img.close()
        elif call.data == "7": #Если значение равно трем то
            # Открываем картинку 3
            img = open('7.jpg', 'rb')
            # Отправляем картинку
            bot.send_photo(
                chat_id=call.message.chat.id, # Идентификатор чата 
                photo=img, # Картинка
                caption="Aquaventure, лучший аквапарк Ближнего Востока по версии TripAdvisor, — это мир водных развлечений и ярких впечатлений в Дубае.",
                reply_markup=keyboard # Кнопки
            )
            # Закрываем картинку
            img.close()
        elif call.data == "8": #Если значение равно трем то
            # Открываем картинку 3
            img = open('8.jpg', 'rb')
            # Отправляем картинку
            bot.send_photo(
                chat_id=call.message.chat.id, # Идентификатор чата 
                photo=img, # Картинка
                caption="La Mer. Пляж разделен на две части полуостровом, на котором построена пешеходная улица с ресторанами и аквапарк. Первая часть находится слева, она более развитая, уютная и ухоженная.",
                reply_markup=keyboard # Кнопки
            )
            # Закрываем картинку
            img.close()
        elif call.data == "9": #Если значение равно трем то
            # Открываем картинку 3
            img = open('9.jpg', 'rb')
            # Отправляем картинку
            bot.send_photo(
                chat_id=call.message.chat.id, # Идентификатор чата 
                photo=img, # Картинка
                caption="Бурдж-эль-Араб — отель в Дубае, самом крупном городе Объединённых Арабских Эмиратов. Здание стоит в море на расстоянии 280 метров от берега на искусственном острове, соединённом с землёй при помощи моста",
                reply_markup=keyboard # Кнопки
            )
            # Закрываем картинку
            img.close()
        elif call.data == "10": #Если значение равно трем то
            # Открываем картинку 3
            img = open('10.jpg', 'rb')
            # Отправляем картинку
            bot.send_photo(
                chat_id=call.message.chat.id, # Идентификатор чата
                photo=img, # Картинка
                caption="Ski Dubai — парк развлечений и первый горнолыжный комплекс на Ближнем Востоке под крышей и один из крупнейших в мире с площадью около 22,5 тыс. м², круглый год покрытый искусственным снегом. Вместимость — 1,5 тысячи посетителей. Расположен в торговом комплексе Mall of the Emirates.",
                reply_markup=keyboard # Кнопки
            )
            # Закрываем картинку
            img.close()
# Проверим, есть ли переменная окружения Хероку (как ее добавить смотрите ниже)
#if "HEROKU" in list(os.environ.keys()):
#    logger = telebot.logger
#    telebot.logger.setLevel(logging.INFO)
TOKEN = '1739533668:AAFABHGc2LmgWEzKCHF7uz-wFFtCWMSZF2I'
server = Flask(__name__)
@server.route('/' + tokenBot.TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://secret-fortress-01929.herokuapp.com/' + tokenBot.TOKEN)
    return "!", 200


if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
#else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.  
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    #bot.remove_webhook()
    #bot.polling(none_stop=True)