import mysql.connector as sql
conn = sql.connect(host="localhost", user="root", passwd="root@123", database="the_royal_bank")
mycursor = conn.cursor() #creating cursor object 'mycursor'.

import datetime as dt #importing 'datetime' module as dt (alias name).

conn.autocommit = True
choice = 'y'
while choice == 'y': #entire program runs in a infinit loop unless and untile 'choice' is changed to "n/N"
    
    print() #menu
    print("Please select the type of operation - ")
    print()
    print("Enter 1 to CREATE A NEW BANK ACCOUNT. ")
    print("Enter 2 for TRANSACTIONS. ")
    print("Enter 3 to UPDATE DETAILS. ")
    print("Enter 4 to view CUSTOMER DETAILS. ")
    print("Enter 5 to view TRANSACTION MADE. ")
    print("Enter 6 to view CHANGES MADE. ")
    print("Enter 7 to DELETE ACCOUNT. ")
    print("Enter 8 to QUIT. ")
    print()

    n = input("Enter your choice [1-8]: ") #inputting user's choice 
    print()

    if n == "1":
        
        print("CREATE A BANK ACCOUNT")
        print()
        acc_no = input("Enter your desired 8 digit account number: ") #user inputs his/her desired 8 digit account number.
        if acc_no.isdigit(): #this block check whether user have inputted only digits or some other charecters.
            an_len=len(acc_no)
            if an_len == 8: #this block checks whether the account number is only of 8 digits or not
                print("Valid format for account number.")
                print()
            elif an_len < 8:
                print()
                print("The number of digits in the account number is less than 8.")
                print("Please retry.")
                break #breaks the while loop if 'an_len' is less than 8 digits.
            elif an_len > 8:
                print()
                print("The number of digit in the account number is more than 8.")
                print("Please retry.")
                break #breaks the while loop if 'an_len' is more than 8 digits.
            else:
                print()
                print("Please retry.")
                break
        else: #this block runs if user inputs alphabets or special characters in account number.
            print()
            print("Please retry using numbers [0-9]")
            print("Please retry.")
            break
        
        name = input("Enter your first name: ") #user inputs his first name.
        acc_name = name.upper() #all alphabets are capitalized using 'upper()'.
        if acc_name.isalpha(): #checks whether name contains only alphabaets or anything else.
            print("Valid name format.")
            print()
        else:
            print()
            print("Please retry, using alphabets [A-Z]/[a-z]")
            break
        
        cit = input("Enter your city: ") #user inputs his city.
        city = cit.upper() #all alphabets are capitalized using 'upper()'.
        if city.isalpha(): #checks whether city contains only alphabaets or anything else.
            print("Valid city format.")
            print()
        else:
            print()
            print("Please retry, using alphabets [A-Z]/[a-z]")
            break
            
        p_no = input("Enter your 10 digit phone number: ") #user inputs phone number.
        if p_no.isdigit(): #check whether phone number contains only digit or not.
            pn_len=len(p_no)
            if pn_len == 10: #checks whether phone number only contains 10 digit not more or less.
                print("Valid format for phone number.")
                print()
            elif pn_len < 10:
                print()
                print("The number of digits in the phone number is less than 10.")
                print("Please retry.")
                break
            elif pn_len > 10:
                print()
                print("The number of digits in the phone number is more than 10.")
                print("Please retry.")
                break
            else:
                print()
                print("Please retry.")
        else:
            print()
            print("Please retry using numbers [0-9]")
            print("Please retry.")
            break
        
        dob = input("Enter your Date of Birth in the format YYYY-MM-DD: ") #user inputs dob in same format as in mysql
        try:
            dob_sql = dt.datetime.strptime(dob, "%Y-%m-%d") 
            print("Valid date format")
            print()
        except ValueError as ve: #this block runs if user inputs wrong format.
            print()
            print("Error: ", ve)
            print("Wrong date format, please retry.")
                
        print("Please enter your gender - ")
        print() #menu for inputing gender.
        print("Enter M for MALE")
        print("Enter F for FEMALE")
        print("Enter O for OTHER")
        print()
        gen = input("Enter your gender [M/F/O]: ")
        gender = gen.upper()
        if gender.isalpha():
            if gender == "M":
                print("Gender: Male")
            elif gender == "F":
                print("Gender: Female")
            elif gender == "O":
                print("Gender: Other")
            else:
                print("Error, enter a valid choice [M/F/O]")
                print("Please retry.")
                break
        else:
            print("Error, enter a valid choice [M/F/O]")
            print("Please retry.")
            break   
        print()
        
        e = input("Enter your valid email address: ") #user inputs email.
        email = e.lower()
        if "@" and "." in email: #email must contain '@' and '.' to be in valid format.
            print("Valid email format.")
            print()
        else:
            print()
            print("Error, please retry using correct email address.")
            break
        
        print("Please enter your account type - ")
        print() #menu for account type.
        print("Enter C for CURRENT ACCOUNT")
        print("Enter S for SAVINGS ACCOUNT")
        print()
        typ = input("Enter your account type [C/S]: ")
        acc_type = typ.upper()
        if acc_type.isalpha():
            if acc_type == "C":
                print("Account type: Current")
            elif acc_type == "S":
                print("Account type: Savings")
            else:
                print("Error, enter a valid choice [C/S]")
                print("Please retry.")
                break
        print()
        
        print("Minimum amount for opening a CURRENT ACCOUNT is 10000")
        print("Minimum amount for opening a SAVINGS ACCOUNT is 500")
        print()
        balance = float(input("Enter opening balance: ")) #user enters base amount.
        if acc_type == "C" and balance >= 10000:
            print("Valid amount")
        elif acc_type == "S" and balance >= 500:
            print("Valid amount")
        else:
            print("Please retry")
            break
        print()

        SQL_cmd = "INSERT INTO customer_details(Account_Number, Account_Name, City, Phone_no, DOB, Gender, Email, Account_Type, Initial_Amount)\
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)" #sql query to insert data in the 'customer_details' table.
        val = (acc_no, acc_name, city, p_no, dob, gender, email, acc_type, balance)

        try:
            mycursor.execute(SQL_cmd,val) #query executed.
            conn.commit()
            print("Account Created Succesfully.")
            break
        except sql.Error as err: #except block to prevent unkown errors.
            print()
            print("Error: ", err)
            print("Account number", "'", acc_no, "'", "already taken, please retry using a different account number.")
            break
        
    elif n == "2":
        
        print("TRANSACTIONS") #transaction menu to withdraw or deposit money.
        print()
        acc_no = input("Enter your account number: ") #user inputs his/her account number.
        if acc_no.isdigit(): #checks if the inputted account number contains only digits or not.
            an_len=len(acc_no)
            if an_len == 8: #this block checks whether the account number is only of 8 digits or not
                print("Valid format for account number.")
                print()
            elif an_len < 8:
                print()
                print("The number of digits in the account number is less than 8.")
                print("Please retry.")
                break
            elif an_len > 8:
                print()
                print("The number of digit in the account number is more than 8.")
                print("Please retry.")
                break
            else:
                print()
                print("Please retry.")
                break
        else:
            print("Please retry using numbers [0-9]")
            print("Please retry.")
            break
        
        name = input("Enter your first name: ") #user inputs his/her first name.
        acc_name = name.upper()
        if acc_name.isalpha(): #checks if the name contains anything else except alphabts.
            print("Valid name format.")
            print()
        else:
            print()
            print("Please retry, using alphabets [A-Z]/[a-z]")
            break
            
        SQL_cmd1 = "SELECT * FROM customer_details WHERE Account_Number = %s AND Account_Name = %s" #select query to check whether the inpuuted values exist in the 'customer_details' table
        values1 = (acc_no, acc_name)
        mycursor.execute(SQL_cmd1, values1)
        
        if mycursor.fetchone() is  None: #if there is no data then this block runs
            print("Invalid account number or name." )
            print("Please retry using correct account number or name.")
            break
        else: #else, this block runs  
            print("Please select your operation - ")
            print()
            print("Enter 1 to WITHDRAW MONEY")
            print("Enter 2 to DEPOSIT MONEY")
            print()
            tr = input("Enter your choice [1/2]: ") #user inputs his choice to withdraw or to deposit money.
            print()
            if tr.isdigit():
                if tr == "1": #user wants to withdraw money.
                    with_amt = input("Enter amount to be withdrawl: ")
                    if with_amt.isdigit(): #checks whether user inputs digits or not.
                        print("Valid amount format.")
                        print()
                    else:
                        print()
                        print("Please retry using numbers [0-9]")
                        break
                    
                    try:
                        SQL_cmd2 = "UPDATE customer_details SET Initial_Amount = Initial_Amount - %s WHERE Account_Number = %s" #updates table 'customer_details' and its initial amount.
                        values2 = (with_amt, acc_no) 
                        mycursor.execute(SQL_cmd2, values2)
                        SQL_cmd3 = "INSERT INTO transactions(Account_Number, Date, Withdrawal_Amount, Amount_Deposited) VALUES(%s, %s, %s, %s)" #insert the transaction details in 'transactions' table to save records.            
                        dat = dt.datetime.today()
                        amt_dep = 0
                        values3 = (acc_no, dat, with_amt, amt_dep)
                        mycursor.execute(SQL_cmd3, values3)
                        conn.commit()
                        print("Amount withdrawn successfully.")
                        break
                    except sql.Error as err:
                        print()
                        print("Error: ", err)
                        break
                    
                elif tr == "2": #user wants deposit money
                    amt_dep = input("Enter amount to be deposited: ")
                    if amt_dep.isdigit():
                        print("Valid amount format.")
                        print()
                    else:
                        print()
                        print("Please retry using numbers [0-9]")
                        break

                    try:
                        SQL_cmd4 = "UPDATE customer_details SET Initial_Amount = Initial_Amount + %s WHERE Account_Number = %s" #updates table 'customer_details' and its initial amount.
                        values4 = (amt_dep, acc_no)
                        mycursor.execute(SQL_cmd4, values4)
                        
                        SQL_cmd5 = "INSERT INTO transactions(Account_Number, Date, Withdrawal_Amount, Amount_Deposited) VALUES(%s, %s, %s, %s)" #insert the transaction details in 'transactions' table to save records.
                        dat = dt.datetime.today()
                        with_amt = 0
                        values5 = (acc_no, dat, with_amt, amt_dep)
                        mycursor.execute(SQL_cmd5, values5)
                        conn.commit()
                        print("Account deposited succesfully.")
                        break
                    
                    except sql.Error as err:
                        print()
                        print("Error: ", err)
                        break
                else:
                    print()
                    print("Invalid operation: ", tr)
                    print("Please retry using [1/2]")
                    break

    elif n == "3":
        
        print("UPDATE YOUR DETAILS") #user wants update is account info.
        print()
        acc_no = input("Enter your account number: ") #user inputs acc_no 
        if acc_no.isdigit(): #checks whether acc_no is of 8 digits only.
            an_len=len(acc_no)
            if an_len == 8:
                print("Valid format for account number.")
                print()
            elif an_len < 8:
                print()
                print("The number of digits in the account number is less than 8.")
                print("Please retry.")
                break
            elif an_len > 8:
                print()
                print("The number of digit in the account number is more than 8.")
                print("Please retry.")
                break
            else:
                print()
                print("Please retry.")
                break
        else:
            print("Please retry using numbers [0-9]")
            print("Please retry.")
            break
        
        name = input("Enter your first name: ") #user inputs his/her name.
        acc_name = name.upper()
        if acc_name.isalpha():
            print("Valid name format.")
            print()
        else:
            print()
            print("Please retry, using alphabets [A-Z]/[a-z]")
            break
            
        SQL_cmd1 = "SELECT * FROM customer_details WHERE Account_Number = %s AND Account_Name = %s" #select query to display records of cutomer_details.
        values1 = (acc_no, acc_name)
        mycursor.execute(SQL_cmd1, values1)
        
        if mycursor.fetchone() is  None: #if there is no data in customer_details this block will run.
            print("Invalid account number or name." )
            print("Please retry using correct account number or name.")
            break
        else: #if select statement displays any record then this block will run
            SQL_cmd1 = "SELECT * FROM customer_details WHERE Account_Number = %s AND Account_Name = %s" #select query to display records of cutomer_details.
            values1 = (acc_no, acc_name)
            mycursor.execute(SQL_cmd1, values1)
            data=mycursor.fetchall() #saving all the required records in 'data'.
            for row in data: #for loop to print records
                print("OLD CITY: ", row[2])
                print("OLD PHONE NUMBER: ", row[3])
                print("OLD EMAIL ADDRESS: ", row[6])
                print()
                
            print("Please select your operation - ")
            print() #menu
            print("Enter 1 to change your CITY")
            print("Enter 2 to change your PHONE NUMBER")
            print("Enter 3 to change your EMAIL ADDRESS")
            print()
            ch = input("Enter your choice [1-3]: ") #user inputs his/her choice.
            print()
            if ch.isdigit():
                if ch == "1": #1 to change his/her city name
                    n_cit = input("Enter your new city: ")
                    new_city = n_cit.upper() #converts n_cit to uppercase
                    if new_city.isalpha(): #checks whether new_city contains only alphabets or not.
                        print("Valid city format.")
                        print()
                    else:
                        print()
                        print("Please retry, using alphabets [A-Z]/[a-z]")
                        break
                    try:
                        SQL_cmd2 = "UPDATE customer_details SET City = %s WHERE Account_Number = %s" #update query to update customer_details.
                        value2 = (new_city, acc_no)
                        mycursor.execute(SQL_cmd2, value2)

                        SQL_cmd3 = "INSERT INTO change_table(Account_Number, Date, Old, New) VALUES(%s, %s, %s, %s)" #inserting changes made into change_table for storing changes.
                        dat = dt.datetime.today()
                        old_city = row[2]
                        value3 = (acc_no, dat, old_city, new_city)
                        mycursor.execute(SQL_cmd3, value3)
                        conn.commit()
                        print("Account updated succesfully.")
                        break
                    except sql.Error as err:
                        print()
                        print("Error: ", err)
                        break

                elif ch == "2": #2 to change his/her phone_number.
                    new_pno = input("Enter your phone number: ")
                    if new_pno.isdigit(): #checks whether new_pno contains only digits.
                        pn_len=len(new_pno)
                        if pn_len == 10: #checks length of phone number.
                            print("Valid format for phone number.")
                            print()
                        elif pn_len < 10:
                            print()
                            print("The number of digits in the phone number is less than 10.")
                            print("Please retry.")
                            break
                        elif pn_len > 10:
                            print()
                            print("The number of digits in the phone number is more than 10.")
                            print("Please retry.")
                            break
                        else:
                            print()
                            print("Please retry.")
                    else:
                        print()
                        print("Please retry using numbers [0-9]")
                        print("Please retry.")
                        break
                    try:
                        SQL_cmd2 = "UPDATE customer_details SET Phone_no = %s WHERE Account_Number = %s" #update query to update customer_details.
                        value2 = (new_pno, acc_no)
                        mycursor.execute(SQL_cmd2, value2)

                        SQL_cmd3 = "INSERT INTO change_table(Account_Number, Date, Old, New) VALUES(%s, %s, %s, %s)" #inserting changes made into change_table for storing changes.
                        dat = dt.datetime.today()
                        old_pno = row[3]
                        value3 = (acc_no, dat, old_pno, new_pno)
                        mycursor.execute(SQL_cmd3, value3)
                        conn.commit()
                        print("Account updated succesfully.")
                        break
                    except sql.Error as err:
                        print()
                        print("Error: ", err)
                        break
                        
                elif ch == "3": #3 to change email address.
                    n_em = input("Enter new email address: ")
                    new_email = n_em.lower()
                    if "@" and "." in new_email:
                        print("Valid email format.")
                        print()
                    else:
                        print()
                        print("Error, please retry using correct email address.")
                        break
                    try:
                        SQL_cmd2 = "UPDATE customer_details SET Email = %s WHERE Account_Number = %s" #update query to update customer_details.
                        value2 = (new_email, acc_no)
                        mycursor.execute(SQL_cmd2, value2)

                        SQL_cmd3 = "INSERT INTO change_table(Account_Number, Date, Old, New) VALUES(%s, %s, %s, %s)" #inserting changes made into change_table for storing changes.
                        dat = dt.datetime.today()
                        old_email = row[6]
                        value3 = (acc_no, dat, old_email, new_email)
                        mycursor.execute(SQL_cmd3, value3)
                        conn.commit()
                        print("Account updated succesfully.")
                        break
                    except sql.Error as err:
                        print()
                        print("Error: ", err)
                        break
                        
    elif n == "4":
        
        print("VIEW YOUR ACCOUNT DETAILS") #user wants view his details
        print()
        acc_no = input("Enter your account number: ") #user input his/her account number.
        if acc_no.isdigit():
            an_len=len(acc_no)
            if an_len == 8:
                print("Valid format for account number.")
                print()
            elif an_len < 8:
                print()
                print("The number of digits in the account number is less than 8.")
                print("Please retry.")
                break
            elif an_len > 8:
                print()
                print("The number of digit in the account number is more than 8.")
                print("Please retry.")
                break
            else:
                print()
                print("Please retry.")
                break
        else:
            print("Please retry using numbers [0-9]")
            print("Please retry.")
            break
        
        name = input("Enter your first name: ") #user inputs his/her name.
        acc_name = name.upper()
        if acc_name.isalpha():
            print("Valid name format.")
            print()
        else:
            print()
            print("Please retry, using alphabets [A-Z]/[a-z]")
            break
        
        SQL_cmd1 = "SELECT * FROM customer_details WHERE Account_Number = %s AND Account_Name = %s" #select query to display records from customer_details.
        values1 = (acc_no, acc_name)
        mycursor.execute(SQL_cmd1, values1)
        
        if mycursor.fetchone() is  None: #if no data is found this block runs.
            print("Invalid account number or name." )
            print("Please retry using correct account number or name.")
            break
        else: #else;
            SQL_cmd1 = "SELECT * FROM customer_details WHERE Account_Number = %s AND Account_Name = %s"
            values1 = (acc_no, acc_name)
            mycursor.execute(SQL_cmd1, values1)
            data=mycursor.fetchall() #records saved in data variable.
            for row in data: #for loop to print data
                print("Your information: ")
                print()
                print("Account Number: ", acc_no)
                print("Account Name: ", acc_name)
                print("City: ", row[2])
                print("Phone Number: ", row[3])
                print("Date of Birth YYYY-MM-DD: ", row[4])
                print("Gender: ", row[5])
                print("Email: ", row[6])
                print("Account Type: ", row[7])
                print("Balance: ₹", row[8])
            break

    elif n == "5":
        
        print("VIEW YOUR TRANSACTIONS") #transaction details 
        print()
        acc_no = input("Enter your account number: ") #user inputs his/her acc no.
        if acc_no.isdigit():
            an_len=len(acc_no)
            if an_len == 8:
                print("Valid format for account number.")
                print()
            elif an_len < 8:
                print()
                print("The number of digits in the account number is less than 8.")
                print("Please retry.")
                break
            elif an_len > 8:
                print()
                print("The number of digit in the account number is more than 8.")
                print("Please retry.")
                break
            else:
                print()
                print("Please retry.")
                break
        else:
            print("Please retry using numbers [0-9]")
            print("Please retry.")
            break
        
        name = input("Enter your first name: ") #user inputs his/her name.
        acc_name = name.upper()
        if acc_name.isalpha():
            print("Valid name format.")
            print()
        else:
            print()
            print("Please retry, using alphabets [A-Z]/[a-z]")
            break
        
        SQL_cmd1 = "SELECT * FROM customer_details WHERE Account_Number = %s AND Account_Name = %s" #select query to diplay records.
        values1 = (acc_no, acc_name)
        mycursor.execute(SQL_cmd1, values1)
        
        if mycursor.fetchone() is  None: #if select query displays no record this block will run
            print("Invalid account number or name." )
            print("Please retry using correct account number or name.")
            break
        else: #else
            SQL_cmd2 = "SELECT * FROM transactions WHERE Account_Number = %s"
            values2 = (acc_no,)
            mycursor.execute(SQL_cmd2, values2)
            data = mycursor.fetchall() #user records stored in 'data'.
            for row in data:
                print("Your information: ")
                print()
                print("Account Number: ", acc_no)
                print("Date: ", row[2])
                print("Amount Withdrawn: ", row[3])
                print("Amount Deposited: ", row[4])
                print()
            break
            
    elif n == "6":
        
        print("VIEW CHANGES MADE IN YOUR ACCOUNT") #changes made by the user.
        print()
        acc_no = input("Enter your account number: ") #user inputs his/her account number.
        if acc_no.isdigit():
            an_len=len(acc_no)
            if an_len == 8:
                print("Valid format for account number.")
                print()
            elif an_len < 8:
                print()
                print("The number of digits in the account number is less than 8.")
                print("Please retry.")
                break
            elif an_len > 8:
                print()
                print("The number of digit in the account number is more than 8.")
                print("Please retry.")
                break
            else:
                print()
                print("Please retry.")
                break
        else:
            print("Please retry using numbers [0-9]")
            print("Please retry.")
            break
        
        name = input("Enter your first name: ") #user inputs his/her name.
        acc_name = name.upper()
        if acc_name.isalpha():
            print("Valid name format.")
            print()
        else:
            print()
            print("Please retry, using alphabets [A-Z]/[a-z]")
            break
        
        SQL_cmd1 = "SELECT * FROM customer_details WHERE Account_Number = %s AND Account_Name = %s" #select query to diplaay records from customer_details
        values1 = (acc_no, acc_name)
        mycursor.execute(SQL_cmd1, values1)
        
        if mycursor.fetchone() is  None: #if select stmnt displays no recor this bloc will run.
            print("Invalid account number or name." )
            print("Please retry using correct account number or name.")
            break
        else: #elese
            SQL_cmd2 = "SELECT * FROM change_table WHERE Account_Number = %s"
            values2 = (acc_no,)
            mycursor.execute(SQL_cmd2, values2)
            data = mycursor.fetchall()
            for row in data: #printing data.
                print("Your information: ")
                print()
                print("Account Number: ", acc_no)
                print("Date: ", row[2])
                print("Old data [City/Phone Number/ Email]: ", row[3])
                print("New data [City/Phone Number/ Email]: ", row[4])
                print()
            break
        
    elif n == "7":
        
        print("ACCOUNT DELETION")
        print()
        acc_no = input("Enter your account number: ") #user inputs his/her name.
        if acc_no.isdigit():
            an_len=len(acc_no)
            if an_len == 8:
                print("Valid format for account number.")
                print()
            elif an_len < 8:
                print()
                print("The number of digits in the account number is less than 8.")
                print("Please retry.")
                break
            elif an_len > 8:
                print()
                print("The number of digit in the account number is more than 8.")
                print("Please retry.")
                break
            else:
                print()
                print("Please retry.")
                break
        else:
            print("Please retry using numbers [0-9]")
            print("Please retry.")
            break
        
        name = input("Enter your first name: ") #user inputs his/her name.
        acc_name = name.upper()
        if acc_name.isalpha():
            print("Valid name format.")
            print()
        else:
            print()
            print("Please retry, using alphabets [A-Z]/[a-z]")
            break
        
        SQL_cmd1 = "SELECT * FROM customer_details WHERE Account_Number = %s AND Account_Name = %s" #select query to display records
        values1 = (acc_no, acc_name)
        mycursor.execute(SQL_cmd1, values1)
        
        if mycursor.fetchone() is  None: #select query displays no record this block will run.
            print("Invalid account number or name." )
            print("Please retry using correct account number or name.")
            break
        else: #else.
            print("Are you sure you want to delete your account?")
            print("All your data will be lost permanently. ")
            yn = input("Enter your choice [Y/N]: ") #asking for final permission from the user.
            dele = yn.upper()
            if dele == "Y":
                SQL_cmd2 = "DELETE FROM customer_details WHERE Account_Number = %s AND Account_Name = %s" #delete query
                val2 = (acc_no, acc_name)
                mycursor.execute(SQL_cmd2, val2)

                SQL_cmd3 = "DELETE FROM transactions WHERE Account_Number = %s" #delete query
                val3 = (acc_no,)
                mycursor.execute(SQL_cmd3, val3)

                SQL_cmd4 = "DELETE FROM change_table WHERE Account_Number = %s" #delete query
                val4 = (acc_no,)
                mycursor.execute(SQL_cmd4, val4)

                print("Account deleted successfully. ")
                break
            
            elif dele == "N":
                print("Account not deleted. ")
                break

            else:
                print("Please retry, using [Y/N]")
                break
            
    elif n == "8": #if user wants to quit the program.

        print("Do you want continue [Y/N]")
        ch = input("Enter your choice: ")
        choice = ch.lower()

    else:
        
        print("Invalid operation: ", n)
        print("Please retry using [1-4]")
        break
else:
    print()
    print("Thank you, please visit again")
    quit()
