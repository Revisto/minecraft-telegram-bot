import dotenv
from os import getenv

dotenv.load_dotenv()

class Config:
        MINECRAFT_SERVER_IP = getenv("minecraft_server_ip")
        MINECRAFT_SERVER_PORT = getenv("minecraft_server_port")
        TELEGRAM_ACCESS_TOKEN = getenv("telegram_robot_access_token")
        MINECRAFT_SERVER_ADDRESS = f"{MINECRAFT_SERVER_IP}:{MINECRAFT_SERVER_PORT}"