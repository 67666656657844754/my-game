import tkinter as tk
import subprocess
import sys
import os

# Create the main window
root = tk.Tk()
root.title("Square, Квадрат")
root['bg'] = "#fafafa"
root.geometry("800x500+400+100")

# Function to start the game by running 'game.py'
def start_game():
    python = sys.executable  # Get the path to the current Python interpreter
    game_path = os.path.join(os.getcwd(), "game.py")  # Build the full path to game.py
    subprocess.run([python, game_path])  # Run the game script

# Function to open a new window with game information
def about_game():
    about_window = tk.Toplevel(root)  # Create a new window on top of the main window
    about_window.title("About the game, про гру")
    about_window['bg'] = "#fafafa"
    about_window.geometry("800x500+400+100")

    # English description
    about_label = tk.Label(
        about_window,
        text="This is a Square game where you control a blue square to avoid red enemies.",
        fg="black",
        bg="#fafafa",
        font=("Arial", 16)
    )
    about_label.pack(pady=20)

    # Ukrainian description
    about_label_ua = tk.Label(
        about_window,
        text="Це квадратна гра, де ви керуєте синім квадратом, щоб уникнути червоних ворогів.",
        fg="black",
        bg="#fafafa",
        font=("Arial", 12)
    )
    about_label_ua.pack(pady=10)

# Main label with game title
text_game = tk.Label(
    root,
    text="Square game",
    fg="red",
    bg="#fafafa",
    font=("Arial", 24)
)
text_game.pack(pady=30)

# Button to start the game
game_start = tk.Button(
    root,
    text="Go",
    fg="red",
    bg="#fafafa",
    font=("Arial", 24),
    command=start_game
)
game_start.pack(pady=10)

# Button to show information about the game
about_game_button = tk.Button(
    root,
    text="About the game, про гру",
    fg="red",
    bg="#fafafa",
    font=("Arial", 20),
    command=about_game
)
about_game_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()