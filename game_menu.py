import tkinter as tk
import subprocess
import sys
import os

root = tk.Tk()

def start_game():
    python = sys.executable
    subprocess.run([python, os.path.join(os.getcwd(), "game.py")])

def about_game():
    
    about_window = tk.Toplevel(root)
    about_window.title("About the game, про гру")
    about_window['bg'] = "#fafafa"
    about_window.geometry("800x500+400+100")
    
    
    about_label = tk.Label(about_window, text="This is a Square game where you control a blue square to avoid red enemies.", fg="Black", bg="#fafafa", font=("Arial", 16))
    about_label.pack(pady=20)
    about_label_ua = about_label = tk.Label(about_window, text="Це квадратна гра, де ви керуєте синім квадратом, щоб уникнути червоних ворогів.", fg="Black", bg="#fafafa", font=("Arial", 10))
    about_label_ua.pack(pady=20)

root.title("Square, Квадрат")
root['bg'] = "#fafafa"
root.geometry("800x500+400+100")


text_game = tk.Label(root, text="Square game", fg="Red", bg="#fafafa", font=("Arial", 24))
text_game.pack()


game_start = tk.Button(root, text="Go", fg="Red", bg="#fafafa", font=("Arial", 24), command=start_game)
game_start.pack()


about_game_button = tk.Button(root, text="About the game, про гру", fg="Red", bg="#fafafa", font=("Arial", 24), command=about_game)
about_game_button.pack()

root.mainloop()
