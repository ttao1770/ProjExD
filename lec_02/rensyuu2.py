print("hello world")

import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showwarning(txt,f"[{txt}]ボタンが押されました")

root = tk.Tk()
root.title("テキトーなタイトル")
root.geometry("500x300")

label = tk.Label(root,text="ラベルを書いてみ竹",font=("Times New Roman",20))
label.pack()

button = tk.Button(root,text = "don't push", command = button_click)
button.bind("<1>",button_click)
button.pack()

entry = tk.Entry(root,width=30)
entry.insert(tk.END, "hoge")
entry.pack()

root.mainloop()