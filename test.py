
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
    
    
    
    