import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key

    key = event.keysym


def key_up(event):
    global key

    key = ""

def main_proc():
    global cx,cy,mx,my,key,c
    if key == "Up" and maze_bg[my-1][mx] == 0:
        my -= c
    if key == "Down" and maze_bg[my+1][mx] == 0:
        my += c
    if key == "Right" and maze_bg[my][mx+1] == 0:
        mx += c
    if key == "Left" and maze_bg[my][mx-1] == 0:
        mx -= c
    cx,cy = 100 * mx + 50, 100 * my +50

    root.after(100,main_proc)
    canvas.coords("tori", cx, cy)

def make_startgoal():
    canvas.create_rectangle(100,100,200,200,fill="green")
    canvas.create_rectangle(1300,700,1400,800,fill="red")

def even_fin():
    global cx,cy,mx,my,key,c
    if cx >= 1200 and cy >= 600:
        goal = tk.PhotoImage(file = "fig/20.png")
        cx,cy = 750,450
        canvas.create_image(cx, cy, image=goal, tag = "goal")
        c = 0
    


    
    



if __name__ == "__main__":

    key = ""
    my = 1
    mx = 1
    c = 1

    root = tk.Tk()
    root.title("迷えるこうかとん")
    #root.geometry("1500x900")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    

    maze_bg = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_bg)

    make_startgoal()

    
    tori = tk.PhotoImage(file = "fig/5.png")
    cx,cy = 100 * mx + 50, 100 * my +50
    canvas.create_image(cx, cy, image=tori, tag = "tori")
    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    even_fin()

    

    main_proc()
    root.mainloop()