import tkinter as tk

root = tk.Tk()
root.title("Game Over")
root['bg'] = "#fafafa"
root.geometry("300x100+400+100")

game_over = tk.Label(root, text="GAME OVER", fg="Red", bg="#fafafa", font=("Arial", 24))
game_over.pack()

def close_window():
    root.destroy()

okbutt = tk.Button(root, text="Ok", fg="Red", bg="#fafafa", font=("Arial", 24), command=close_window)
okbutt.pack()

root.mainloop()