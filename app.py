from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Digits
from timer import Timer

class PawseApp(App):
    CSS_PATH = "pawse.css"
    ENABLE_COMMAND_PALETTE = False
    BINDINGS = [
        ("space", "toggle_timer", "Start | Pause"), # do i use / instead?
        ("r", "reset_timer", "Reset"), # im 90% sure that this basically
        ("q", "quit", "Quit"), # just calls action_funcname or something 
        # and its like: keybind:function:display
    ]
    def update_timer(self):
        remaining = self.timer.get_remaining()

        minutes = int(remaining) // 60
        seconds = int(remaining) % 60

        self.query_one("#timer", Digits).update(f"{minutes:02}:{seconds:02}")
    def on_mount(self):
        self.set_interval(1, self.update_timer)
    def __init__(self):
        super().__init__()
        self.timer = Timer(25 * 60)
        
    def compose(self) -> ComposeResult:
        minutes = int(self.timer.get_remaining()) // 60
        seconds = int(self.timer.get_remaining()) % 60
        yield Header()
        yield Digits(f"{minutes:02}:{seconds:02}", id="timer")
        yield Footer()

    def action_toggle_timer(self):
        if self.timer.running:
            self.timer.pause()
        else:
            self.timer.start()

    def action_reset_timer(self):
        self.timer.reset()

if __name__ == "__main__":
    PawseApp().run()