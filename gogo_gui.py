from textual.app import App, ComposeResult
from textual.widgets import Markdown
from textual.widgets import Input, Button

EXAMPLE_MARKDOWN = """\
# Download Anime Episode from GoGoAnime

- take the *id* name from gogoanime
- Paste here
- Insert the Episode number you want
---
"""


class MarkdownExampleApp(App):
    def compose(self) -> ComposeResult:
        yield Markdown(EXAMPLE_MARKDOWN)
        yield Input(placeholder="enter gogoanime serie id")
        yield Button("Primary!", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button))
        
if __name__ == "__main__":
    app = MarkdownExampleApp()
    app.run()