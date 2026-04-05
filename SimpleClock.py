import tkinter as tk
from datetime import datetime


class SimpleClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Clock")
        self.resizable(False, False)
        self.configure(bg="white")

        self.time_label = tk.Label(self, font=("Sans-Serif", 59), bg="black", fg="white")
        self.time_label.pack()

        self.day_label = tk.Label(self, font=("Ink Free", 34, "bold"))
        self.day_label.pack()

        self.date_label = tk.Label(self, font=("Ink Free", 30, "bold"))
        self.date_label.pack()

        self.update_clock()
        self.mainloop()

    def update_clock(self):
        now = datetime.now()
        self.time_label.config(text=now.strftime("%I:%M:%S %p"))
        self.day_label.config(text=now.strftime("%A"))
        self.date_label.config(text=now.strftime("%d %B, %Y"))
        self.after(1000, self.update_clock)


if __name__ == "__main__":
    SimpleClock()
