# You-py!
# Made by Alexander Betancourt
# © 10/28/2021 12:00PM
# Descripton: Python terminal based youtube downloader program!

# Possible: future Features include.
# MP3 and WAV support
# Multple link support

# Imports
import json
from datetime import datetime
import os
from pytube import YouTube

class video:
    '''Contains all video functions in a single class'''
    format = ""
    path = ""
    link = ""
    def __init__(self, format):
        '''intalizes with the format, path, and link.
        path: checks if path exists 
        link: checks link and sets'''
        if paths:
            i = 1
            for pat in paths:
                print(f'{i}: {pat}')
                i += 1
        else:
            # ERROR 1 is a no path error!
            print("ERROR 1")
            print("Path error no default path!")
            pause_feature()
            return
        path_num = int(input("Please pick a path number: "))
        path_num = path_num - 1
        path = paths[path_num]
        #save_path = Paths[path]
        try:
            os.path.exists(path)
        except Exception as a:
            print("ERROR 2")
            print(f"Path: {path} does not exist!")
        link = input("Please insert a link: ")
        try:
            self.yt = YouTube(link)
        except Exception as b:
            print("ERROR 3")
            print(f"link: {link} does not exist!")
        self.format = format
        self.path = path
        self.link = link
        self.download()
    
    def collect_data(self):
        '''Colects data from the API wrapper'''
        data = []
        data.append("Title:")
        data.append(self.yt.title)
        data.append("View count:")
        data.append(self.yt.views)
        data.append("URL:")
        data.append(self.link)
        data.append("Format:")
        data.append(self.format)
        data.append("Timestamp:")
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        data.append(dt_string)
        data.append("Path: ")
        data.append(self.path)
        return data

    def download(self):
        '''Downloads the video using the class atrbutes'''
        print(f"Retreving: {self.yt.title}")
        print(f'Downloading an {self.format}, from {self.link} to {self.path}: ')
        try:
            self.yt.streams.filter(
                progressive=True, file_extension=self.format).order_by(
                    'resolution')[-1].download(self.path)
        except Exception as c:
            # ERROR 4: pyTube servers dead
            print("ERROR 4")
            print(c)
            return
        print(f"DONE! Downloading {self.yt.title} in {self.format}")
        print(f"from {self.link} to {self.path}")
        downloads.append(self.collect_data())
        saved['downloads'] = downloads
        with open(path_to_json + file_name, "w") as json_file:
            json.dump(saved, json_file, indent=4)
        pause_feature()


# Declarations:
paths = []
downloads = []
path_to_json = './youtube_videos/save_data/'
saved = {}
line = "+=========================================+"
# Line shorthand to make lines in terminal

# Pause for people to read the text!


def pause_feature():
    '''Pauses the menu using input.'''
    input("Press Enter to countinue.... ")

# Cleans input by getting rid of periods and spaces


def clean_input(user_input):
    '''Cleans the input by getting,
    rid of any undesired characters.'''
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
        if paths:
            i = 1
            for pat in paths:
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
            paths.append(user_path)
            saved['paths'] = paths
            with open(path_to_json + file_name, "w") as json_file:
                json.dump(saved, json_file, indent=4)
            pause_feature()


def check_input(filtered_input):
    
    # Input Checker! I wish Python, had Switch statements!
    if(filtered_input == "DOWNLOAD" or filtered_input == "D"):
        video('mp4')
    # elif(filtered_input == "MP3"):
    #     downloadUI('mp3')
    elif(filtered_input == "RECENT" or filtered_input == "R"):
        recentDownloads()
    elif(filtered_input == "EXIT" or filtered_input == "E"):
        return True
    elif(filtered_input == "PATH" or filtered_input == "P"):
        print("Type 'add' to add a path\nType 'see' to see all saved paths: ")
        user_input = input(": ").upper()
        pathMenu(clean_input(user_input))
    elif(filtered_input == "CLS" or filtered_input == "CLEAR" or filtered_input == "C"):
        os.system('cls||clear')
    else:
        print("Invaild input!")


def recentDownloads():
    if downloads:
        os.system('cls||clear')
        i = 1
        for download in downloads:
            print(f'{line}')
            print(f'{i}.')
            i += 1
            for x in range(0,12,2):
                print(f'{download[x]} {download[x+1]}')
            pause_feature()
            os.system('cls||clear')
    else:
        print("No recent downloads")
        pause_feature()



for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
  with open(path_to_json + file_name, "r") as json_file:
    saved = json.load(json_file)
paths = saved['paths']
downloads = saved['downloads']

while(True):
    user_input = mainMenu()
    if(check_input(user_input)):
        break
