#!/usr/bin/env python
# coding: utf-8

# In[78]:


from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    
    if text =='=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "ERROR"
        
        scvalue.set(value)
        
        
    elif text == 'C':
        scvalue.set("")
        #scvalue.update()
    
    else:
        scvalue.set(scvalue.get()+ text)
        #scvalue.update()
        

root = Tk()
root.title("CALCULATOR")
root.geometry("300x600")
root['background']='#e9f2f2'

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, 
               font= 'Calibri 30 bold',bg='#d3eaeb')
screen.pack(fill = X, ipadx=8, padx=10, pady=10)



frame1 = Frame(root, bg= '#e9f2f2')

b1 = Button(frame1,text='9', bg= '#d36ff8',
            font= 'Calibri 20 bold',padx=6, pady=6)
b1.pack(side=LEFT,padx=23, pady=3)
b1.bind("<Button-1>", click)

b2 = Button(frame1,text='8', bg= '#d36ff8',
           font= 'Calibri 20 bold',padx=6, pady=6)
b2.pack(side=LEFT,padx=23, pady=3)
b2.bind("<Button-1>", click)

b3 = Button(frame1,text='7', bg= '#d36ff8',
           font= 'Calibri 20 bold',padx=6, pady=6)
b3.pack(side=LEFT,padx=23, pady=3)
b3.bind("<Button-1>", click)

frame1.pack(fill = X, padx=5, pady=5)



frame1 = Frame(root, bg= '#e9f2f2')

b1 = Button(frame1,text='6', bg= '#d36ff8',
            font= 'Calibri 20 bold',padx=6, pady=6)
b1.pack(side=LEFT,padx=23, pady=3)
b1.bind("<Button-1>", click)

b2 = Button(frame1,text='5', bg= '#d36ff8',
            font= 'Calibri 20 bold',padx=6, pady=6)
b2.pack(side=LEFT,padx=23, pady=3)
b2.bind("<Button-1>", click)

b3 = Button(frame1,text='4', bg= '#d36ff8',
           font= 'Calibri 20 bold',padx=6, pady=6)
b3.pack(side=LEFT,padx=23, pady=3)
b3.bind("<Button-1>", click)

frame1.pack(fill = X, padx=5, pady=5)



frame1 = Frame(root, bg= '#e9f2f2')

b1 = Button(frame1,text='3', bg= '#d36ff8',
            font= 'Calibri 20 bold',padx=6, pady=6)
b1.pack(side=LEFT,padx=23, pady=3)
b1.bind("<Button-1>", click)

b2 = Button(frame1,text='2', bg= '#d36ff8',
           font= 'Calibri 20 bold',padx=6, pady=6)
b2.pack(side=LEFT,padx=23, pady=3)
b2.bind("<Button-1>", click)

b3 = Button(frame1,text='1', bg= '#d36ff8',
           font= 'Calibri 20 bold',padx=6, pady=6)
b3.pack(side=LEFT,padx=23, pady=3)
b3.bind("<Button-1>", click)

frame1.pack(fill = X, padx=5, pady=5)



frame1 = Frame(root, bg= '#e9f2f2')

b1 = Button(frame1,text='-',bg= '#d36ff8',
            font= 'Calibri 23 bold',padx=6, pady=6)
b1.pack(side=LEFT,padx=23, pady=3)
b1.bind("<Button-1>", click)

b2 = Button(frame1,text='0', bg= '#d36ff8',
           font= 'Calibri 20 bold',padx=6, pady=6)
b2.pack(side=LEFT,padx=23, pady=3)
b2.bind("<Button-1>", click)

b3 = Button(frame1,text='*', bg= '#d36ff8',
           font= 'Calibri 22 bold',padx=6, pady=6)
b3.pack(side=LEFT,padx=23, pady=3)
b3.bind("<Button-1>", click)

frame1.pack(fill = X, padx=5, pady=5)



frame1 = Frame(root, bg= '#e9f2f2')

b1 = Button(frame1,text='/', bg= '#d36ff8',
            font= 'Calibri 20 bold',padx=6, pady=6)
b1.pack(side=LEFT,padx=23, pady=3)
b1.bind("<Button-1>", click)

b2 = Button(frame1,text='%', bg= '#d36ff8',
           font= 'Calibri 19 bold',padx=6, pady=6)
b2.pack(side=LEFT,padx=23, pady=3)
b2.bind("<Button-1>", click)

b3 = Button(frame1,text='+', bg= '#d36ff8',
           font= 'Calibri 20 bold',padx=6, pady=6)
b3.pack(side=LEFT,padx=23, pady=3)
b3.bind("<Button-1>", click)

frame1.pack(fill = X, padx=5, pady=5)



frame1 = Frame(root, bg= '#e9f2f2')

b1 = Button(frame1,text='.',bg= '#d36ff8',
            font= 'Calibri 24 bold',padx=6, pady=6)
b1.pack(side=LEFT,padx=23, pady=3)
b1.bind("<Button-1>", click)

b2 = Button(frame1,text='=', bg= '#d36ff8',
           font= 'Calibri 22 bold',padx=6, pady=6)
b2.pack(side=LEFT,padx=23, pady=3)
b2.bind("<Button-1>", click)

b3 = Button(frame1,text='C', bg= '#d36ff8',
           font= 'Calibri 20 bold',padx=6, pady=6)
b3.pack(side=LEFT,padx=23, pady=3)
b3.bind("<Button-1>", click)

frame1.pack(fill = X, padx=5, pady=5)



root.mainloop()


# In[ ]:




