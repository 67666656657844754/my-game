import tkinter as tk

root = tk.Tk()

root.title("game over")
root['bg'] = "#fafafa"
root.geometry("300x100+400+100")


game_over = tk.Label(root, text="GAME OVER", fg="Red", bg="#fafafa", font=("Arial", 24))
game_over.pack()
okbutt = tk.Button(root, text="Ok", fg="Red", bg="#fafafa" ,font=("Aerial", 24))
okbutt.pack()

root.mainloop()
