import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    tori = tk.PhotoImage(file="./fig/8.png")
    cx,cy = 300,400
    canvas.create_image(cx, cy, tori, tag = "tori")
    root.mainloop()