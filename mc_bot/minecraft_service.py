import requests
from config import Config

def error_handler(func):
    def wrapper(self, *args, **kwargs):
        response_json = self._get_response_json()
        if response_json.get("debug", {}).get("ping") is False:
            return {
                "status": "error",
                "message": response_json.get("debug", {}).get("error", "Unknown error")
            }
        return func(self, response_json, *args, **kwargs)
    return wrapper

class Minecraft_Status:
    def __init__(self):
        self.MINECRAFT_SERVER_ADDRESS = Config.MINECRAFT_SERVER_ADDRESS
    
    def _get_response_json(self):
        response = requests.get(f"https://api.mcsrvstat.us/3/{self.MINECRAFT_SERVER_ADDRESS}")
        response_json = response.json()
        return response_json

    @error_handler
    def get_online_users_count(self, response_json):
        return {
            "status": "success",
            "online_users_count": response_json.get("players", {}).get("online", 0)
        }

    @error_handler
    def get_online_users_names(self, response_json):
        return {
            "status": "success",
            "online_users_names": response_json.get("players", {}).get("list", [])
        }