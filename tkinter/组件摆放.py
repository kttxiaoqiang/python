#pack：按照方位布局
#place：按照坐标布局
#grid：按照网格布局

import tkinter

'''
pack布局方式
'''

def PackMode():
    baseframe=tkinter.Tk()

    btn1=tkinter.Button(baseframe,text='A',background='green')
    btn1.pack(side=tkinter.LEFT,expand=tkinter.YES,fill=tkinter.Y)

    btn2=tkinter.Button(baseframe,text='B')
    btn2.pack(side=tkinter.TOP,expand=tkinter.YES,fill=tkinter.BOTH)

    btn3=tkinter.Button(baseframe,text='C')
    btn3.pack(side=tkinter.RIGHT,expand=tkinter.YES,fill=tkinter.NONE)

    btn4=tkinter.Button(baseframe,text='D')
    btn4.pack(side=tkinter.LEFT,expand=tkinter.NO,fill=tkinter.Y)

    btn5=tkinter.Button(baseframe,text='E')
    btn5.pack(side=tkinter.TOP,expand=tkinter.NO,fill=tkinter.BOTH)

    btn6=tkinter.Button(baseframe,text='F')
    btn6.pack(side=tkinter.BOTTOM,expand=tkinter.YES,fill=tkinter.BOTH)

    baseframe.mainloop()

def GridMode():

    import  tkinter

    baseframe=tkinter.Tk()
    baseframe.wm_title('登录窗口')

    lb1=tkinter.Label(baseframe,text='账号').grid(row=0,sticky=tkinter.E)
    tkinter.Entry(baseframe).grid(row=0,column=1,sticky=tkinter.E)

    lb2=tkinter.Label(baseframe,text='密码').grid(row=1,sticky=tkinter.E)
    tkinter.Entry(baseframe).grid(row=1,column=1,sticky=tkinter.E)

    btn=tkinter.Button(baseframe,text='登录').grid(row=2,column=1,sticky=tkinter.E)

    baseframe.mainloop()



def PlaceMode():
    





# GridMode()
# PackMode()




