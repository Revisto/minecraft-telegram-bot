from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import setting
from models import Minecraft_Status

def number_of_online_players(update, context):
    update.message.reply_text(f'There are {Minecraft_Status().get_online_users_count()} online players in minecraft.')

def names_of_online_players(update, context):
    update.message.reply_text(f"Online players' usernames in minecraft are \n{Minecraft_Status().get_online_users_names()}")

def main():
    updater = Updater(setting.telegram_access_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("numberplayers", number_of_online_players))
    dp.add_handler(CommandHandler("players", names_of_online_players))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
