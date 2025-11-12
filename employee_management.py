import sqlite3

# Connect to database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    department TEXT
)
''')

# Add new employee
def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    dept = input("Enter Department: ")
    try:
        cursor.execute("INSERT INTO employees VALUES (?, ?, ?, ?)", (emp_id, name, email, dept))
        conn.commit()
        print("✅ Employee added successfully!\n")
    except sqlite3.IntegrityError:
        print("⚠️ Employee ID or Email already exists.\n")

# View all employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print()

# Update employee record
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    new_dept = input("Enter new Department: ")
    cursor.execute("UPDATE employees SET department=? WHERE emp_id=?", (new_dept, emp_id))
    conn.commit()
    print("✅ Employee updated successfully!\n")

# Delete employee
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
    conn.commit()
    print("🗑️ Employee deleted successfully!\n")

# Menu
while True:
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice! Try again.\n")

conn.close()
