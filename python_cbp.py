# IMPORTING THE REQUIRED FILES 
from tkinter import *
##import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import sqlite3


#TO OPEN A NEW WINDOW
root = Tk()
root.title('CONTACT BASED MANAGEMENT SYSTEM')
root.geometry("830x590")

# DATA FOR WORK
# Addind Fake Data
'''

 data = [
         (1, 'Johny', 'Elder', '9845239124', 'Johny@gmail.com'),
         (2, 'Mary', 'Smith', '8679414534', 'Mary@gmail.com'),
         (3, 'Tommy', 'Texter', '6079845672', 'TommyText@gmail.com'),
         (4, 'Edwin', 'Louis', '7056842948', 'LouisEdwin@gmail.com'),
         (5, 'Bobby', 'Elder', '8809759220', 'bobby@gmail.com'),
         (6, 'Steve', 'Smith', '7099050222', 'SteveSmith@gmail.com'),
         (7, 'Tina', 'Browne', '8099637889', 'Tina@gmail.com'),
         (8, 'Mark', 'Lane', '9088567883', 'Mark@gmail.com'),
         (9, 'John', 'Smith', '7094467853', 'Johnsmith@gmail.com'),
         (10, 'Mary', 'Louis', '6075542367', 'Mary12@gmail.com'),
         (11, 'Johny', 'Lane', '8077653445', 'JohnyLane@gmail.com'),
         (12, 'Mary', 'Bush', '8077669934', 'Mary20@gmail.com'),
         (13, 'Tommy', 'Field', '9077658963', 'TommyField@gmail.com'),
         (14, 'Erin', 'Smith', '7089965779', 'Erinsmith@gmail.com'),
         (15, 'Tony', 'Stark', '8808880888', 'Tonystark@gmail.com'),
         (16, 'Steve', 'Rogers', '7098876532', 'SteveRogers@gmail.com'),
         (17, 'Tina', 'Lane', '9099087654', 'TinaLane@gmail.com'),
         (18, 'Mark', 'Smith', '8077896543', 'Marksmith@gmail.com'),
         (19, 'John', 'Browne', '99912776176', 'Browne@gmail.com'),
         (20, 'Amanda', 'Rogers', '8907896546', 'Amanda@gmail.com')
        ]

'''

# DATABASE FOR THE PROJECT

def query_database():
        # clearing the treeview
        for contact in my_tree.get_children():
                my_tree.delete(contact)
                
        # Connecting to the database
        conn = sqlite3.connect('contact_m.db')
        # Creating a cursor instance
        c = conn.cursor()

        c.execute("SELECT rowid,* FROM contacts")
        records = c.fetchall()
        print(records)

        # Add our data to the screen
        global count
        count = 0
        
        for record in records:
                if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
                else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('oddrow',))
                # increment counter
                count += 1 
        
        
        # Commit the changes
        conn.commit()
        # Closing the connection
        conn.close()

def search_contacts():
        result_contact = search_entry.get()
        # close the search box
        search.destroy()

        # clearing the treeview
        for contact in my_tree.get_children():
                my_tree.delete(contact)


        # Connecting to the database
        conn = sqlite3.connect('contact_m.db')
        # Creating a cursor instance
        c = conn.cursor()

        c.execute("SELECT rowid,* FROM contacts WHERE lname like ?",(result_contact,))
        records = c.fetchall()

        # Add our data to the screen
        global count
        count = 0
        
        for record in records:
                if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
                else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('oddrow',))
                # increment counter
                count += 1 
        
        
        # Commit the changes
        conn.commit()
        # Closing the connection
        conn.close()


def results():
        global search_entry, search
        
        search = Toplevel(root)
        search.title("Search Bar")
        search.geometry("300x180")
##        search.iconbitmap('D:\SEM - 3\PYTHON LAB\Project\python_cbp.py')

        # Create a small minilevel label
        search_frame = LabelFrame(search, text = "Name")
        search_frame.pack(padx=10, pady=10)

        # Add entry box
        search_entry = Entry(search_frame)
        search_entry.pack(pady=20, padx=20 , ipadx=10)

        # Add button
        search_button = Button(search, text="Search Contacts" ,command = search_contacts)
        search_button.pack(padx=20, pady=20, ipadx = 8)
        

# ROOT MENU
my_menu = Menu(root)
root.config(menu = my_menu)
# Configure
search_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label = "Search", menu = search_menu )
# Creating a Drop Menu
search_menu.add_command(label="Search", command = results)
search_menu.add_command(label="Reset", command = query_database)
search_menu.add_separator()
search_menu.add_command(label="Exit", command = root.quit)
# ADD SOME STYLE (STYLE LIBRARY)
style = ttk.Style()

