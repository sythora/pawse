from pathlib import Path
from PIL import Image, ImageSequence
from rich_pixels import Pixels
import sys

if getattr(sys, "frozen", False):
    asset_dir = Path(sys._MEIPASS) / "assets"
else: # MEIPASS is the pyinstaller temp, so its detecting 
    # if its running in py or pyinstaller
    asset_dir = Path(__file__).parent / "assets" # fix cuz i went one to up or something
class meow:
    def __init__(self):
        self.state_gifs = {
            "sleeping": "sleeping.gif",
            "working": "working.gif",
            "happy": "happy.gif",
            "break": "break.gif",
            "excited": "excited.gif",
            "thinking": "thinking.gif"
        }
    # thank you stackoverflow! Rest in Peace!
        self.frames = {}
        self.frame = 0

    def load(self, state: str):
        if state in self.frames:
            return  # shit's already loaded, no need for a mem leak
        filename = self.state_gifs.get(state)
        # I had to learn this stuff from scratch...
        if filename is None:
            raise ValueError(f"Unknown meow state: {state}")

        path = asset_dir / filename
        if path.exists():
            with Image.open(path) as gif:
                self.frames[state] = []
               
                for frame in ImageSequence.Iterator(gif):
                    self.frames[state].append(frame.convert("RGBA"))
        else:
            print("broski where did the kittens go?")
            raise FileNotFoundError(f"GIF file not found: {path}")
    
        # this is like barely 100 lines of code total i think and this is taking a shit ton of time, wow, python is hard for me... idk how these skids do it, 
        # oh wow CLAUDE!!
    def get(self, state: str):
        if state not in self.frames:
            self.load(state)

        frames = self.frames[state]
        frame = frames[self.frame]
        self.frame = (self.frame + 1) % len(frames)
        return  Pixels.from_image(frame)