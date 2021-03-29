# Подключаем Telegram API 
import telebot

# Подключаем библиотеку для создания кнопок
from telebot import types
 
token = '1739533668:AAFABHGc2LmgWEzKCHF7uz-wFFtCWMSZF2I'
# Объявляем бота
bot = telebot.TeleBot(token)

def create_keyboard():
    # Создаём тип для кнопок
    keyboard = types.InlineKeyboardMarkup()
    # Создаём кнопку 
    btn1 = types.InlineKeyboardButton(text="1.Бурж-Халифа", callback_data="1")
    # Создаём кнопку 
    btn2 = types.InlineKeyboardButton(text="2.Фонтаны Дубая", callback_data="2")
    # Создаём кнопку 
    btn3 = types.InlineKeyboardButton(text="3.Дубай Молл", callback_data="3")
    # Создаём кнопку 
    btn4 = types.InlineKeyboardButton(text="4.Сад Чудес", callback_data="4")
    # Создаём кнопку 
    btn5 = types.InlineKeyboardButton(text="5.Global Village", callback_data="5")
    # Создаём кнопку 
    btn6 = types.InlineKeyboardButton(text="6.Dubai Frame", callback_data="6")
    # Создаём кнопку 
    btn7 = types.InlineKeyboardButton(text="7.Aquaventure", callback_data="7")
    # Создаём кнопку 
    btn8 = types.InlineKeyboardButton(text="8.La Mer", callback_data="8")
    # Создаём кнопку 
    btn9 = types.InlineKeyboardButton(text="9.Бурж Аль-Араб", callback_data="9")
    # Создаём кнопку 
    btn10 = types.InlineKeyboardButton(text="10.Ski Dubai", callback_data="10")
    # Добавляем кнопку в специальный список
    keyboard.add(btn1)
    # Добавляем кнопку в специальный список
    keyboard.add(btn2)
    # Добавляем кнопку в специальный список
    keyboard.add(btn3)
    # Добавляем кнопку в специальный список
    keyboard.add(btn4)
    # Добавляем кнопку в специальный список
    keyboard.add(btn5)
    # Добавляем кнопку в специальный список
    keyboard.add(btn6)
    # Добавляем кнопку в специальный список
    keyboard.add(btn7)
    # Добавляем кнопку в специальный список
    keyboard.add(btn8)
    # Добавляем кнопку в специальный список
    keyboard.add(btn9)
    # Добавляем кнопку в специальный список
    keyboard.add(btn10)
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
if __name__ == '__main__':
    bot.polling(none_stop=True)
