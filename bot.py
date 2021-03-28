import telebot;
bot = telebot.TeleBot('1739533668:AAFABHGc2LmgWEzKCHF7uz-wFFtCWMSZF2I');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
         if message.text == "Привет":
                  bot.send_message(message.from_user.id, "Привет, вот список 10 достопремечательностей Дубая, которые ты обязан посетить - \n 1.Бурдж-Халифа \n 2. фонтаны дубая \n 3.Дубайский торговый центр \n 4. Dubai Miracle Garden \n 5.Global Village \n 6.Dubai Frame \n 7.Аквапарк Аквавенчер \n 8.La Mer \n 9.Бурдж аль араб \n 10.Комплекс ski dubai \n \nНапишите цифру, чтобы узнать больше")
         elif message.text == "/help":
                  bot.send_message(message.from_user.id, "Напиши привет")
         elif message.text == "1":
                  bot.send_message(message.from_user.id, "Бурдж-Халифа - сверхвысотный небоскрёб высотой 828 метров в Дубае (ОАЭ), самое высокое и самое многоэтажное здание, самое высокое сооружение, единственный 828-метровый и 163-этажный небоскрёб в мире. Уступчатая форма здания напоминает сталагмит")
         elif message.text == "2":
                  bot.send_message(message.from_user.id, "Фонтан Дубай — музыкальный фонтан, расположенный в искусственном озере площадью свыше 12 га рядом с небоскрёбом Бурдж-Халифа в центре Дубая")
         elif message.text == "3":
                  bot.send_message(message.from_user.id, "The Dubai Mall (Дубай Молл) — самый крупный торгово-развлекательный центр в мире, расположенный в даунтауне Дубай. Общая площадь центра составляет более 1,2 млн м²")
         elif message.text == "4":
                  bot.send_message(message.from_user.id, "Dubai Miracle Garden - Красивый сад с инсталяциями с цветами")
         elif message.text == "5":
                  bot.send_message(message.from_user.id, "Global Village - комплекс с кафе, рынками")
         elif message.text == "6":
                  bot.send_message(message.from_user.id, "Dubai frame - самая большая в мире рамка")
         elif message.text == "7":
                  bot.send_message(message.from_user.id, "Аквапарк аквавенчер - большой аквапарк на острове Пальм Джумейра")
         elif message.text == "8":
                  bot.send_message(message.from_user.id, "La mer - пляж в районе Джумейра")
         elif message.text == "9":
                  bot.send_message(message.from_user.id, "Бурдж аль-Араб — отель в форме паруса, один из самых роскошных в мире")
         elif message.text == "10":
                  bot.send_message(message.from_user.id, "Ski dubai - уникальный горнолыжный комплекс который находится в Молле Эмирейтс")
         else:
                  bot.send_message(message.from_user.id, "Напиши /help")
bot.polling(none_stop=True, interval=0)
