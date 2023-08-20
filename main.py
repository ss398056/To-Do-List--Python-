from tkinter import * 
from tkinter import messagebox as mb
import tkinter

def addTask(event) :
    if task.get() != "":
        tasks.append(task.get())
        lbox.insert(0,task.get())
        task.delete(0,END)    
    else :
        mb.showerror("Error","Field not be empty")

    
def deleteTask(event) :
    item = lbox.get(ACTIVE)
    selected_listitem = lbox.curselection()

    if item in tasks :
        tasks.remove(item)
        lbox.delete(selected_listitem[0])
    
frame = Tk()
frame.geometry("600x500+400+100")
img = PhotoImage(file="todo.png")
frame.iconphoto(False,img)
frame.title("To Do List")
frame.configure(bg="#05ff48")

tasks = []


heading = Label(frame,text="To DO List",font=("Arial Black",20),bg="#05ff48",fg="grey").place(x=230,y=10)
add_taskl = Label(frame,text="Enter your task : ",bg="#05ff48",font=("Arial Black",10),fg="brown").place(x=50,y=70)
task = Entry(frame,width=25,font=("Arial",15))
task.place(x=180,y=70)
add = Button(frame,text="Add Task",font=("Arial Black",9),bg="blue",fg="white")
add.place(x=465,y=70)

task_heading = Label(frame,text="Tasks",font=("Arial Black",15),bg="#05ff48",fg="green").place(x=250,y=110)
lbox = Listbox(frame,width=50,height=10,font=("Arial Black",10))
lbox.place(x=80,y=150)

#del_task_heading = Label(frame,text="Delete Tasks",font=("Arial Black",15),bg="#05ff48",fg="Red").place(x=200,y=360)
delNol = Label(frame,text="Click on task then press delete button ",bg="#05ff48",font=("Arial Black",10),fg="brown").place(x=50,y=400)
deletebtn = Button(frame,text="Delete",font=("Arial Black",9),bg="Red",fg="white")
deletebtn.place(x=300,y=350)
add.bind('<Button-1>',addTask)
deletebtn.bind('<Button-1>',deleteTask)

frame.mainloop()