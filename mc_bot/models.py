from mcstatus import MinecraftServer
from os import listdir
from os.path import isfile, join
import requests
import setting

class Minecraft_Status:
    def __init__(self):
        mc_server_lookup = MinecraftServer.lookup(f"{setting.minecraft_server_address}")
        mc_server_status = mc_server_lookup.status()
        mc_server_query = mc_server_lookup.query()
        self.mc_server_status = mc_server_status
        self.mc_server_query = mc_server_query

    def get_online_users_count_via_api(self):
        status_server = (requests.get(f"https://api.mcsrvstat.us/2/{setting.minecraft_server_address}").json())
        online_players = status_server["players"]["online"]
        return online_players

    def get_online_users_count(self):
        return self.mc_server_status.players.online

    def get_online_users_names(self):
        online_users_names_list = self.mc_server_query.players.names
        online_users_names = ", \n".join(online_users_names_list)
        return online_users_names if online_users_names != "" else None


class Files:
    def get_files_names_path_in_directory(self, path="./"):
        return [f for f in listdir(path) if isfile(join(path, f))]

    def get_path_directory_of_videos(self, number):
        return f"./videos/{number}"