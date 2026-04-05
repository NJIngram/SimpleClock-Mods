import tkinter as tk
from datetime import datetime
import threading
import time


class SimpleClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Clock")
        self.resizable(False, False)
        self.configure(bg="white", padx=20, pady=20)
        self.geometry("400x250")

        self.time_label = tk.Label(self, font=("Sans-Serif", 59), bg="black", fg="white")
        self.time_label.pack(padx=20, pady=(20, 5))

        self.day_label = tk.Label(self, font=("Ink Free", 34, "bold"))
        self.day_label.pack(padx=20, pady=5)

        self.date_label = tk.Label(self, font=("Ink Free", 30, "bold"))
        self.date_label.pack(padx=20, pady=(5, 20))

        t = threading.Thread(target=self._clock_thread, daemon=True)
        t.start()
        self.mainloop()

    def _clock_thread(self):
        while True:
            self.after(0, self.update_clock)
            time.sleep(1)

    def update_clock(self):
        now = datetime.now()
        self.time_label.config(text=now.strftime("%I:%M:%S %p"))
        self.day_label.config(text=now.strftime("%A"))
        self.date_label.config(text=now.strftime("%d %B, %Y"))


if __name__ == "__main__":
    SimpleClock()
