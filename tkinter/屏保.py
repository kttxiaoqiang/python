import tkinter
import time
import random


baseframe=tkinter.Tk()
cvs=tkinter.Canvas(baseframe,width=500,height=500)          # 摆放画布
cvs.pack()

class ScreenSaver():
    def __init__(self,color):
        self.color=color
        self.oval_x=random.randint(50,100)
        self.oval_y=random.randint(100,150)
        self.ball = cvs.create_oval(self.oval_x, self.oval_x,self.oval_y,self.oval_y, fill=self.color)
        self.x = random.random()
        self.y = random.random()

    def draw_ball(self):

        cvs.move(self.ball,self.x,self.y)
        self.pos=cvs.coords(self.ball)
        # print(pos)
        if self.pos[0]<=0:
            self.x=1
        if self.pos[2]>=500:
            self.x=-1

        if self.pos[1]<=0:
            self.y=1
        if self.pos[3]>=500:
            self.y=-1

if __name__=="__main__":
    s1=ScreenSaver("red")
    s2=ScreenSaver("yellow")
    s3 = ScreenSaver("green")
    while 1:
        s1.draw_ball()
        s2.draw_ball()
        s3.draw_ball()
        cvs.update()
        cvs.update_idletasks()
        time.sleep(0.005)


