from pytube import YouTube as yt
from pytube.cli import on_progress
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.markdown import Markdown
from rich.status import Status
import os
import datetime
import re
import urllib.request
import ssl
from os import path
import requests

ssl._create_default_https_context = ssl._create_unverified_context


def normalize_name(mystring): 
    # initialising string
    ini_string = mystring
    # printing initial string
    #print ("initial string : ", ini_string)
    getVals = list([val for val in ini_string
                if val.isalpha() or val.isnumeric()])
    result = "".join(getVals)
    # printing final string
    #print ("final string", result)
    return result

def normalize_name_space(mystring): 
    a = mystring
    for k in a.split("\n"):
        #print(re.sub(r"[^a-zA-Z0-9]+", ' ', k))
        # Or:
        final = " ".join(re.findall(r"[a-zA-Z0-9]+", k))
        # print(final)
        final = final.replace(' ','_')
    return final


console = Console(width=80, height=25)
console.clear(home=True)  #clear screen

#link = "https://www.youtube.com/watch?v=PLkkGii3ZoI"
#link = console.input('Youtube video url: ')
console.rule(' # ',style='red')
link = Prompt.ask('Enter youtube video url: ')
console.rule(' # ',style='blue')
console.print('Fetching video data...', style='yellow blink')
with console.status("Monkeying around...", spinner="monkey"):
    video = yt(link, on_progress_callback=on_progress)
#stream = video.streams.get_by_itag(18)
title = Markdown(f'# {video.title}')
console.print(title)
console.print(f'Created by : {video.author}')
video_length = str(datetime.timedelta(seconds=video.length))
console.print(f'Video duration: {video_length}')
console.rule('description')
console.print(video.description)
console.rule('details')
console.print(f'filename: {normalize_name_space(video.title)}.mp4')
filename = f'./{normalize_name_space(video.title)}.mp4'
downladvideo = Confirm.ask('Do you want to downlad the video? ')
if downladvideo:
    stream = video.streams.filter(res='720p', progressive=True, file_extension='mp4').last()
    stream.download(filename=filename)
    console.print('Download completed', style='bold green')
console.rule('Bye Bye')