# THEME OF VIEW
style.theme_use('default') # We have 'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'

# CONFIGURE THE TREEVIEW COLORS
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
	background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10,padx=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command = my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("ID","First Name", "Last Name", "Phone","Email")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=CENTER, width=50,stretch=NO)
my_tree.column("First Name", anchor=CENTER, width=150)
my_tree.column("Last Name", anchor=CENTER, width=150)
my_tree.column("Phone", anchor=CENTER, width=150)
my_tree.column("Email", anchor=CENTER, width=250)


# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("First Name", text="FIRST NAME", anchor=CENTER)
my_tree.heading("Last Name", text="LAST NAME", anchor=CENTER)
my_tree.heading("Phone", text="PHONE", anchor=CENTER)
my_tree.heading("Email", text="EMAIL", anchor=CENTER)


# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


# ADD ENTRY BOXES
data_frame = LabelFrame(root, text="  DETAILS  ")
data_frame.pack(fill="x", expand="yes", padx=20)

id_label = Label(data_frame, text="  ID :")
id_label.grid(row=0, column=0, padx=10, pady=10,sticky=E)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=1, padx=10, pady=10,sticky=W)

fn_label = Label(data_frame, text="  FIRST NAME :")
fn_label.grid(row=0, column=2, padx=10, pady=10,sticky=E)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=3, padx=10, pady=10,sticky=W)

ln_label = Label(data_frame, text="LAST NAME :")
ln_label.grid(row=0, column=4, padx=5, pady=10,sticky=E)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=5, padx=10, pady=10,sticky=W)

phone_label = Label(data_frame, text="  PHONE :")
phone_label.grid(row=1, column=1, padx=15, pady=10,sticky=E)
phone_entry = Entry(data_frame)
phone_entry.grid(row=1, column=2, padx=10, pady=10,sticky=W)

email_label = Label(data_frame, text="  EMAIL :")
email_label.grid(row=1, column=3, padx=10, pady=10,sticky=E)
email_entry = Entry(data_frame)
email_entry.grid(row=1, column=4,ipadx=7, padx=10, pady=10,sticky=W)

#####

# DEFINING THE BUTTONS


# ADD CONATCT
def add_contact():
        # Connecting to the database
        conn = sqlite3.connect('contact_m.db')
        # Creating a cursor instance
        c = conn.cursor()
        
##        fn_var    =  fn_entry.get(),
##        ln_var    = ln_entry.get(),
##        phone_var =  phone_entry.get(),
##        email_var =  email_entry.get(),
##        oid_var   =  id_entry.get()  
##
##        if fn_var=='' or ln_var==''or phone_var=='' or email_var==''or oid_var=='':
##                messagebox.showinfo("Warning!","fields cannot be empty")
        
        # add new contact 
        c.execute("INSERT INTO contacts VALUES (:first, :last, :phone, :email)",                     
        {
                'first' :  fn_entry.get(),
                'last'  :  ln_entry.get(),
                'phone' :  phone_entry.get(),
                'email' :  email_entry.get(),
                'oid'   :  id_entry.get()                                            
        })        

        # Commit the changes
        conn.commit()
        # updating the view
        my_tree.delete(*my_tree.get_children())
        # to get the data from database
        query_database()        
        # Closing the connection
        conn.close()
        clear_all()
        # message box
        messagebox.showinfo("ADDED","New contact is added !")

# TO CLEAR ENTRY
def clear_all():
        id_entry.delete(0, END)
        fn_entry.delete(0, END)
        ln_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)

# Selecting by click
def select_contact(e):  # An Event is passed - optional (e)
        # first we should clear all of them
        clear_all()

        # get contact with the help of ID
        selected = my_tree.focus()
        # getting the values
        values = my_tree.item(selected,'values')

        # gets to entry boxes
        id_entry.insert(0, values[0])
        fn_entry.insert(0, values[1])
        ln_entry.insert(0, values[2])
        phone_entry.insert(0, values[3])
        email_entry.insert(0, values[4])

# BINDING THE TREEVIEW
my_tree.bind("<ButtonRelease-1>",select_contact)


# TO MOVE UP
def up():
        rows = my_tree.selection()
        for row in rows:
                my_tree.move(row,my_tree.parent(row), my_tree.index(row)-1)
                             
# TO MOVE DOWN
def down():
        rows = my_tree.selection()
        for row in reversed(rows):
                my_tree.move(row,my_tree.parent(row), my_tree.index(row)+1)
        

