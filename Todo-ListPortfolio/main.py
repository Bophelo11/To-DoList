#Logic
##Import modules that are needed(tkinter,turtles,time,sys etc.)
from tkinter import *
import tkinter.messagebox

##Setup the screen
screen = Tk()
screen.title("What the F*#k are we gonna do today?")
screen.minsize(width=400, height=900)
screen.config(bg="gray")
#Setup the mini popup screens
frame_tsk = Frame(screen)
frame_tsk.pack()

listbox_task=Listbox(frame_tsk,bg="black",fg="white",height=15,width=50,font = "Helvetica")
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task=Scrollbar(frame_tsk)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

#define the functions
def Enter_task():
    input_text = ""

    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text =="":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some text")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Add Task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()
##Define the delete function
def delete_butt():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])

##define the markcompleted function
def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    temp_marked = listbox_task.get(marked)
    temp_marked = temp_marked + "✔"
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)




#Define the buttons
En_Butt = Button(screen,text="Enter a task",width=30, command=Enter_task)
En_Butt.pack(pady=3)

del_butt = Button(screen,text="Remove a task", width=30, command=delete_butt)
del_butt.pack(pady=3)

mk_butt = Button(screen,text="Mark as Complete", width=30, command=markcompleted)
mk_butt.pack(pady=3)

#keep screen open
screen.mainloop()

