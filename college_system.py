# import mysql.connector as mysql
import sqlite3
connection = sqlite3.connect("./college.db")

# db = mysql.connect(host="localhost",user="root",password="",database="college")
command_handler = connection.cursor()

def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Register New Student")
            username = input(str("Student username : "))
            password = input(str("Student password : "))
            query_vals = (username,password)
            query = f"INSERT INTO users (username,password,privilege) VALUES ('{username}','{password}','student')"
            print(query)
            command_handler.execute(query)
            connection.commit()
            print(username + " has been registered as a student")
        
        elif user_option == "2":
            print("")
            print("Register New Teacher")
            username = input(str("Teacher username : "))
            password = input(str("Teacher password : "))
            query_vals = (username,password)
            command_handler.execute(f"INSERT INTO users (username,password,privilege) VALUES ('{username}','{password}','teacher')")
            connection.commit()
            print(username + " has been registered as a teacher")
    
        elif user_option == "3":
            print("")
            print("Delete Existing Student Account")
            username = input(str("Student username : "))
            query_vals = (username,"student")
            command_handler.execute(f"DELETE FROM users WHERE username = '{username}' AND privilege = 'student'")
            connection.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == "4":
            print("")
            print("Delete Existing Teacher Account")
            username = input(str("Teacher username : "))
            query_vals = (username,"teacher")
            command_handler.execute(f"DELETE FROM users WHERE username = '{username}' AND privilege = 'teacher'")
            connection.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == "5":
            break
        else:
            print("No valid option selected")


def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised") 

def main():
    # command_handler.execute("CREATE DATABASE IF NOT EXISTS COLLEGE;")
    command_handler.execute("CREATE TABLE IF NOT EXISTS users(username varchar(255), password varchar(255), privilege varchar(255))")
    connection.commit()
    while 1:
        print("Welcome to the college system")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("Student login")
        elif user_option == "2":
            print("Teacher login")
        elif user_option == "3":
            auth_admin()
        else:
            print("No valid option was selected")

main()
