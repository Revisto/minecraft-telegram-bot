import requests
from config import Config

def offline_server_handler(func):
    def wrapper(self, *args, **kwargs):
        response_json = self._get_response_json()
        if response_json.get("online") is False:
            return {
                "status": "error",
                "message": "lol, the server's down."
            }
        return func(self, response_json, *args, **kwargs)
    return wrapper

class Minecraft_Status:
    def __init__(self):
        self.MINECRAFT_SERVER_ADDRESS = Config.MINECRAFT_SERVER_ADDRESS
    
    def _get_response_json(self):
        response = requests.get(f"https://api.mcstatus.io/v2/status/java/{self.MINECRAFT_SERVER_ADDRESS}")
        response_json = response.json()
        return response_json

    @offline_server_handler
    def get_online_users_count(self, response_json):
        return {
            "status": "success",
            "online_users_count": response_json.get("players", {}).get("online", 0)
        }

    @offline_server_handler
    def get_online_users_names(self, response_json):
        return {
            "status": "success",
            "online_users_names": response_json.get("players", {}).get("list", [])
        }