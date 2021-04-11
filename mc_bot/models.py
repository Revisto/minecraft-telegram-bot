from mcstatus import MinecraftServer
from os import listdir, remove, path
from os.path import isfile, join
import os.path
from random import choice
import requests
import setting
from PIL import Image
from validator_collection import is_not_empty

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

    def get_online_users_list_names(self):
        online_users_names_list = self.mc_server_query.players.names
        return online_users_names_list

class Files:
    def does_it_exist(self, file_path):
        return path.exists(file_path)

    def get_files_names_path_in_directory(self, directory_path="./"):
        if not directory_path.endswith("/"):
            directory_path = directory_path+"/"
        if not Files().does_it_exist(directory_path):
            return []
        return [directory_path+f for f in listdir(directory_path) if isfile(join(directory_path, f))]

    def get_path_directory_of_videos(self, number):
        return f"./videos/{number}"

    def random_choice_from_list(self, the_list):
        return choice(the_list)

    def remove_file(self, path):
        remove(path)
class Features:

    def merge_images_side_by_side(self, image_paths, resample=Image.BICUBIC):
        im_list = []
        for path in image_paths:
            im_list.append(Image.open(path))

        min_height = min(im.height for im in im_list)
        im_list_resize = [im.resize((int(im.width * min_height / im.height), min_height),resample=resample)
                        for im in im_list]
        total_width = sum(im.width for im in im_list_resize)
        dst = Image.new('RGB', (total_width, min_height))
        pos_x = 0
        for im in im_list_resize:
            dst.paste(im, (pos_x, 0))
            pos_x += im.width
        dst.save('.temp.jpg')
        image_bytes = open(".temp.jpg", "rb")
        Files().remove_file(".temp.jpg")
        return image_bytes

    def send_picture_of_online_users(self, online_users, update):
        random_pictures_of_online_users = []
        for user in online_users:
            user_pictures_path = f"users_pictures/{user}"
            users_pictures = Files().get_files_names_path_in_directory(user_pictures_path)
            if not is_not_empty(users_pictures):
                continue
            radnom_user_pic = Files().random_choice_from_list(users_pictures)
            random_pictures_of_online_users.append(radnom_user_pic)
        if is_not_empty(random_pictures_of_online_users):
            image_bytes = Features().merge_images_side_by_side(random_pictures_of_online_users)
            update.message.reply_photo(image_bytes)
            