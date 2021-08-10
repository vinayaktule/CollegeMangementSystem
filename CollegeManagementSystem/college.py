import mysql.connector as mysql

try:
    db = mysql.connect(host="localhost",user="root",password="", database="college")
except Exception as e:
    print("Database not connected !!!")
command_handler = db.cursor(buffered=True)

def admin_session():
    print("\nWELCOME TO ADMIN ACCOUNT")
    print("*"*50)
    print("1.\t Register Student")
    print("2.\t Register Teacher")
    print("3.\t Delete Student")
    print("4.\t Delete Teacher")
    print("5.\t Logout")

    user_option = input(str("Option : " ))

    if user_option ==  "1":
        print("Register new Student")
        username = input(str("Student username\t"))
        password = input(str("Student password\t"))
        query_vals =  (username, password)

        command_handler.execute("INSERT INTO users (username, password, privilege) values (%s, %s, 'student')",query_vals)
        db.commit()
        print(f"{username} has been registered as student !!!\n")
    elif user_option == "2":
        print("Register new Teacher")
        username = input(str("Teacher username\t"))
        password = input(str("Teacher password\t"))
        query_vals =  (username, password)

        command_handler.execute("INSERT INTO users (username, password, privilege) values (%s, %s, 'teacher')",query_vals)
        db.commit()
        print(f"{username} has been registered as teacher !!!\n")

    elif user_option == "3":
        print("Delete existing Student")
        username = input(str("Student username to delete\t"))
        query_vals = (username, "student")
        command_handler.execute("DELETE FROM users where username = %s AND privilege = %s", query_vals)
        db.commit()
        if command_handler.rowcount<1:
            print(f"Sorry...{username} not found !!!")
        else:
            print(username, "User deleted successfully !!!")
    elif user_option == "4":
        print("Delete existing Teacher")
        username = input(str("Teacher username to delete\t"))
        query_vals = (username, "teacher")
        command_handler.execute("DELETE FROM users where username = %s AND privilege = %s", query_vals)
        db.commit()
        if command_handler.rowcount<1:
            print("Sorry...User not found !!!")
        else:
            print(f"{username} deleted successfully !!!")
    
    elif user_option=="5":
        exit()

    else:
        print("Enter correct option")

def auth_admin():
    print("WELCOME to ADMIN LOGIN PAGE !!!")
    username = input(str("Enter username\t"))
    password = input(str("Enter password\t"))
    
    if username.lower() == "admin" and password == "admin":
        admin_session()
    else:
        print("Incorrect username or password")

def main():
    while 1:
        print("*"*50)
        print("Welcome to college Management System")
        print("*"*50)
        print("1.\t Admin Login")
        print("2.\t Student Login")
        print("3.\t Teacher Login")
        print("4.\t Logout")

        user_option = input(str("Option :"))

        if user_option == '1':
            print("Admin Login")
            auth_admin()
        elif user_option == '2':
            print("Student Login")
        elif user_option == '3':
            print("Teacher Login")
        elif user_option == '4':
            print("Successfully logout from College Management System")
            exit()

        else:
            print("Enter valid option")

main()