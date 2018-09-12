import tkinter

def reg():
    name=e1.get()
    pwd=e2.get()

    t1=len(name)
    t2=len(pwd)

    if name =='111' and pwd=='222':
        lb3['text']='登录成功'
    else:
        lb3['text']='用户名或密码错误'
        e1.delete(0,t1)
        e2.delete(0,t2)

baseframe=tkinter.Tk()

lb1=tkinter.Label(baseframe,text='用户名')
lb1.grid(row=0,column=0,stick=tkinter.E)

e1=tkinter.Entry(baseframe)
e1.grid(row=0,column=1,stick=tkinter.E)

lb2=tkinter.Label(baseframe,text='密码')
lb2.grid(row=1,column=0,stick=tkinter.E)

e2=tkinter.Entry(baseframe)
e2.grid(row=1,column=1,stick=tkinter.E)
e2['show']='*'   #设置遮挡字符

btn1=tkinter.Button(baseframe,text='登录',command=reg)
btn1.grid(row=2,column=1,stick=tkinter.E)

lb3=tkinter.Label(baseframe,text='')
lb3.grid(row=2,column=2)

tkinter.mainloop()