import mysql.connector as sql
conn = sql.connect(host="localhost", user="root", passwd="root@123", database="the_royal_bank")
mycursor = conn.cursor() #creating cursor object: 'mycursor'.

print("========================================================== <<<<<<<<<<  WELCOME TO THE ROYAL BANK  >>>>>>>>>> ==========================================================")

import datetime as dt #importing 'datetime' module with alias name 'dt'.
print(dt.datetime.now()) #prints the date and time at which the program was execute with the help of 'datetime' module.
print()

choice = "y"
while choice == "y": #while loop runs until the choice is anything excepts 'y' or 'Y'.
    
    print() #menu for the user to login or register in the bank
    print("Please select the type of operation - ")
    print()
    print("Enter 1 to REGISTER")
    print("Enter 2 to LOGIN")
    print("Enter 3 to CHANGE Username/Password")
    print("Enter 4 to EXIT")
    print()

    try: #entire code in try block to avoid big error msgs that would scare the user
        n = int(input("Enter your choice [1-4]: ")) #inputting user choice for the above menu
        print()

        if n == 1: #new user can login if he don't have a account.
            
            username = input("Enter a Username: ") #user inputs his/her username.
            if username.isalnum(): #checks whether the username is alpha-numeric or not; if true pass
                print("Valid username format.")
                pass
            else: #if the username is not alpha-numeric it will break the while loop, hence stopping the code
                print()
                print("Error, enter a alpha-numeric username.")
                print("Please retry")
                break #breaks the while loop when an error is occured.
            
            print()
            password = int(input("Enter a numeric password: ")) #user inputs a numeric password
            print()
        
            SQL_cmd = "INSERT INTO user_table(Username,Password) VALUES(%s,%s)" #SQL cmd to insert 'username' and 'password' to 'user_table'.
            val = (username, password)
        
            try:
                mycursor.execute(SQL_cmd, val) #execute the sql cmd
                conn.commit()
                print("User registered successfully with bank.")
                print()
                print("Welcome", username, ",") 
                import menu #imports the 'menu' module which contains online banking system.
                break
            
            except sql.Error as err: #shows error if the username is already present in 'user_table' as it is the primary key in 'user-table'.
                print("Error:", err)
                print("Please retry.")
                break

        elif n == 2: 
            
            username = input("Enter your Username: ") #user inputs his/her username.
            if username.isalnum(): #checks whether the username is alpha-numeric or not; if true pass
                print("Valid username format.")
                pass
            else: #if the username is not alpha-numeric it will break the while loop, hence stopping the code
                print()
                print("Error, enter a alpha-numeric username.")
                print("Please retry")
                break #breaks the while loop when an error is occured.

            print()
            password = int(input("Enter your numeric password: ")) #user inputs his/her numeric password
            print()
    
            SQL_cmd = "SELECT * FROM user_table WHERE Username = %s AND Password = %s" #sql query to display records from 'user_table'.
            val = (username, password) #values which are needed for the 'SQL_cmd'.
            mycursor.execute(SQL_cmd, val) #executes the sql cmd.
        
            if mycursor.fetchone() is  None: #if the select query does not displays any data then this if block will run.
                print("No user found with username","'",username, "'", "or password","'",password,"'.")
                print("Invalid username or password")
                print("Please retry using your correct username or password.")
                break #breaks the while loop
            else:
                print("Welcome", username, ",")
                import menu #if the select query displays any data then the 'menu' module is imported
                break

        elif n == 3: #if the user wants to change his/her 'username' or 'password'
            print("Please select the type of operation - ") #menu
            print()
            print("Enter 1 to change USERNAME")
            print("Enter 2 to change PASSWORD")
            print()
            try:
                change = int(input("Enter your choice [1/2]: "))
                print()

                if change == 1: #if user wants to change his/her username.
                    username = input("Enter your old Username: ") #user inputs old username.
                    if username.isalnum(): #checks whether the username is alpha-numeric or not; if true pass
                        print("Valid username format.")
                        pass
                    else: #if the username is not alpha-numeric it will break the while loop, hence stopping the code
                        print()
                        print("Error, enter a alpha-numeric username.")
                        print("Please retry")
                        break #breaks the while loop when an error is occured.

                    print()
                    password = int(input("Enter your numeric password: ")) #user inputs his password
                    print()

                    SQL_cmd = "SELECT * FROM user_table WHERE Username = %s AND Password = %s" #sql query to display records from 'user_table'.
                    val = (username, password) #values for sql query
                    mycursor.execute(SQL_cmd,val) #executing the sql query

                    if mycursor.fetchone() is  None: #if the select query does not displays any data then this if block will run.
                        print("Invalid username or password")
                        print("Please retry using your correct username or password.")
                        break #breaks the while loop
                    else:
                        try:
                            new_username = input("Enter your new username: ") #else, user inputs new username.
                            if new_username.isalnum(): #check whether the new username is alpha-numeric or not.
                                print("Valid username format.")
                                print()
                                if new_username == username: #if the old username = new username the the while loops break
                                    print("The new username is same as the old username.")
                                    break #breaks the while loop
                                else:
                                    SQL_cmd1 = "UPDATE user_table SET Username = %s WHERE Password = %s" #sql query to update the username in 'user_table'.
                                    new_val1 = (new_username, password)
                                
                                    try:
                                        mycursor.execute(SQL_cmd1, new_val1) #executing the sql query.
                                        conn.commit()
                                        print("Username updated from","'",username,"' to ", "'", new_username, "'")
                                        break #breaks the while loop as the username is change.
                                    except sql.Error as err: #this block runs if the new username is already present in the 'user_table'.
                                        print("Error:", err)
                                        print("Username", "'", new_username, "'", "already taken, please retry using a different username.")
                                        break #breaks the while loop
                            else: #this block runs if the new username contains anything else except numbers or alphabets
                                print()
                                print("Error, enter a alpha-numeric username.")
                                print("Please retry")
                                break
                                
                        except ValueError as ve: #this block runs if password entered by the user is not 'int'.
                            print()
                            print("Error:",ve)
                            print("Please retry using numbers [0-9]")
                            break
                        
                elif change == 2: #if the user wants to change his/her password.
                    username = input("Enter your Username: ") #user inputs the username.
                    if username.isalnum(): #checks whether the username is alpha-numeric or not; if true pass
                        print("Valid username format.")
                        pass
                    else: #if the username is not alpha-numeric it will break the while loop, hence stopping the code
                        print()
                        print("Error, enter a alpha-numeric username.")
                        print("Please retry")
                        break #breaks the while loop when an error is occured.

                    print()
                    password = int(input("Enter your old numeric password: ")) #user inputs the old password.
                    print()

                    SQL_cmd = "SELECT * FROM user_table WHERE Username = %s AND Password = %s" #sql query to display records from 'user_table'.
                    val = (username, password) #values for sql query
                    mycursor.execute(SQL_cmd,val) #executing the sql query

                    if mycursor.fetchone() is None: #if the select query does not displays any data then this if block will run.
                        print("Invalid username or password")
                        print("Please retry using your correct username or password.")
                        break #breaks the while loop.
                    else:
                        try:
                            new_password = int(input("Enter your new numeric password: ")) #user inputs new password.
                            if new_password == password: #checks whether the new password is same as old password
                                print("The new password is same as the old password.")
                                break #breaks the while loop if new password is same as old password 
                            else:
                                SQL_cmd2 = "UPDATE user_table SET Password = %s WHERE Username = %s" #sql query to update 'user_table'.
                                new_val2 = (new_password, username)
                                try:
                                    mycursor.execute(SQL_cmd2, new_val2)#executes the sql query
                                    conn.commit()
                                    print("Password updated from","'",password,"' to","'", new_password, "'")
                                    break
                                except sql.Error as err:
                                    print("Error:", err)
                                    break
                        except ValueError as ve: #this block runs if password entered by the user is not 'int',
                            print()
                            print("Error:",ve)
                            print("Please retry using numbers [0-9]")
                            break
                else: #this block runs if user inputs wrong choice in changing username or password.
                    print("Invalid operation: ", change)
                    print("Error, please retry using [1/2]")
                    break
                
            except ValueError as ve: #this block runs if the correct value in the 'change' variable is not inputted by the user.
                print()
                print("Error:",ve)
                print("Please retry using numbers [0-9]")
                break
        
                    
                
        elif n == 4: #if the user wants to quit.
            
            print("Do you want continue [Y/N]")
            ch = input("Enter your choice: ")
            choice = ch.lower()
              
        else: #this block runs if the correct value in the 'n' variable is not inputted by the user. 
            
            print("Invalid operation: ", n)
            print("Please retry using [1-4]")
            break

    except ValueError as ve: #this block runs if 'n' not a 'int' based operation inputted by user.
        print()
        print("Error:",ve)
        print("Please retry using numbers [0-9]")
        break

else:
    print()
    print("Thank you, please visit again")
    quit() #quits python.
    
