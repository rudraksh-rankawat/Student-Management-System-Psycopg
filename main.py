import psycopg2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def insert_data():
    try:  
        parameters = (name_entry.get(),address_entry.get(), int(age_entry.get()), number_entry.get())
        query = "insert into students (name, address, age, number) values(%s, %s, %s, %s)"
        run_query(query, parameters)
        refresh_treeview()
        print("data inserted successfully")
        # messagebox.showinfo("data inserted successfully")
        
    except Exception as e:
        print(e)
        messagebox.showinfo(str(e))
        
def delete_data():
    
    selected_item = tree.selection()[0]
    student_id = tree.item(selected_item)['values'][0]
    
    query = "delete from students where id = (%s)"
    parameters = (student_id,)
    run_query(query, parameters)
    refresh_treeview()

def update_data():
    selected_item = tree.selection()[0]
    student_id = tree.item(selected_item)['values'][0]
    parameters = (name_entry.get(),address_entry.get(), int(age_entry.get()), number_entry.get() ,student_id)
    query = "update students set name = %s, address = %s, age = %s ,number = %s WHERE id=%s"
    run_query(query, parameters)
    refresh_treeview()
    
def create_db():
    query = "CREATE IF NOT EXISTS students(id serial primary key, name text, address text, age int, number text);"
    parameters = ()
    run_query(query, parameters)
    refresh_treeview()

def run_query(query, parameters=()):
    conn = psycopg2.connect(dbname="project_psycopg", user="postgres", port="5432", password="qwaszxrainy")
    curr = conn.cursor()
    try:
        curr.execute(query, parameters)
        query_result = None
        if query.lower().startswith("select"):
            query_result = curr.fetchall()
        conn.commit()    
    except psycopg2.Error as e:
        messagebox.showerror("Database Error", str(e))
        print("Database Error", str(e))
        
    finally:
        curr.close()
        conn.close()
        
    return query_result 

def refresh_treeview():
    for item in tree.get_children():
        tree.delete(item)
    records = run_query("select * from students;")
    print(type(records))
    for record in records:
        tree.insert('', "end", values=record)
    
#tkinter UI
root = tk.Tk()
root.title("Student App")
root.geometry("600x500")

# main_label = tk.Label(root, text="Enter Student Details")
# main_label.grid(column=1)


frame = tk.LabelFrame(root, text="Students", bd=2, relief="groove")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")


tk.Label(frame, text="Name: ").grid(row=1,column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=1, column=1)

address_label = tk.Label(frame, text="Address: ")
address_entry = tk.Entry(frame)
address_label.grid(row=2, column=0)
address_entry.grid(row=2, column=1)

age_label = tk.Label(frame, text="Age: ")
age_entry = tk.Entry(frame)
age_label.grid(row=3, column=0)
age_entry.grid(row=3, column=1)

number_label = tk.Label(frame, text="Number: ")
number_entry = tk.Entry(frame)
number_label.grid(row=4, column=0)
number_entry.grid(row=4, column=1)


button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, sticky="ew", pady=10)


tk.Button(button_frame, text="Create Table",command=create_db ).grid(row=0, column=0)
tk.Button(button_frame, text="Insert Data", command=insert_data).grid(row=0, column=1)
tk.Button(button_frame, text="Update Data", command=update_data).grid(row=0, column=2)
delete = tk.Button(button_frame, text="Delete Data", command=delete_data)
delete.grid(row=0, column=3)
root.bind('<Delete>', delete_data)



tree_frame = tk.Frame(root)
tree_frame.grid(row = 2, column=0)

tree_scrollbar = tk.Scrollbar(tree_frame)
tree_scrollbar.pack(side="right", fill="y")

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrollbar.set, selectmode="browse")
tree.pack()

tree_scrollbar.config(command=tree.yview)

tree["columns"] = ["student_id", "name", "address", "age", "number"]
tree.column("#0", width=0, stretch="NO")
tree.column("student_id", anchor="center", width=40)
tree.column("name", anchor="center", width=80)
tree.column("address", anchor="center", width=80)
tree.column("age", anchor="center", width=40)
tree.column("number", anchor="center", width=100)

tree.heading("student_id", anchor="center", text="ID")
tree.heading("name", anchor="center", text="Name")
tree.heading("address", anchor="center", text="Address")
tree.heading("age", anchor="center", text="Age")
tree.heading("number", anchor="center", text="Phone Number")



refresh_treeview()
root.mainloop()

