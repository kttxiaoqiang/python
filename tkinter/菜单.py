#普通菜单的代码
def nomal_menu():
    import tkinter
    baseframe=tkinter.Tk()
    menubar=tkinter.Menu(baseframe)

    for item in ['File','Edit','View','About']:
        menubar.add_command(label=item)
    baseframe['menu']=menubar


    baseframe.mainloop()

#级联菜单
def cascade_ment():
    import tkinter
    baseframe=tkinter.Tk()
    baseframe.wm_title('标题')
    menubar=tkinter.Menu(baseframe)
    emenu=tkinter.Menu(menubar)

    for item in ['COPY','PAST','CUT']:
        emenu.add_command(label=item)

    menubar.add_cascade(label='File',menu=emenu)
    menubar.add_cascade(label='Edit')
    menubar.add_cascade(label='About')

    baseframe['menu']=menubar
    baseframe.mainloop()

#弹出式菜单
def pop_menu():
    import tkinter
    baseframe=tkinter.Tk()

    def makelabel():
        tkinter.Label(baseframe,text="这个是python").pack()

    menubar=tkinter.Menu(baseframe)

    # emenu=tkinter.Menu(menubar)
    for x in ['1号菜','2号菜','三号菜']:
        menubar.add_separator()
        menubar.add_command(label=x)
    menubar.add_command(label='做菜了',command=makelabel)


    def pop(event):
        menubar.post(event.x_root,event.y_root)

    baseframe.bind('<Button-3>',pop)




    baseframe.mainloop()

pop_menu()