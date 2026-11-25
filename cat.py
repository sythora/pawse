
from pathlib import Path
from PIL import Image, ImageSequence
from rich_pixels import Pixels
import sys

if getattr(sys, "frozen", False):
    asset_dir = Path(sys._MEIPASS) / "assets"
else:
    asset_dir = Path(__file__).parent / "assets"


class Meow:
    def __init__(self):
        self.state_gifs = {
            "finished_calico": "cheering_calico.gif",
            "focused_tuxedo": "focused_tuxedo.gif",
            "sleepy_tabby": "sleepy_tabby.gif",
            "zoomies_tabby": "zoomies_tabby.gif",
        }

        self.frames = {}
        self.frame = {}

    def load(self, state: str):
        if state in self.frames:
            return

        filename = self.state_gifs.get(state)

        if filename is None:
            raise ValueError(f"Unknown meow state: {state}")

        path = asset_dir / filename

        if not path.exists():
            print("broski where did the kittens go?")
            raise FileNotFoundError(f"GIF file not found: {path}")

        with Image.open(path) as gif:
            self.frames[state] = []

            for frame in ImageSequence.Iterator(gif):
                self.frames[state].append(frame.convert("RGBA").copy())

        self.frame[state] = 0

    def get(self, state: str):
        if state not in self.frames:
            self.load(state)

        frames = self.frames[state]
        frame = frames[self.frame[state]]

        self.frame[state] = (self.frame[state] + 1) % len(frames)

        return Pixels.from_image(frame)
