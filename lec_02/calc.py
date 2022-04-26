import tkinter as tk
import tkinter.messagebox as tkm
from tkinter.tix import COLUMN

if __name__ == "__main__":
    
    root = tk.Tk()
    root.geometry("300x450")


    c = 1
    for i in range(3):
         for j in range(3):
            btn = tk.Button(root, text=i+j+c, font=("Times New Roman", 30))
            if j >= 2:
                c += 2
            btn.grid(row = i, column = j)
    btn = tk.Button(root, text=0, font=("Times New Roman", 30))
    btn.grid(row = 4, column = 0)
    
    root.mainloop()