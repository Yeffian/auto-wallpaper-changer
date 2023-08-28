from PIL import Image
import os
import random
import ctypes

PICTURES_DIR = os.getcwd()
CATEGORIES = list(filter(os.path.isdir, os.listdir(os.curdir)))

screen_size = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)


def select_picture():
    category = random.choice(CATEGORIES)
    pictures = PICTURES_DIR + "/" + category
    picture = random.choice(os.listdir(pictures))
    return os.path.abspath(category + "\\" + picture)



def main():
    picture = select_picture()

    image = Image.open(picture)
    wallpaper_img = image.resize(screen_size)
    wallpaper_img.convert('RGB')
    wallpaper_img.save('./wallpaper.png')

    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd() + '.\\wallpaper.png', 0)


main()