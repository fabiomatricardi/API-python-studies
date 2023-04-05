from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.markdown import Markdown
import os
import requests
import datetime
"""
Using ANIME API this software can collect information about specific Anime Series
in GoGoAnime simply using the Anime id (easy detectable on gogoanime.ar. For 
example the serie info from https://gogoanime.gr/category/tomo-chan-wa-onnanoko 
has as ID "tomo-chan-wa-onnanoko" )
ANIME API
GitHub Repo
https://github.com/riimuru/gogoanime-api#how-to-get-started

API documentation
https://docs.consumet.org/rest-api/Anime/gogoanime/get-anime-episode-streaming-linkshttps://docs.consumet.org/rest-api/Anime/gogoanime/get-anime-episode-streaming-links
"""
console = Console()
console.clear(home=True)
print(Panel("Download Anime Episode from [yellow]GoGoAnime", title="Anime Freak", title_align="right"))
#print(Panel("Download Anime Episode from [yellow]GoGoAnime", title="Anime Freak", subtitle="Thank you"))
#console.print([1, 2, 3])
#console.print("[blue underline]Looks like a link")
#console.print(locals())
###  console.rule("[bold red]Chapter 2")
#console.print("FOO", style="white on blue")
"""with console.status("Monkeying around...", spinner="monkey"):
    console.print("What's your name?")"""

myidx = console.input("Insert Anime [i]ID[/i] :smiley: :")
#myidx = input('Take it from GoGoAnime url: ')
url = f"https://api.consumet.org/anime/gogoanime/info/{myidx}"
response = requests.get(url)
info = response.json()
title = info['title']
eps = info['totalEpisodes']
idname = info['id']
mymdtitle = Markdown(f"# {title}")
console.rule("[bold red]Anime Info")
console.print(mymdtitle)
#print("---------------")
print(info['description'])
mymaxepisode = Markdown(f"- Total Num of Episodes: {str(info['totalEpisodes'])}")
console.print(mymaxepisode)
console.rule("[bold blue]Download Episode")
singleEP = console.input(f'Episode Number you want to download? [bold red]1 - {eps}: ')
print(f"Downloading {info['title']} epidode {singleEP}")
is_rich_great = Confirm.ask("Do you confirm?")
if is_rich_great:
    serieName = myidx
    idname= myidx
    url = f"https://api.consumet.org/anime/gogoanime/watch/{idname}-episode-{singleEP}"
    response = requests.get(url, params={"server": "vidstreaming"})
    data = response.json()
    link = data['sources'][0]['url']
    #filename=f"/content/{title}_ep_{singleEP}.mp4"
    #!~/.local/bin/downloadm3u8 -o "$filename" "$link"
    #print(link)
    filename2= f"{serieName}-{singleEP}.mp4"
    f = f'ffmpeg -nostats -loglevel 0 -i {link} -c copy {filename2}'
    start = datetime.datetime.now()
    console.print(f"Download Started at {start}",style="#F3CCFF")
    console.print(f"executing ffmpeg command",style="blink #af00ff")
    with os.popen(f):
        pass
    end = datetime.datetime.now()
    console.print(f"Download Ended at {end}", style="bold red")
    elapsed = end - start
    print("---------------")
    console.print(f"completed in {elapsed}",style="bold #16FF00")
console.rule("[bold blue]Bye Bye")
"""
console.print(f"Your name is {url}",style="frame blink bold yellow")

console.print("  ")
console.print("Danger, Will Robinson!", style="frame blink bold yellow")
console.print("  ")
"""
"""
print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))


from rich.prompt import Prompt
name = Prompt.ask("Enter your name", default="Paul Atreides")

from rich.prompt import Confirm
is_rich_great = Confirm.ask("Do you like rich?")
assert is_rich_great"""

"""import random
import time

from rich.live import Live
from rich.table import Table


def generate_table() -> Table:
    '''Make a new table.'''
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(
            f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
        )
    return table


with Live(generate_table(), refresh_per_second=4) as live:
    for _ in range(40):
        time.sleep(0.4)
        live.update(generate_table())"""