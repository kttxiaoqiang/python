import tkinter

def showLable():
    global baseFrame
    #在函数中定义一个函数
    #lable的父组件是baseFrame
    lb=tkinter.Label(baseFrame,text="显示lable")
    lb.pack()

baseFrame=tkinter.Tk()

btn=tkinter.Button(baseFrame,text="showlable",command=showLable)
btn.pack()

baseFrame.mainloop()