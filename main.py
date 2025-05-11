import psycopg2
import tkinter as tk


def create_table():
    conn = psycopg2.connect(dbname="project_psycopg", user="postgres", port="5432", password="qwaszxrainy")
    curr = conn.cursor()
    curr.execute('create table students(id serial primary key, name text, address text, age int, number text);')
    print("table created successfully")
    conn.commit()
    conn.close()

def insert_table():

    try:
        name = name_entry.get()
        address = address_entry.get()
        age = int(age_entry.get())
        number = number_entry.get()

        conn = psycopg2.connect(dbname="project_psycopg", user="postgres", port="5432", password="qwaszxrainy")
        curr = conn.cursor()
        # query = 
        curr.execute("insert into students (name, address, age, number) values(%s, %s, %s, %s)", (name, address, age, number))
        print("data inserted successfully")
        conn.commit()
        conn.close()

    except Exception as e:
        print(e)

# def update_data():

#     id = input("Enter ID of student you want to edit")
    

root = tk.Tk()

root.title("Student App")
root.geometry("400x400")

main_label = tk.Label(root, text="Enter Student Details")
main_label.grid(column=1)



name_label = tk.Label(root, text="Name: ")
name_entry = tk.Entry(root)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)

address_label = tk.Label(root, text="Address: ")
address_entry = tk.Entry(root)
address_label.grid(row=2, column=0)
address_entry.grid(row=2, column=1)

age_label = tk.Label(root, text="Age: ")
age_entry = tk.Entry(root)
age_label.grid(row=3, column=0)
age_entry.grid(row=3, column=1)

number_label = tk.Label(root, text="Number: ")
number_entry = tk.Entry(root)
number_label.grid(row=4, column=0)
number_entry.grid(row=4, column=1)


enter_button = tk.Button(root, text="ENTER", command=insert_table)
enter_button.grid(row=5, column=1)


root.mainloop()

