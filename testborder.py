from rich import box
from rich.console import Console
from rich.table import Table
from rich.bar import Bar
from rich.panel import Panel

table = Table(title="Star Wars Movies", box=box.MINIMAL_DOUBLE_HEAD)
console = Console()
console.print(table)
mybox = Bar(30.0,0.0,12.0)
mybox2 = Bar(30.0,0.0,17.8, color="#F3CCFF", bgcolor="#af00ff")
mypanel = Panel("Download Anime Episode from [yellow]GoGoAnime", title="Anime Freak",box=box.DOUBLE)
mypanel2 = Panel("Download Anime Episode from [yellow]GoGoAnime", title="Anime Freak",box=box.HORIZONTALS)
console.print(mybox)
console.print(mypanel)
console.print(mybox2)
console.rule("aspetta")
console.print(mypanel2)

MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

## This is a H2

### This is H3

> this is quote

1. This is a list item
2. This is another list item
"""
from rich.console import Console
from rich.markdown import Markdown

md = Markdown(MARKDOWN)
console.print(md)