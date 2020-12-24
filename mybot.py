import telebot
from telebot import types

# токен-бота
bot = telebot.TeleBot('1497000529:AAEnvApitFftdq2FG0O0gvclMBS4sFFmxJk')


# если /help, /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здраствуйте "
                     + message.from_user.first_name
                     + ", здесь вы можете купить украшения ручной работы",
                     reply_markup=markup_menu)


markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_1 = types.KeyboardButton('Кольцо')
btn_2 = types.KeyboardButton('Ожерелье')
btn_3 = types.KeyboardButton('Браслеты')
btn_4 = types.KeyboardButton('Брошь')
markup_menu.add(btn_1, btn_2, btn_3, btn_4)


Pistols = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_p1 = types.KeyboardButton('Золото')
btn_p2 = types.KeyboardButton('Белое золота')
btn_p3 = types.KeyboardButton('Серебро')
btn_p4 = types.KeyboardButton('Позолота')
btn_p5 = types.KeyboardButton('В меню')
Pistols.add(btn_p1, btn_p2, btn_p3, btn_p4, btn_p5)


PP = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_pp1 = types.KeyboardButton('Из японского бисера')
btn_pp2 = types.KeyboardButton('Из нитки жемчуга')
btn_pp3 = types.KeyboardButton('Из кристаллов')
btn_pp4 = types.KeyboardButton('Из бронзовых бусин')
btn_pp5 = types.KeyboardButton('В меню')
PP.add(btn_pp1, btn_pp2, btn_pp3, btn_pp4, btn_pp5)


Rifles = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_r1 = types.KeyboardButton('Змейка')
btn_r2 = types.KeyboardButton('Манжета')
btn_r3 = types.KeyboardButton('Теннисный')
btn_r4 = types.KeyboardButton('Шармами')
btn_r5 = types.KeyboardButton('В меню')
Rifles.add(btn_r1, btn_r2, btn_r3, btn_r4, btn_r5)


Heavy = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_h1 = types.KeyboardButton('Ажурные')
btn_h2 = types.KeyboardButton('Эмалевые')
btn_h3 = types.KeyboardButton('Мозаичные')
btn_h4 = types.KeyboardButton('Камеи')
btn_h5 = types.KeyboardButton('В меню')
Heavy.add(btn_h1, btn_h2, btn_h3, btn_h4, btn_h5)

vmenyu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_naz5 = types.KeyboardButton('В меню')
vmenyu.add(btn_naz5)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "В меню":
        bot.reply_to(message, "Назад", reply_markup=markup_menu)
    if message.text == "Кольцо":
        bot.reply_to(message, "Выберите кольцо", reply_markup=Pistols)
    if message.text == "Ожерелье":
        bot.reply_to(message, "Выберите ожерелье", reply_markup=PP)
    if message.text == "Браслеты":
        bot.reply_to(message, "Выберите браслет", reply_markup=Rifles)
    if message.text == "Брошь":
        bot.reply_to(message, "Выберите брошь", reply_markup=Heavy)


bot.polling(none_stop=True)
