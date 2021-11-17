# You-py!
# Made by Alexander Betancourt
# © 10/28/2021 12:00PM
# Descripton: Python terminal based youtube downloader program!

# Possible: future Features include.
# MP3 and WAV support
# Multple link support
# History Downloaded to files

# Imports
import json
import os
from pytube import YouTube

# Declarations:
Downloads = []
# Downloads is a list, that keeps the files that you recently download
Paths = ['../youpy/youtube videos']
# Default Path included!

line = "+=========================================+"
# Line shorthand to make lines in terminal

# Pause for people to read the text!


def pause_feature():
    input("Press Enter to countinue.... ")

# Cleans input by getting rid of periods and spaces


def clean_input(user_input):
    str(user_input)
    if(user_input[0] == '.'):
        ch = '.'
        user_input = user_input.lstrip(ch)
    if(user_input[0] == ' '):
        ch = ' '
        user_input = user_input.lstrip(ch)
    return user_input

# Main menu UI


def mainMenu():
    # Returns Cleanded String with filetype
    os.system('cls||clear')
    print(f'{line}')
    print("           Welcome to you-py!")
    print("Type 'Download' if you want to download a video:")
    print("Type 'Exit' to stop the program:")
    print("Type 'Recent' to get recent downloads:")
    print("Type 'Path' to edit and view paths:")
    user_input = input(": ").upper()
    return clean_input(user_input)

# PATH menu UI


def pathMenu(cleaned_input):
    # Plus addtional input checking
    if(cleaned_input == "SEE"):
        if Paths:
            i = 1
            for pat in Paths:
                print(f'{i}: {pat}')
                i += 1
            pause_feature()
        else:
            # ERROR 1 is a no path error!
            print("ERROR 1")
            pause_feature()
    elif (cleaned_input == "ADD"):
        print("Type 'return' to go back to main menu)")
        user_path = input("What file path do you want to use?: ")
        print(clean_input(user_path))
        if (clean_input(user_path)) == "RETURN":
            print("Returning back to main menu!~")
            pause_feature()
        elif not os.path.exists(user_path):
            print("Path of the file is Invalid")
            pause_feature()
        else:
            print("Path exists~!")
            Paths.append(user_path)
            pause_feature()


def check_input(filtered_input):
    # Input Checker! I wish Python, had Switch statements!
    if(filtered_input == "DOWNLOAD"):
        downloadUI('mp4')
    elif(filtered_input == "MP3"):
        downloadUI('mp3')
    elif(filtered_input == "RECENT"):
        recentDownloads()
    elif(filtered_input == "EXIT"):
        return True
    elif(filtered_input == "PATH"):
        print("Type 'add' to add a path\nType 'see' to see all saved paths: ")
        user_input = input(": ").upper()
        pathMenu(clean_input(user_input))
    elif(filtered_input == "CLS" or filtered_input == "CLEAR"):
        os.system('cls||clear')
    else:
        print("Invaild input!")


def recentDownloads():
    if Downloads:
        os.system('cls||clear')
        print(f'{line}')
        i = 1
        for download in Downloads:
            print(f'{i}. {download}')
            i += 1
        pause_feature()
    else:
        print("No recent downloads")
        pause_feature()


def downloadUI(form):
    link = input("Please insert a link: ")
    if Paths:
        i = 1
        for pat in Paths:
            print(f'{i}: {pat}')
            i += 1
    else:
        # ERROR 1 is a no path error!
        print("ERROR 1")
        pause_feature()
        return
    path = int(input("Please pick a path number: "))
    path = path - 1
    save_path = Paths[path]
    download(link, form, save_path)


def download(link, format, save_path):
    print(f'Downloading an {format}, from {link} to {save_path}: ')
    print(format)
    try:
        yt = YouTube(link)
    except YouTube.DoesNotExist:
        # Video doesn't exist
        print("ERROR 2")
        return
    try:
        yt.streams.filter(
            progressive=True, file_extension=format).order_by(
                'resolution')[-1].download(save_path)
    except YouTube.DoesNotExist:
        # ERROR 4: pyTube servers dead
        print("ERROR 4")
    print(f"DONE! Downloading an {format}, from {link} to {save_path}")
    Downloads.append(link)
    pause_feature()


while(True):
    user_input = mainMenu()
    if(check_input(user_input)):
        break
