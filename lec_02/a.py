import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    entry.insert(tk.END,txt)
    btn.config(bg="#F0F8FF")
    btn.config(fg="#FF4500")


def plus_click(event):
    btn=event.widget
    btn.config(bg="#F0F8FF")
    btn.config(fg="#FF4500")
    txt=btn["text"]
    entry.insert(tk.END,txt)

def equal_click(event):
    siki=entry.get()
    ans=eval(siki)
    entry.delete(0,tk.END)
    entry.insert(tk.END,str(ans))



if __name__=="__main__":
    root=tk.Tk()
    root.geometry("300x450")

    entry=tk.Entry(justify="right",
                    width=10,
                    font=("Times New Roman",40))

    entry.grid(row=0,
                column=0,
                columnspan=3)


   

    r,c=0,0
    for i, num in enumerate(range(9,-3,-1),1):
        if num == -2:
            button=tk.Button(root, 
                        text="+", 
                        font=("Times New Roman",30))
            button.bind("<1>",plus_click)
        
        elif num == -1:
            button=tk.Button(root, 
                        text="=", 
                        font=("Times New Roman",30))
            button.bind("<1>",equal_click)

        else:
            button=tk.Button(root, 
                        text=num, 
                        font=("Times New Roman",30))
            button.bind("<1>",button_click)
    
        
        button.grid(row=r+1,
                    column=c,
                    padx=10,
                    pady=10)
        
        c+=1
        if i%3 == 0 :
            r+=1
            c=0

    root.mainloop()