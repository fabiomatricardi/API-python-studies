from rich.console import Group
from rich.panel import Panel
from rich.live import Live
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)
#from tqdm.rich import trange, tqdm
from rich.progress import track
from ffmpeg_progress_yield import FfmpegProgress
import time
import os
import requests
import datetime

"""
anime serie
youjo-shenki
"""

# progress bar for current app (progress in steps)
app_steps_progress = Progress(
    TextColumn(
        "[bold blue]Downloading video: {task.percentage:.0f}%"
    ),
    BarColumn(),
    TextColumn("({task.completed} of {task.total} steps done)"),
)

link = "https://tc-036.agucdn.com/1ab5d45273a9183bebb58eb74d5722d8ea6384f350caf008f08cf018f1f0566d0cb82a2a799830d1af97cd3f4b6a9a81ef3aed2fb783292b1abcf1b8560a1d1aa308008b88420298522a9f761e5aa1024fbe74e5aa853cfc933cd1219327d1232e91847a185021b184c027f97ae732b3708ee6beb80ba5db6628ced43f1196fe/545126644886463d5c462b394d5fa893/ep.1.1677827924.360.m3u8"
filename2= f"youjo-shenki_ep1.mp4"
cmd = ["ffmpeg", "-i", link, "-c", "copy", filename2]
ff = FfmpegProgress(cmd)

#task1 =app_steps_progress.add_task("Video download...", total=100)
start = datetime.datetime.now()
with app_steps_progress:
    task1 = app_steps_progress.add_task("[red]Downloading...", name="down",total=100)
    for steps in ff.run_command_with_progress():
        app_steps_progress.update(task1)


end = datetime.datetime.now()
print(f"Download started at {start}")
print(f"Download Ended at {end}")
elapsed = end - start
print("---------------")
print(f"completed in {elapsed}")