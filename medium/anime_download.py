import os
import requests

# code start here
myidx = input('Insert anime ID from GoGoAnime url: ')
url = f"https://api.consumet.org/anime/gogoanime/info/{myidx}"
response = requests.get(url)
info = response.json()
# store into variables detailed info
title = info['title']
eps = info['totalEpisodes']
idname = info['id']
print(info['title'])
print("---------------")
print(info['description'])
print("Total Num of Episodes: "+str(info['totalEpisodes']))
singleEP = input(f'Episode to download (max {eps}): ')
print(f"Downloading {info['title']} episode {singleEP}")
serieName = myidx
idname= myidx
url = f"https://api.consumet.org/anime/gogoanime/watch/{idname}-episode-{singleEP}"
response = requests.get(url, params={"server": "vidstreaming"})
data = response.json()
link = data['sources'][0]['url']
filename2= f"{serieName}-{singleEP}.mp4"
f = f'ffmpeg -i {link} -c copy {filename2}'
# execute the command
with os.popen(f):
  pass