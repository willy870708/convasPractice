from tkinter import*

from pynput import mouse

win = Tk()
win.title("Canvas")
win.geometry("1200x750+150-50")
x,y = win.winfo_pointerxy()
l=Button(text = "draw line",font = "Arial 15")
l.pack(side = BOTTOM)
p=Button(text = "draw point",font = "Arial 15")
p.pack(side = BOTTOM)


c = Canvas(win,height=800,width=1200,bg="skyblue")
c.pack()

class Point():
    def __init__(self,x,y,number):
        self.x = x
        self.y = y
        self.number = number
    def drawcircle(self):
        c.create_oval(self.x-25,self.y-25,self.x+25,self.y+25,fill="red")
        c.create_text(self.x,self.y,fill = "black", font = "Arial 14",text = self.number)
        circle.append(self.number)
        self.number=self.number+2
class Line():
    def __init__(self,p1,p2,weight):
        self.p1 = p1
        self.p2 = p2
        self.weight = weight
    

circle=[]
temp = []
i=1
def on_click(event):
    global i 
    point = Point(event.x,event.y,i)
    point.drawcircle()
    i=i+1

def drawline(event):
    c.create_oval(event.x-0.1,event.y-0.1,event.x,event.y, fill = "black")
    
def bindp():
    c.bind("<Button-1>",on_click)
    c.unbind("<B1-Motion>",drawline)
    


def bindl():
    c.bind("<B1-Motion>",drawline)
    c.unbind("<Button-1>",on_click)
        

p.config(command = bindp)    
l.config(command = bindl)



win.mainloop()  





