from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.markdown import Markdown
from rich.progress_bar import ProgressBar as PB
from rich.progress import track
from rich.status import Status as ST
from rich.progress import Progress, SpinnerColumn, TotalFileSizeColumn, TransferSpeedColumn, TimeElapsedColumn, TextColumn, BarColumn

#from tqdm.rich import trange, tqdm
from tqdm import trange, tqdm
from ffmpeg_progress_yield import FfmpegProgress
import time
import os
import requests
import datetime
import cv2  #to show the poster image thumbnail
"""
Using ANIME API this software can collect information about specific Anime Series
in GoGoAnime simply using the Anime id (easy detectable on gogoanime.ar. For 
example the serie info from https://gogoanime.gr/category/tomo-chan-wa-onnanoko 
has as ID "tomo-chan-wa-onnanoko" )
FFMPEG is required to be installed on your local computer
if not download the standalone executable from https://www.gyan.dev/ffmpeg/builds/
---
ANIME API
GitHub Repo: https://github.com/riimuru/gogoanime-api#how-to-get-started
API documentation
https://docs.consumet.org/rest-api/Anime/gogoanime/get-anime-episode-streaming-linkshttps://docs.consumet.org/rest-api/Anime/gogoanime/get-anime-episode-streaming-links
"""
# function to show the image thumbnail of the series
def show_my_image(image_ur):
    cap = cv2.VideoCapture(image_ur)  # Open the URL as video
    success, image = cap.read()  # Read the image as a video frame
    if success:
        cv2.imshow('image ', image)  # Display the image for testing
        cv2.waitKey()
    cap.release()

# Prepare console for display and Print operatons
console = Console()
console.clear(home=True)  #clear screen
# TITLE section
print(Panel("Download Anime Episode from [yellow]GoGoAnime", title="Anime Freak", title_align="right"))
# Accept input of the anime series
myidx = console.input("Insert Anime [i]ID[/i] :smiley: :")
# Query the Anime API for the anime serie
url = f"https://api.consumet.org/anime/gogoanime/info/{myidx}"
response = requests.get(url)
info = response.json()
# Generate info data from te json object and print them
title = info['title']
eps = info['totalEpisodes']
idname = info['id']
mymdtitle = Markdown(f"# {title}")
console.rule("[bold red]Anime Info")
console.print(mymdtitle)
print(info['description'])
mymaxepisode = Markdown(f"- Total Num of Episodes: {str(info['totalEpisodes'])}")
console.print(mymaxepisode)
console.print("[bold yellow]Verify your series looking at the Anime Poster")
show_my_image(info['image'])
# Select episode nuber for download section
console.rule("[bold blue]Download Episode")
singleEP = console.input(f'Episode Number you want to download? [bold red]1 - {eps}: ')
print(f"Downloading {info['title']} epidode {singleEP}")
# Ask for confirmation to proceed with download
is_rich_great = Confirm.ask("Do you confirm?")
if is_rich_great:
    serieName = myidx
    idname= myidx
    url = f"https://api.consumet.org/anime/gogoanime/watch/{idname}-episode-{singleEP}"
    response = requests.get(url, params={"server": "vidstreaming"})
    data = response.json()
    link = data['sources'][0]['url']
    filename2= f"{serieName}-{singleEP}.mp4"
    f = f'ffmpeg -nostats -loglevel 0 -i {link} -c copy {filename2}'
    start = datetime.datetime.now()
    console.print(f"Download Started at {start}",style="#F3CCFF")
    console.print(f"executing ffmpeg command",style="blink #af00ff")
 
    cmd = [
        "ffmpeg", "-i", link, "-c", "copy", filename2
    ]

    ff = FfmpegProgress(cmd)
    
    with Progress(
        SpinnerColumn(),
        TextColumn("Completed {task.completed:^3.0f} %", justify="left", style="white"),
        BarColumn(),) as progress:
        task_download = progress.add_task("[red]Download...", total=100)
        #progress.start()
        for progs in ff.run_command_with_progress():
            progress.update(task_download, completed = progs)
    
    end = datetime.datetime.now()
    console.print(f"Download Ended at {end}", style="bold red")
    elapsed = end - start
    print("---------------")
    console.print(f"completed in {elapsed}",style="bold #16FF00")
console.rule("[bold blue]Bye Bye")