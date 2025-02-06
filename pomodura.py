import tkinter as tk
import time
import ctypes
import os
from threading import Timer

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")
        self.time_var = tk.StringVar()
        self.time_var.set("25:00")
        self.running = False
        self.paused = False
        self.remaining_time = 25 * 60  # 25 minutes
        
        self.label = tk.Label(root, textvariable=self.time_var, font=("Helvetica", 48))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)
    
    def update_time(self):
        if self.running:
            minutes, seconds = divmod(self.remaining_time, 60)
            self.time_var.set(f"{minutes:02}:{seconds:02}")
            if self.remaining_time > 0:
                self.remaining_time -= 1
                self.root.after(1000, self.update_time)
            else:
                self.running = False
                self.lock_screen()
    
    def start_timer(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.update_time()
    
    def pause_timer(self):
        if self.running:
            self.running = False
            self.paused = True
    
    def reset_timer(self):
        self.running = False
        self.paused = False
        self.remaining_time = 25 * 60
        self.time_var.set("25:00")
    
    def lock_screen(self):
        if os.name == 'nt':  # Windows
            ctypes.windll.user32.LockWorkStation()
        elif os.name == 'posix':  # macOS and Linux
            # This is a placeholder, as locking the screen in macOS/Linux typically requires different handling
            # For macOS, use: os.system('/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend')
            # For Linux, use: os.system('gnome-screensaver-command --lock')
            print("Locking screen on macOS/Linux is not implemented in this script.")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()