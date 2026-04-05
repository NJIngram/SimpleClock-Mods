import tkinter as tk
from tkinter import ttk
from datetime import datetime, timezone
import threading
import time


class SimpleClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Clock")
        self.resizable(False, False)
        self.configure(bg="#1a1a1a", padx=20, pady=20)
        self.geometry("440x380")
        self.use_24hr = False
        self.use_gmt = False

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

        style = ttk.Style()
        style.theme_use("default")
        style.configure("BL.TButton",
            font=("Impact", 14),
            background="#f5c518",
            foreground="#1a1a1a",
            borderwidth=0,
            focusthickness=0,
            padding=(14, 4)
        )
        style.map("BL.TButton",
            background=[("active", "#ff6a00")],
            foreground=[("active", "#1a1a1a")]
        )

        self.toggle_button = ttk.Button(
            self, text="TOGGLE 24HR",
            style="BL.TButton",
            cursor="hand2",
            command=self.toggle_24hr
        )
        self.toggle_button.pack(pady=(0, 20))

        self.tz_button = ttk.Button(
            self, text="TOGGLE GMT",
            style="BL.TButton",
            cursor="hand2",
            command=self.toggle_tz
        )
        self.tz_button.pack(pady=(0, 20))

        t = threading.Thread(target=self._clock_thread, daemon=True)
        t.start()
        self.mainloop()

    def _clock_thread(self):
        while True:
            self.after(0, self.update_clock)
            time.sleep(1)

    def update_clock(self):
        now = datetime.now(timezone.utc) if self.use_gmt else datetime.now()
        if self.use_24hr:
            self.time_label.config(text=now.strftime("%H:%M:%S"))
        else:
            self.time_label.config(text=now.strftime("%I:%M:%S %p"))
        self.day_label.config(text=now.strftime("%A"))
        self.date_label.config(text=now.strftime("%d %B, %Y"))

    def toggle_24hr(self):
        self.use_24hr = not self.use_24hr

    def toggle_tz(self):
        self.use_gmt = not self.use_gmt
        self.tz_button.config(text="TOGGLE LOCAL" if self.use_gmt else "TOGGLE GMT")
if __name__ == "__main__":
    SimpleClock()
