
import tkinter

base=tkinter.Tk()

base.wm_title("这是个lable")

lb1=tkinter.Label(base,text="python AT")
lb1.pack()

lb2=tkinter.Label(base,text='绿色背景',background="green")
lb2.pack()

lb3=tkinter.Label(base,text='蓝色背景',background="blue")
lb3.pack()

base.mainloop()