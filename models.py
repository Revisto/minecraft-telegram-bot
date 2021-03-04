from mcstatus import MinecraftServer
import requests


class Minecraft_Status:
    def get_online_users(self):
        status_server = (requests.get("https://api.mcsrvstat.us/2/185.110.190.30:25566").json())
        online_players = status_server["players"]["online"]
        return online_players

    def get_online_users_direct(self):
        server = MinecraftServer.lookup("185.110.190.30:25566")
        status = server.status()
        return status.players.online