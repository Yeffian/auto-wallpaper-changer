# auto-wallpaper-changer

Automatically changes your computer's wallpaper using your own pictures.

## Setup

Clone the repository, and place the script in the root of your folder with all your pictures. The pictures must be organised into subfolders, so if you don't have it organised in subfolders just throw everything into one folder, and place the script in the parent folder. 

If you want to change wallpapers on system startup, first place the ChangeWallpaper.bat script beside your python file. Then open up your Windows Startup folder (Press Win+R, "shell:startup", press enter) and create a shortcut to the batch script inside the startup folder. It may not be instant based on what other startup applications you have, but it should change randomly within a few seconds of booting.