# TO REMOVE CONTACT
def remove_contact():
        x = my_tree.selection()
        for contact in x:
                my_tree.delete(contact)

        # Connecting to the database
        conn = sqlite3.connect('contact_m.db')
        # Creating a cursor instance
        c = conn.cursor()

        # deleting from database
        c.execute("DELETE FROM contacts WHERE oid="+id_entry.get())
        
        # Commit the changes
        conn.commit()
        # Closing the connection
        conn.close()
        clear_all()

        # message box
        messagebox.showinfo("DELETED", "Your contact has been deleted !")


# TO REMOVE ALL CONTACTS
def remove_all():
        # a little pop-up
        # message box
        response = messagebox.askyesno("DELETE !","All contacts will be deleted !\n are you sure?")
        if response==1:
                for contact in my_tree.get_children():
                        my_tree.delete(contact)

                # Connecting to the database
                conn = sqlite3.connect('contact_m.db')
                # Creating a cursor instance
                c = conn.cursor()

                # delete everything from table
                c.execute("DROP TABLE contacts")
                

                # Commit the changes
                conn.commit()
                # Closing the connection
                conn.close()
                clear_all()

                # adding new values
                creating_the_table()

# UPDATE CONTACT
def update_contact():
        # get the contact
        selected = my_tree.focus()
        # updating it
        my_tree.item(selected, text="", values=(id_entry.get(),fn_entry.get(),ln_entry.get(),phone_entry.get(),email_entry.get(),))      

        # We should update the database as well
        # Connecting to the database
        conn = sqlite3.connect('contact_m.db')
        # Creating a cursor instance
        c = conn.cursor()

        c.execute("""UPDATE contacts SET
                fname = :first,
                lname = :last,
                phone = :phone,
                email = :email

                WHERE oid = :oid""",
                {
                        'first' :  fn_entry.get(),
                        'last'  :  ln_entry.get(),
                        'phone' : phone_entry.get(),
                        'email' : email_entry.get(),
                        'oid'   : id_entry.get()
                })
        
        # Commit the changes
        conn.commit()
        # Closing the connection
        conn.close()
        clear_all()

        # message box
        messagebox.showinfo("UPDATED","Your contact is updated !")

def creating_the_table():
        conn = sqlite3.connect('contact_m.db')

        # Creating a cursor instance
        c = conn.cursor()

        # Creating a Table
        c.execute(""" CREATE TABLE if not exists contacts(
                fname text,
                lname text,
                phone text,
                email text)
        """)
        # Add some data
        '''
        for contact in data:
                c.execute("INSERT INTO contacts VALUES (:fname, :lname, :phone, :email)",
                        {
                         'fname': contact[1],
                         'lname': contact[2],
                         'phone': contact[3],
                         'email': contact[4]
                        }                
                )
        '''
        # Commit the changes
        conn.commit()
        # Closing the connection
        conn.close()

        
#####

# ADDING BUTTONS (POSITIONING)
button_frame = LabelFrame(root, text=" OPERATIONS " )
button_frame.pack(fill="x", expand="yes", padx=20)
##
add_button = Button(button_frame,text="ADD CONTACT", command= add_contact)
add_button.grid(row=0, column=0, padx=45, pady=10)
move_down_button = Button(button_frame, text="CLEAR", command=clear_all)
move_down_button.grid(row=1, column=0, padx=35, pady=10,ipadx = 24)
##
update_button = Button(button_frame, text="REMOVE",  command=remove_contact)
update_button.grid(row=0, column=5, padx=0, pady=10,ipadx = 22)

##search_button = Button(button_frame, text="SEARCH",  command= results)
##search_button.grid(row=0, column=4, padx=0, pady=10,ipadx = 22)

remove_all_button = Button(button_frame, text="UPDATE", command = update_contact)
remove_all_button.grid(row=0, column=3, padx=10, pady=10,ipadx = 22)
##
move_up_button = Button(button_frame, text="MOVE UP", command=up)
move_up_button.grid(row=1, column=3, padx=60, pady=10,ipadx = 18)
move_down_button = Button(button_frame, text="MOVE DOWN", command=down)
move_down_button.grid(row=1, column=5, padx=45, pady=10,ipadx = 8)
##
remove_one_button = Button(button_frame, text="REMOVE ALL" , command=remove_all)
remove_one_button.grid(row=0, column=7, padx=45, pady=10,ipadx = 10)
# END OF BUTTONS


# Testing
query_database()

root.mainloop()
