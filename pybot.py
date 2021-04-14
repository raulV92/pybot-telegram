
import os
from pathlib import Path

import telegram
#from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters

import pyfirmata

# funciones Bot:


def valida_usuario(handler_func):
    def wrapper_func(update, context):
        if update.effective_chat.id in list(usuarios.keys()):
            return handler_func(update, context)

    return wrapper_func
##############
# Funciones para menu de botones:


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    elif footer_buttons:
        menu.append(footer_buttons)
    return menu


def build_buttons(elements, type_: str):
    button_list = []
    for each in elements:
        button_list.append(
            InlineKeyboardButton(each, callback_data=type_ + str(each)))

    #breakpoint()
    # reply_markup
    return InlineKeyboardMarkup(build_menu(button_list, n_cols=2))


######

@valida_usuario
def greet_user(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="hola " + update._effective_user.first_name +
                             comandos)
    #breakpoint()


@valida_usuario
def callback_func(update, context):
    #print('entra callback')
    query = update.callback_query
    query.answer()
    #print(query.data)
    tec_id = query.from_user.id
    if query.data[0:2] == 't_':
        tecnicos[tec_id].cambiar_a_tienda(query.data[2:], context.bot)
    elif query.data[0:2] == 'i_':
        tecnicos[tec_id].mandar_foto(query.data[2:], context.bot)



def init_bot(bot_token):
    bot = telegram.Bot(token=bot_token)
    print(bot.get_me())
    ## commands
    start_handler = CommandHandler('start', greet_user)
    dispatcher.add_handler(start_handler)  # 1

    ## Raw text handler_func
    message_handler = MessageHandler(Filters.text & (~Filters.command),
                                     message_validation)

    
    # Callback
    callback_handler = CallbackQueryHandler(callback_func)
    dispatcher.add_handler(callback_handler)  # 7

    updater.start_polling()




if __name__=='__main__':
	with open('token.txt', 'r') as t:
		token=t.readline()
	print(token)
	breakpoint()
	init_bot(token)




