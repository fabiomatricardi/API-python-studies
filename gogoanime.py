import os
import requests
import time
import datetime
# code start here
myidx = input('Insert anime ID from GoGoAnime url: ')
url = f"https://api.consumet.org/anime/gogoanime/info/{myidx}"
response = requests.get(url)
info = response.json()
title = info['title']
eps = info['totalEpisodes']
idname = info['id']
print(info['title'])
print("---------------")
print(info['description'])
print("Total Num of Episodes: "+str(info['totalEpisodes']))
singleEP = input(f'Episode to download (max {eps}): ')
print(f"Downloading {info['title']} epidode {singleEP}")
serieName = myidx
idname= myidx
url = f"https://api.consumet.org/anime/gogoanime/watch/{idname}-episode-{singleEP}"
response = requests.get(url, params={"server": "vidstreaming"})
data = response.json()
print(data)

"""link = data['sources'][0]['url']
filename2= f"{serieName}-{singleEP}.mp4"
f = f'ffmpeg -nostats -loglevel 0 -i {link} -c copy {filename2}'
start = datetime.datetime.now()
print(f"Started at {start}")
print(f"executing ffmpeg command")
with os.popen(f):
  pass
end = datetime.datetime.now()
print(f"Ended at {end}")
elapsed = end - start
print(f"completed in {elapsed}")"""