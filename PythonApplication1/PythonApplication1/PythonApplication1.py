import threading
import subprocess
import time
import random
import ctypes
import pygame
import os
import sys

# ---------------- Configuration ----------------
run_duration = 60  # Run for 1 minute
start_time = time.time()

weird_images = [
    "weird1.jpg",
    "weird2.png",
    "weird3.jpg"
]

# Add as many common Windows apps as desired
apps = [
    "notepad.exe",
    "calc.exe",
    "mspaint.exe",
    "explorer.exe",
    "cmd.exe",
    "taskmgr.exe",
    "control.exe",
    "write.exe",  # WordPad
    r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe"
]

# ---------------- Mouse Blocking ----------------
def block_input():
    ctypes.windll.user32.BlockInput(True)

def unblock_input():
    ctypes.windll.user32.BlockInput(False)

# ---------------- Open Random Apps Quickly ----------------
def open_apps_spam():
    while time.time() - start_time < run_duration:
        app = random.choice(apps)
        try:
            subprocess.Popen(app)
        except:
            pass
        time.sleep(0.05)  # faster launching

# ---------------- Rapid Weird Images ----------------
def show_images():
    while time.time() - start_time < run_duration:
        image_path = random.choice(weird_images)
        if not os.path.exists(image_path):
            continue
        try:
            pygame.init()
            img = pygame.image.load(image_path)
            width, height = img.get_size()
            screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
            pygame.display.set_caption("😵 Weird Image 😵")
            screen.blit(img, (0, 0))
            pygame.display.flip()
            t0 = time.time()
            while time.time() - t0 < 0.2:
                for event in pygame.event.get():
                    pass  # do nothing
                time.sleep(0.01)
            pygame.quit()
        except Exception as e:
            print(f"Image error: {e}")
        time.sleep(0.05)

# ---------------- Main Logic ----------------
def main():
    print("Blocking input and starting chaos for 5 minutes...")
    block_input()

    thread_apps = threading.Thread(target=open_apps_spam, daemon=True)
    thread_images = threading.Thread(target=show_images, daemon=True)

    thread_apps.start()
    thread_images.start()

    while time.time() - start_time < run_duration:
        time.sleep(1)

    unblock_input()
    print("5 minutes passed. Input restored. Program ends.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        unblock_input()
        print("\nForcefully stopped. Input restored.")

