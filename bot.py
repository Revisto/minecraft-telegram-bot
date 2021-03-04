from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import setting
from models import Minecraft_Status

def players(update, context):
    update.message.reply_text(f'There are {Minecraft_Status().get_online_users_direct()} online players in minecraft.')

def main():
    updater = Updater(setting.telegram_access_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("players", players))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()