import tkinter

def baseLable(event):
    global baseframe
    lable1=tkinter.Label(baseframe,text='谢谢点击')
    lable1.pack()

baseframe=tkinter.Tk()

btn1=tkinter.Button(baseframe,text='模拟点击')
btn1.bind('<Button-1>',baseLable)
btn1.pack()

# tkinter.mainloop()
