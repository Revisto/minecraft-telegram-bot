import os
import random
from PIL import Image
import io

class FileManager:
    def __init__(self):
        self.videos_base_path = "./videos"
        self.users_pictures_base_path = "./users_pictures"

    def get_gifs(self, directory_number):
        directory_path = os.path.join(self.videos_base_path, str(directory_number))
        if not os.path.exists(directory_path):
            return []
        return [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith('.gif')]

    def get_user_pictures(self, username):
        username = username.lower()
        if not os.path.exists(self.users_pictures_base_path):
            return []  # Return an empty list if the base path doesn't exist

        directories = next(os.walk(self.users_pictures_base_path), (None, [], None))[1]
        user_directory = None
        for directory in directories:
            if directory.lower() == username:
                user_directory = directory
                break
        if user_directory is None:
            return []  # Return an empty list if the user's directory doesn't exist

        user_directory_path = os.path.join(self.users_pictures_base_path, user_directory)
        pictures = [os.path.join(user_directory_path, file) for file in os.listdir(user_directory_path) if file.endswith('.jpg')]
        return pictures

class ImageFeatures:
    @staticmethod
    def generate_users_pictures(online_users):
        image_paths = []
        for username in online_users:
            username_pictures = FileManager().get_user_pictures(username)
            if username_pictures != []:
                image_paths.append(random.choice(username_pictures))
        
        if image_paths != []:
            return ImageFeatures.merge_images_side_by_side(image_paths)
        return None

    @staticmethod
    def merge_images_side_by_side(image_paths, resample=Image.BICUBIC):
        images = [Image.open(path) for path in image_paths]
        min_height = min(img.height for img in images)
        resized_images = [img.resize((int(img.width * min_height / img.height), min_height), resample=resample) for img in images]
        total_width = sum(img.width for img in resized_images)
        combined_image = Image.new('RGB', (total_width, min_height))
        current_position = 0
        for img in resized_images:
            combined_image.paste(img, (current_position, 0))
            current_position += img.width
        image_bytes_io = io.BytesIO()
        combined_image.save(image_bytes_io, format='JPEG')
        image_bytes_io.seek(0)
        return image_bytes_io.getvalue()