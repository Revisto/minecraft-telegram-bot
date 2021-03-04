from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job
import setting
from models import Minecraft_Status
from time import sleep
import threading

def number_of_online_players(update, context):
    update.message.reply_text(f'There are {Minecraft_Status().get_online_users_count()} online players in minecraft.')

def names_of_online_players(update, context):
    updater.message.reply_text(f"Online players' usernames in minecraft are {Minecraft_Status().get_online_users_names()}")

def entry_and_exits_status(update, context):
    for i in range (50):
        sleep(10)
        context.bot.sendMessage(chat_id='107731089', text='bot_welcome')


def main():
    updater = Updater(setting.telegram_access_token, use_context=True)
    dp = updater.dispatcher
    
    def entry_and_exits_status():
        for i in range (50):
            sleep(10)
            updater.bot.sendMessage(chat_id='107731089', text='bot_welcome')

    # loop_for_entry_and_exits_status = 
    threading.Thread(target=entry_and_exits_status).start()

    dp.add_handler(CommandHandler("numberPlayers", number_of_online_players))
    dp.add_handler(CommandHandler("Players", names_of_online_players))
    dp.add_handler(CommandHandler("startTheMagic", entry_and_exits_status))



    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()