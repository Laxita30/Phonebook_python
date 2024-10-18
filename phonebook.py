# from curses import window
from tkinter import *
from tkinter import ttk
from tkinter.tix import Tree
from tokenize import Name 
from views import *
from tkinter import messagebox
co0="#ffffff"
co1="#000000"
co2="#4456F0"
co3="#CDCDCD"

window= Tk()
window.title("")
window.geometry('485x450')
window.configure(background=co0)
window.resizable(width=False,height=False)


frame_up=Frame(window,width=500,height=50,bg=co2)
frame_up.grid(row=0,column=0,padx=0,pady=1)

frame_down=Frame(window,width=500,height=150,bg=co0)
frame_down.grid(row=1,column=0,padx=0,pady=1)

frame_table=Frame(window,width=500,height=100,bg=co0)
frame_table.grid(row=2,column=0,columnspan=2,padx=10,pady=1,sticky=NW)

def show():
    global tree
    listheader = ['Name','Gender','Telephone','Email']
    demo_list=view()
    tree=ttk.Treeview(frame_table,selectmode='extended' , columns=listheader,show="headings")

    vsb=ttk.Scrollbar(frame_table,orient="vertical",command=tree.yview)
    hsb=ttk.Scrollbar(frame_table,orient="horizontal",command=tree.xview)

    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
    tree.grid(column=0,row=0,sticky='nsew')
    vsb.grid(column=1,row=0,sticky='ns')
    hsb.grid(column=0,row=1,sticky='ew')

    tree.heading(0,text='Name',anchor=NW)
    tree.heading(1,text='Gender',anchor=NW)
    tree.heading(2,text='Telephone',anchor=NW)
    tree.heading(3,text='Email',anchor=NW)

    tree.column(0,width=120,anchor=NW)
    tree.column(1,width=50,anchor=NW)
    tree.column(2,width=100,anchor=NW)
    tree.column(3,width=180,anchor=NW)

    for item in demo_list:
        tree.insert('','end',values=item)

show()

def insert():
    Name=e_name.get()
    Gender=c_gender.get()
    Telephone=e_tphone.get()
    Email=e_email.get()

    data=[Name,Gender,Telephone,Email]
    if Name =='' or Gender=='' or Telephone=='' or Email=='':
        messagebox.showwarning('data','please fill in all blanks')
    else:
        add(data)
        messagebox.showinfo('data','data added successfully')
        e_name.delete(0,'end')
        c_gender.delete(0,'end')
        e_tphone.delete(0,'end')
        e_email.delete(0,'end')
        show()

def to_update():
    try:

        tree_data=tree.focus()
        tree_dictionary=tree.item(tree_data)
        tree_list=tree_dictionary['values']  
        Name=str(tree_list[0])
        Gender=str(tree_list[1])
        Telephone=str(tree_list[2])
        Email=str(tree_list[3])

        e_name.insert(0,Name)
        c_gender.insert(0,Gender)
        e_tphone.insert(0,Telephone)
        e_email.insert(0,Email)
        def confirm():
            new_name=e_name.get()
            new_gender=c_gender.get()
            new_telephone=e_tphone.get()
            new_email=e_email.get()
            data=[new_telephone,new_name,new_gender,new_telephone,new_email]
            update(data)
            messagebox.showinfo('success','data updated successfully')
            e_name.delete(0,'end')
            c_gender.delete(0,'end')
            e_tphone.delete(0,'end')
            e_email.delete(0,'end')
            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()
            show()
        b_confirm=b_delete = Button(frame_down,text='confirm',height=1,bg=co2,fg=co0,font=('Ivy 8 bold'),command=confirm)
        b_confirm.place(x=280,y=110)
    except IndexError:
        messagebox.showerror('Error','select one of them from the table')

def to_remove():
    try:
        tree_data=tree.focus()
        tree_dictionary=tree.item(tree_data)
        tree_list=tree_dictionary['values'] 
        tree_telephone=str(tree_list[2])

        remove(tree_telephone)
        messagebox.showinfo('Success','data has been deleted successfully')

        for widget in frame_table.winfo_children():
            widget.destroy()  
        show()
    except IndexError:
        messagebox.showerror('Error','select one of them from table')

def to_search():
    telephone=e_search.get()
    data=search(telephone)    

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('','end',values=item) 

    e_search.delete(0,'end')
#frame_up widgets

app_name=Label(frame_up,text="Phonebook",height=1,font=('verdana 17 bold'),fg= co0,bg=co2)
app_name.place(x=5,y=5)

#frame_down widget
l_name= Label(frame_down,text="Name *",width=20,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_name.place(x=10,y=20)
e_name=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_name.place(x=80,y=20)

l_gender= Label(frame_down,text="Gender *",width=20,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_gender.place(x=10,y=50)
c_gender=ttk.Combobox(frame_down,width=27)
c_gender['values'] = ['','Male','Female']
c_gender.place(x=80,y=50)

l_tphone= Label(frame_down,text="Telephone *",width=20,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_tphone.place(x=10,y=80)
e_tphone=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_tphone.place(x=80,y=80)

l_email=Label(frame_down,text="Email *",width=20,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_email.place(x=10,y=110)
e_email=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_email.place(x=80,y=110)

b_search= Button(frame_down,text="search", height=1,width=6,bg=co2,fg=co0,font=('Ivy 8 bold'),command=to_search)
b_search.place(x=290,y=20)
e_search=Entry(frame_down,width=16,justify='left',font=('Ivy', 11),highlightthickness=1,relief="solid")
e_search.place(x=347,y=20)

b_view = Button(frame_down,text='view',height=1,width=6,bg=co2,fg=co0,font=('Ivy 8 bold'),command=show)
b_view.place(x=290,y=50)

b_add = Button(frame_down,text='Add',height=1,width=7,bg=co2,fg=co0,font=('Ivy 8 bold'),command=insert)
b_add.place(x=400,y=50)

b_update = Button(frame_down,text='Update',height=1,width=7,bg=co2,fg=co0,font=('Ivy 8 bold'),command=to_update)
b_update.place(x=400,y=80)

b_delete = Button(frame_down,text='Delete',height=1,width=7,bg=co2,fg=co0,font=('Ivy 8 bold'),command=to_remove)
b_delete.place(x=400,y=110)

window.mainloop()