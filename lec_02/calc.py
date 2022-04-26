import tkinter as tk
import tkinter.messagebox as tkm
from tkinter.tix import COLUMN

if __name__ == "__main__":
    
    root = tk.Tk()
    root.geometry("300x450")

    #入力欄の設定
    entry = tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
    
    entry.grid(row=0,column=0,columnspan=3)

#ボタンの設定
    def button_click(event):
        btn = event.widget
        txt = btn["text"]
        entry.insert(tk.END, txt)
        #tkm.showinfo(txt,f"{txt}のボタンが押されました")


    c = 1

    for i in range(3):
         for j in range(3):
            btn = tk.Button(root, text=i+j+c, font=("Times New Roman", 30))
            btn.bind("<1>",button_click)
            if j >= 2:
                c += 2
            btn.grid(row = i + 1, column = j, padx = 10, pady = 10)
    btn = tk.Button(root, text=0, font=("Times New Roman", 30))
    btn.grid(row = 4, column = 0, padx = 10, pady = 10)
    btn = tk.Button(root, text = "+", font = ("Time New Roman",30))
    btn.grid(row = 4, column = 1, padx = 10, pady = 10)
    btn = tk.Button(root, text = "=", font = ("Time New Roman", 30))
    btn.grid(row = 4, column = 2, padx = 10, pady = 10)
    btn.bind("<1>",button_click)
    
    
    root.mainloop()