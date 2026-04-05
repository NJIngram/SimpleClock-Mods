import tkinter as tk
from datetime import datetime
import threading
import time


class SimpleClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Clock")
        self.resizable(False, False)
        self.configure(bg="#1a1a1a", padx=20, pady=20)
        self.geometry("440x320")
        self.use_24hr = False

        self.time_label = tk.Label(
            self, font=("Impact", 48, "bold"),
            bg="#1a1a1a", fg="#f5c518",
            relief="flat"
        )
        self.time_label.pack(padx=20, pady=(20, 2))

        self.day_label = tk.Label(
            self, font=("Impact", 22),
            bg="#1a1a1a", fg="#ff6a00"
        )
        self.day_label.pack(padx=20, pady=2)

        self.date_label = tk.Label(
            self, font=("Impact", 18),
            bg="#1a1a1a", fg="#cccccc"
        )
        self.date_label.pack(padx=20, pady=(2, 14))

        self.toggle_button = tk.Button(
            self, text="TOGGLE 24HR",
            font=("Impact", 14),
            bg="#f5c518", fg="#1a1a1a",
            activebackground="#ff6a00", activeforeground="#1a1a1a",
            relief="flat", cursor="hand2",
            padx=14, pady=4,
            command=self.toggle_24hr
        )
        self.toggle_button.pack(pady=(0, 20))

        t = threading.Thread(target=self._clock_thread, daemon=True)
        t.start()
        self.mainloop()

    def _clock_thread(self):
        while True:
            self.after(0, self.update_clock)
            time.sleep(1)

    def update_clock(self):
        now = datetime.now()
        if self.use_24hr:
            self.time_label.config(text=now.strftime("%H:%M:%S"))
        else:
            self.time_label.config(text=now.strftime("%I:%M:%S %p"))
        self.day_label.config(text=now.strftime("%A"))
        self.date_label.config(text=now.strftime("%d %B, %Y"))

    def toggle_24hr(self):
        self.use_24hr = not self.use_24hr


if __name__ == "__main__":
    SimpleClock()
