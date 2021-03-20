from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from validator_collection import is_not_empty

import setting
from models import Files, Minecraft_Status


def number_of_online_players(update, context):
    online_users_count = Minecraft_Status().get_online_users_count()
    path_of_gifs_related_to_online_users_count = Files().get_path_directory_of_videos(online_users_count)
    gifs_related_to_online_users_count = Files().get_files_names_path_in_directory(path_of_gifs_related_to_online_users_count)
    update.message.reply_text(f'There are {online_users_count} online players in minecraft.')
    if is_not_empty(gifs_related_to_online_users_count):
        respone_gif_path = Files().random_choice_from_list(gifs_related_to_online_users_count)
        update.message.reply_animation(open(respone_gif_path, "rb"))
        

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
