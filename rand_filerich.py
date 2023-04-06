import time
import random
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)

def process(chunks):
    for chunk in chunks:
        time.sleep(0.1)
        yield chunk

chunks = [random.randint(1,20) for _ in range(100)]

progress_columns = (
    SpinnerColumn(),
    "[progress.description]{task.description}",
    BarColumn(),
    TaskProgressColumn(),
    "Elapsed:",
    TimeElapsedColumn(),
    "Remaining:",
    TimeRemainingColumn(),
)

with Progress(*progress_columns) as progress_bar:
    task = progress_bar.add_task("[blue]Downloading...", total=sum(chunks))
    for chunk in process(chunks):
        progress_bar.update(task, advance=chunk)