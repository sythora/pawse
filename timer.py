import time

class Timer:
    def __init__(self, duration: int = 25 * 60): # 25 min in sec
        # store og duration so the time can be reset later
        self.duration = duration
        # track remaining time seperate from the og duration
        self.remaining = float(duration)
        # calc elapsed time 
        self.started = None
        self.running = False

    def start(self):
        # WHAT EVER YOU DO, DON'T restart A RUNNING TIMER
        if not self.running and self.remaining > 0:
            self.started = time.monotonic()
            self.running = True

    def pause(self):
        if self.running:
            # save remaining time if paused
            self.remaining = self.get_remaining()
            self.running = False
            self.started = None

    def reset(self):
        #nuke the shit out of the timer just like what happened to my soul after my girl broke up with me
        self.remaining = float(self.duration)
        self.running = False
        self.started = None
    def get_remaining(self):
     if self.running:
        elapsed = time.monotonic() - self.started
        remaining = max(0, self.remaining - elapsed)

        if remaining == 0:
            self.remaining = 0
            self.running = False

        return remaining

     return self.remaining
        
    def finished(self):
        return self.get_remaining() <= 0


    