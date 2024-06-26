from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from random import choice

from config import Config
from minecraft_service import Minecraft_Status
from file_service import FileManager, ImageFeatures


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text(
        "I'm Revisto's Minecraft Bot,\n/players - to get the names of online players\n/numberplayers - to get the number of online players\n\n",
    )

async def number_of_online_players(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the number of online players."""
    online_users_count = Minecraft_Status().get_online_users_count()
    if online_users_count.get("status") == "error":
        await update.message.reply_text(online_users_count.get("message"))
        return
    
    gifs = FileManager().get_gifs(online_users_count.get("online_users_count"))
    await update.message.reply_text(f'There are {online_users_count.get("online_users_count")} online players in minecraft.')
    if gifs != []: 
        respone_gif_path = choice(gifs)
        await update.message.reply_animation(open(respone_gif_path, "rb"))

async def names_of_online_players(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the names of online players."""
    online_users_names = Minecraft_Status().get_online_users_names()
    if online_users_names.get("status") == "error":
        await update.message.reply_text(online_users_names.get("message"))
        return
    
    if online_users_names.get("online_users_names") == []:
        await update.message.reply_text("No online players.")
        return
    
    names_list = [user["name"] for user in online_users_names.get("online_users_names", [])]
    names = "\n".join([user["name"] for user in online_users_names.get("online_users_names", [])])
    await update.message.reply_text(f"Online players' usernames in minecraft are \n{names}")
    users_pictures = ImageFeatures.generate_users_pictures(names_list)
    if users_pictures is not None:
        await update.message.reply_photo(users_pictures)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(Config.TELEGRAM_ACCESS_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", start))
    application.add_handler(CommandHandler("numberplayers", number_of_online_players))
    application.add_handler(CommandHandler("players", names_of_online_players))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()