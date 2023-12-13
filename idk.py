import random
import tkinter

canvas = tkinter.Canvas(width=800,height=600)
canvas.pack()



farba = ["blue", "red", "cyan","pink"]
farba1 = random.choice(farba)


def Kruh():
    farba = ["blue", "red", "cyan","pink"]
    farba1 = random.choice(farba)
    canvas.create_oval(x , y, x1, y1, fill=farba1, outline="black")
    canvas.create_oval(x + 40 , y, x1+ 40, y1, fill=farba1, outline="black")
    canvas.create_oval(x , y+ 40, x1, y1+ 40, fill=farba1, outline="black")
    canvas.create_oval(x+40 , y  + 40, x1+40, y1+ 40, fill=farba1, outline="black")
    canvas.create_oval(x+20,y + 20,x1 +20,y1 + 20,  fill="yellow", outline="black")

c1 = 0
x = 10
y = 10
x1 = 50
y1 = 50
for i in range(63):
    Kruh()
    c1 = c1 + 1
    x = x + 85
    x1 = x1 + 85
    if c1 == 9 or c1 == 18 or c1 == 27 or c1 == 36 or c1 == 45 or c1 == 54 or c1 == 63:
        y = y + 80
        y1 = y1 + 80
        x = 10
        x1 = 50




canvas.mainloop()