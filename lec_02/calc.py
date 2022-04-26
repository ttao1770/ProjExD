import tkinter as tk
import tkinter.messagebox as tkm
from random import randint

#イコールを押した際に計算結果を出力する
def button_equrle(event):
        num = entry.get()
        res = eval(num)
        entry.delete(0,tk.END)
        entry.insert(tk.END, str(res))

#クリックしたときクリックした文字を画面に出力する
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, txt)
    #tkm.showinfo(txt,f"{txt}のボタンが押されました")

#ｃボタンを押した際に画面の数字をすべて消す
def button_color(event):
    entry.delete(0,tk.END)

#rdボタンを押した際にランダムに４桁までの数値を画面に出す
def button_random(event):
    num = randint(0,9999)
    entry.delete(0,tk.END)
    entry.insert(tk.END, str(num))

if __name__ == "__main__":
    
    root = tk.Tk()
    root.geometry("300x450")

#入力欄の設定
    entry = tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
    
    entry.grid(row=0,column=0,columnspan=4)

#ボタンの設定
    c = 1

    for i in range(3):
         for j in range(3):
            btn = tk.Button(root, text=i+j+c, font=("Times New Roman", 30))
            btn.bind("<1>",button_click)
            if j >= 2:
                c += 2
            btn.grid(row = i + 1, column = j)
    #0のボタンを追加
    btn = tk.Button(root, text=0, font=("Times New Roman", 30))
    btn.grid(row = 4, column = 0)
    btn.bind("<1>",button_click)
    #＋のボタンを追加
    btn = tk.Button(root, text = "+", font = ("Time New Roman",30))
    btn.grid(row = 4, column = 1)
    btn.bind("<1>",button_click)
    #＝のボタンを追加
    btn = tk.Button(root, text = "=", font = ("Time New Roman", 30))
    btn.grid(row = 4, column = 2)
    btn.bind("<1>",button_equrle)
    #cのボタンを追加
    btn = tk.Button(root, text= "c", font = ("Time New Roman", 30))
    btn.grid(row = 1, column=3)
    btn.bind("<1>",button_color)
    #ｒｄのボタンを追加
    btn = tk.Button(root, text = "rd", font = ("Time New Roman", 30))
    btn.grid(row = 2, column=3)
    btn.bind("<1>",button_random)

    
    root.mainloop()