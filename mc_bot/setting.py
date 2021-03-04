import dotenv
from os import getenv

dotenv.load_dotenv()

minecraft_server_ip = getenv("minecraft_server_ip")
minecraft_server_port = getenv("minecraft_server_port")
telegram_access_token = getenv("telegram_robot_access_token")
minecraft_server_address = f"{minecraft_server_ip}:{minecraft_server_port}"