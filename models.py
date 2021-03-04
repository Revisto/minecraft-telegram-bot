from mcstatus import MinecraftServer
import requests
import setting

class Minecraft_Status:
    def get_online_users(self):
        status_server = (requests.get(f"https://api.mcsrvstat.us/2/{setting.minecraft_server_address}").json())
        online_players = status_server["players"]["online"]
        return online_players

    def get_online_users_direct(self):
        server = MinecraftServer.lookup(f"{setting.minecraft_server_address}")
        status = server.status()
        return status.players.online