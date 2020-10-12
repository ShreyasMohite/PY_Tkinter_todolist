





from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import threading


class Todo:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x600")
        self.root.title("Todo List")
        self.root.iconbitmap("logo985.ico")
        self.root.resizable(0,0)

        select_task=IntVar()
        add_task=StringVar()
        completed_task=StringVar()





    #==================hover button==================================#

        def on_enter1(e):
            But_select_task['background']="black"
            But_select_task['foreground']="cyan"  
        def on_leave1(e):
            But_select_task['background']="SystemButtonFace"
            But_select_task['foreground']="SystemButtonText"

            

        def on_enter2(e):
            But_add_task['background']="black"
            But_add_task['foreground']="cyan"  
        def on_leave2(e):
            But_add_task['background']="SystemButtonFace"
            But_add_task['foreground']="SystemButtonText"



        def on_enter3(e):
            But_done_task['background']="black"
            But_done_task['foreground']="cyan"  
        def on_leave3(e):
            But_done_task['background']="SystemButtonFace"
            But_done_task['foreground']="SystemButtonText"

        def on_enter4(e):
            But_clear_screen['background']="black"
            But_clear_screen['foreground']="cyan"  
        def on_leave4(e):
            But_clear_screen['background']="SystemButtonFace"
            But_clear_screen['foreground']="SystemButtonText"

        def on_enter5(e):
            But_clear_task['background']="black"
            But_clear_task['foreground']="cyan"  
        def on_leave5(e):
            But_clear_task['background']="SystemButtonFace"
            But_clear_task['foreground']="SystemButtonText"

        def on_enter6(e):
            But_reset_task['background']="black"
            But_reset_task['foreground']="cyan"  
        def on_leave6(e):
            But_reset_task['background']="SystemButtonFace"
            But_reset_task['foreground']="SystemButtonText"


    #=======================================================#
        def clear():
            select_task.set("0")
            add_task.set("")
            completed_task.set("")

        def select():
            if select_task.get()==0:
                tkinter.messagebox.showerror("Error","Please select number")
            else:
                lab_num_task.config(text=select_task.get())
                Ent_task.config(state="normal")
                But_add_task.config(state="normal")
                number_task_combo.config(state="disable")
                But_select_task.config(state="disable")


        
        tasks=list()
        dummy=list()
        
        def add_tasks_method():
            if add_task.get()=="":
                tkinter.messagebox.showerror("Error","Please Enter Valid Task")
            else:
                tasks.append(add_task.get())
                lab_task_present.config(text=tasks)
                add_task.set("")
                if len(tasks)==select_task.get():
                    Ent_task.config(state="disable")
                    But_add_task.config(state="disable")
                    Ent_complete_task.config(state="normal")
                    But_done_task.config(state="normal")


        def completed_task_method():
            name=completed_task.get()
            completed_task.set("")
            if name=="":
                tkinter.messagebox.showerror("Error","Please Enter Valid Task")
            else:
                if name in tasks:
                    tasks.remove(name)
                    dummy.append(name)
                    lab_task_completed_num.config(text=len(dummy))
                    lab_task_remaining_set.config(text=len(tasks))
                    lab_task_completed_set.config(text=dummy)
                    lab_task_remaining_get.config(text=tasks)
                    if len(tasks)==0:
                        lab_task_message.config(text="ALL TASKS ARE COMPLETED")

                else:
                    tkinter.messagebox.showerror("Error","Unknown task")
            

        
        def add_thread():
            t1=threading.Thread(target=add_tasks_method)
            t1.start()

        
        def reset():
            number_task_combo.config(state="readonly")
            But_select_task.config(state="normal")
            dummy.clear()
            tasks.clear()
            clear_screen()
            

        def clear_screen():
            lab_num_task.config(text="")
            lab_task_present.config(text="")
            lab_task_completed_num.config(text="0")
            lab_task_completed_set.config(text="[ ]")
            lab_task_remaining_set.config(text="0")
            lab_task_remaining_get.config(text="[ ]")
            lab_task_message.config(text="")
            








    #=======================frame=======================3=
        mainframe=Frame(self.root,width=500,height=600,bd=4,relief="ridge")
        mainframe.place(x=0,y=0)

        first_frame=Frame(mainframe,width=493,height=200,bd=4,relief="ridge")
        first_frame.place(x=0,y=0)

        second_frame=Frame(mainframe,width=493,height=393,bd=4,relief="ridge",bg="black")
        second_frame.place(x=0,y=200)
    

    #============================first_frame================================
        lab_frame=LabelFrame(first_frame,text="Enter Task",width=487,height=195,font=('times new roman',12,'bold'))
        lab_frame.place(x=0,y=0)

    #==============================lab_frame================================

        lab_number_task=Label(lab_frame,text="Select Number Of Task  :",font=('times new roman',12,"bold"))
        lab_number_task.place(x=0,y=0)

        lab_task=Label(lab_frame,text="Enter Name of Task       :",font=('times new roman',12,"bold"))
        lab_task.place(x=0,y=50)

        lab_completed=Label(lab_frame,text="Completed Task Name :",font=('times new roman',12,"bold"))
        lab_completed.place(x=0,y=100)

    #=========================Entry=================================================
        number_task=list(range(1,11))
        number_task_combo=Combobox(lab_frame,values=number_task,font=('arial',11),width=18,state="readonly",textvariable=select_task)
        number_task_combo.set("0")
        number_task_combo.place(x=200,y=10)

        Ent_task=Entry(lab_frame,state="disable",font=('times new roman',12),relief="sunken",bd=4,textvariable=add_task)
        Ent_task.place(x=200,y=53)

        Ent_complete_task=Entry(lab_frame,state="disable",font=('times new roman',12),relief="sunken",bd=4,textvariable=completed_task)
        Ent_complete_task.place(x=200,y=103)

    #==========================Button================================================
        But_select_task=Button(lab_frame,width=10,text="Select",cursor="hand2",font=('times new roman',10,"bold"),command=select)
        But_select_task.place(x=390,y=10)
        But_select_task.bind("<Enter>",on_enter1)
        But_select_task.bind("<Leave>",on_leave1)

        But_add_task=Button(lab_frame,state="disable",width=10,text="Add",cursor="hand2",font=('times new roman',10,"bold"),command=add_thread)
        But_add_task.place(x=390,y=53)
        But_add_task.bind("<Enter>",on_enter2)
        But_add_task.bind("<Leave>",on_leave2)

        But_done_task=Button(lab_frame,width=10,state="disable",text="Done",cursor="hand2",font=('times new roman',10,"bold"),command=completed_task_method)
        But_done_task.place(x=390,y=103)
        But_done_task.bind("<Enter>",on_enter3)
        But_done_task.bind("<Leave>",on_leave3)


        But_clear_screen=Button(lab_frame,width=10,text="Clear Screen",cursor="hand2",font=('times new roman',10,"bold"),command=clear_screen)
        But_clear_screen.place(x=390,y=143)
        But_clear_screen.bind("<Enter>",on_enter4)
        But_clear_screen.bind("<Leave>",on_leave4)

        But_clear_task=Button(lab_frame,width=10,text="Clear",cursor="hand2",font=('times new roman',10,"bold"),command=clear)
        But_clear_task.place(x=30,y=143)
        But_clear_task.bind("<Enter>",on_enter5)
        But_clear_task.bind("<Leave>",on_leave5)

        But_reset_task=Button(lab_frame,width=10,text="Reset",cursor="hand2",font=('times new roman',10,"bold"),command=reset)
        But_reset_task.place(x=200,y=143)
        But_reset_task.bind("<Enter>",on_enter6)
        But_reset_task.bind("<Leave>",on_leave6)

    #===========================Bottom_frame===================================================== 
        
        lab_total=Label(second_frame,text="Total Number of Task  =  ",font=('times new roman',12,'bold'),bg="black",fg="cyan")
        lab_total.place(x=110,y=20)

        lab_num_task=Label(second_frame,text="",font=('times new roman',12,'bold'),bg="black",fg="cyan")
        lab_num_task.place(x=300,y=20)

        lab_task=Label(second_frame,text="Tasks",font=('times new roman',12,'bold'),bg="black",fg="cyan")
        lab_task.place(x=20,y=50)

        lab_task_present=Label(second_frame,text="",font=('times new roman',12,'bold'),bg="black",fg="cyan")
        lab_task_present.place(x=20,y=75)

        lab_task_completed=Label(second_frame,text="Tasks Completed =",font=('times new roman',12,'bold'),bg="black",fg="cyan")
        lab_task_completed.place(x=20,y=125)

        lab_task_completed_num=Label(second_frame,text="0",font=('times new roman',12,'bold'),bg="black",fg="cyan")
        lab_task_completed_num.place(x=170,y=125)

        lab_task_completed_set=Label(second_frame,text="[ ]",font=('times new roman',12,'bold'),bg="black",fg="cyan")
        lab_task_completed_set.place(x=20,y=150)

        lab_task_remaining=Label(second_frame,text="Task Reamining  = ",font=('times new roman',12,'bold'),bg="black",fg="cyan")
        lab_task_remaining.place(x=150,y=210)

        lab_task_remaining_set=Label(second_frame,text="0",font=('times new roman',12,'bold'),bg="black",fg="cyan")
        lab_task_remaining_set.place(x=300,y=210)

        lab_task_remaining_get=Label(second_frame,text="[ ]",font=('times new roman',12,'bold'),bg="black",fg="cyan")
        lab_task_remaining_get.place(x=150,y=240)

        lab_task_message=Label(second_frame,text="",font=('times new roman',12,'bold'),bg="black",fg="red")
        lab_task_message.place(x=120,y=300)


        




if __name__ == "__main__":
    root=Tk()
    app=Todo(root)
    root.mainloop()