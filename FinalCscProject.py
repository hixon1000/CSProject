import mysql.connector as mysql
import time
import datetime
from tabulate import tabulate

class project:
    def __init__(self):
        self.password=['tiger']
        #password trial
        while True:
            try:
                paswd=str(input('Enter password: '))
                if paswd==self.password[0]:
                    pass
                else:
                    raise ValueError
            except ValueError:
                print('Access Denied...Try Again')
            else:
                print('Access Granted')
                break
        print()
        print('Connecting...')
        time.sleep(5)
        #Create the connectivity and necessary tables
        self.myconnect=mysql.connect(host='localhost',user='root',passwd=self.password[0])
        x=self.myconnect.is_connected()
        if x == True:
            print('Connection Established')
        else:
            print('Connection Failed')
        self.mycursor=self.myconnect.cursor()
        self.mycursor.execute('create database if not exists city_library')
        self.mycursor.execute('use city_library')
        self.mycursor.execute("create table if not exists employee_details(emp_id int(4) not null primary key, name varchar(30) not null, age int(2), occupation varchar(20), date_of_joining date, contact_info char(12), salary int(5))")
        self.mycursor.execute("create table if not exists book_details(book_id int(4) not null primary key, name varchar(30) not null, author varchar(30), publisher varchar(20), date_of_purchase date,cost_of_purchase int(5),copies int(2))")
        self.mycursor.execute("create table if not exists purchase_rent_details(sl_no int(4) not null primary key, name varchar(30) not null, contact_info char(12), address varchar(40), status varchar(10), date_of_rent_or_purchase date, cost_of_rent_or_purchase int(5), date_of_return date null, Book_id int(4) references book_details(book_id), User_id int default null references user_details(user_id))")
        self.mycursor.execute("create table if not exists user_details(user_id int not null primary key, user_name varchar(30), username varchar(20) not null unique, password varchar(20) not null)")

    #creating functions for library management system

    def userid(self):
        self.mycursor.execute('select count(*) from user_details')
        count=self.mycursor.fetchone()[0]
        return int(count)

    def emp_id(self):
        self.mycursor.execute('select count(*) from employee_details')
        count=self.mycursor.fetchone()[0]
        return int(count)

    def book_id(self):
        self.mycursor.execute('select count(*) from book_details')
        count=self.mycursor.fetchone()[0]
        return int(count)

    def purchase_id(self):
        self.mycursor.execute('select count(*) from purchase_rent_details')
        count=self.mycursor.fetchone()[0]
        return int(count)

    def registration(self,name,username,password):
        count=self.userid()
        self.mycursor.execute("insert into user_details values({},'{}','{}','{}')".format(count+1,name,username,password))
        self.myconnect.commit()
        print('Record added')

    def signin(self,username,password):
        self.mycursor.execute("select password from user_details where username='%s'"%(username))
        record=self.mycursor.fetchall()
        print(record)
        return bool(record[0][0]==password)
    def force_int(self, string :str):
        while True:
            try:
                return int(input(string))
            except ValueError:
                print("Invalid Value")
    def force_date(self, string :str):
        while True:
            try:
                return str(datetime.datetime.strptime(input(string), "%Y-%m-%d").date())
            except ValueError:
                print("Invalid Date Format (yyyy-mm-dd)")
    def get_book_id(self, name):
        self.mycursor.execute("select book_id from book_details where name='{0}'".format(name))
        return int(self.mycursor.fetchone[0])
    def get_user_id(self, name):
        self.mycursor.execute("select user_id from user_details where name='{0}'".format(name))
        return int(self.mycursor.fetchone[0])
    #1. Employee Details
    #1.1 Add new one
    def employeedetails(self, name,age,occupation,date_of_joining,contact_info,salary):
        count=self.emp_id()
        self.mycursor.execute("insert into employee_details values({0},'{1}',{2},'{3}','{4}','{5}',{6})".format(count+1,name,age,occupation,date_of_joining,contact_info,salary))
        self.myconnect.commit()
        print('Record added')

    #1.2 display details
    def display_emp_details(self,name):
        self.mycursor.execute("select * from employee_details where name='%s'"%(name))
        records=self.mycursor.fetchall() # Check Kar
        print(tabulate(records,headers = ["ID", "Name", "Age", "Occupation","Date Of Joining", "Contact", "Salary"]))
        # for i in range(len(records)):
            # emp_id=records[i][0]
            # age=records[i][2]
            # occupation=records[i][3]
            # DOJ=records[i][4]
            # contact=records[i][5]
            # salary=records[i][6]
            # print(f"Details\n\nID: {emp_id}\nName: {name}\nAge: {age}\nOccupation: {occupation}\nDate of Joining: {DOJ}\nContact: {contact}\nSalary: {salary}")


    #1.3 Update record
    def update_emp_record(self,name,field,value):
        if field in ['emp_id','age','salary']:
            self.mycursor.execute("update employee_details set {0}={1} where name='{2}'".format(field,int(value),name))
            self.myconnect.commit()
        else:
            self.mycursor.execute("update employee_details set {0}='{1}' where name='{2}'".format(field,str(value),name))
            self.myconnect.commit()
        print('Record Updated')

    #1.4 Delete record
    def delete_record(self,name):
        self.mycursor.execute("select * from employee_details where name='"+name+"'")
        row=self.mycursor.fetchall()
        for i in range(len(row)):
            eid=row[i][0]
            age=row[i][2]
            occu=row[i][3]
        print(f"Details\n\nID: {eid}\nName: {name}\nAge: {age}\nOccupation: {occu}")
        p=input('Do you wish to proceed with the action (y/n): ')
        if p.lower()=='y':
            self.mycursor.execute("delete from employee_details where name='"+name+"'")
            self.myconnect.commit()
            print("Record deleted")
        else:
            print("ACTION CANCELLED")

    #1.5 Exit - In main loop

    #2. Inventory 
    #2.1 Add new one to inventory
    def bookdetails(self,name,author,publisher,purchase_date,purchase_cost,copies):
        count=self.book_id()
        self.mycursor.execute("insert into book_details values({0},'{1}','{2}','{3}','{4}',{5},{6})".format(count+1,name,author,publisher,purchase_date,purchase_cost,copies))
        self.myconnect.commit()
        print('Record added')

#2.2 Display details of book
    def display_book_details(self,book_name):
        self.mycursor.execute("select * from book_details where name='%s'"%(book_name))
        records=self.mycursor.fetchall() # Check Kar
        print(tabulate(records,headers = ["ID", "Name", "Author", "Publisher","Date Of Purchase", "Purchase Cost", "No of Copies"]))
        # for i in range(len(records)):
        #     book_id=records[i][0]
        #     author=records[i][2]
        #     publisher=records[i][3]
        #     DOP=records[i][4]
        #     purchase_cost=records[i][5]
        #     copies=records[i][6]
        #     print(f"Details\n\nID: {book_id}\nName: {book_name}\nAuthor: {author}\nPublisher: {publisher}\nDate of Purchase: {DOP}\nPurchase Cost: {purchase_cost}\nNo of Copies: {copies}")

#2.3 
    def update_book_record(self,name,field,value):
        if field in ['book_id','copies','cost_of_purchase']:
            self.mycursor.execute("update book_details set {0}={1} where name='{2}'".format(field,int(value),name))
            self.myconnect.commit()
        else:
            self.mycursor.execute("update book_details set {0}='{1}' where name='{2}'".format(field,str(value),name))
            self.myconnect.commit()
        print('Record Updated')

#2.4 Delete record
    def delete_book_record(self,book_name):
        self.mycursor.execute("select * from book_details where name='"+book_name+"'")
        row=self.mycursor.fetchall()
        for i in range(len(row)):
            bid=row[i][0]
            author=row[i][2]
            publisher=row[i][3]
        print(f"Details\n\nID: {bid}\nName: {book_name}\nAuthor: {author}\nPublisher: {publisher}")
        p=input('Do you wish to proceed with the action (y/n): ')
        if p.lower()=='y':
            self.mycursor.execute("delete from book_details where name='"+book_name+"'")
            self.myconnect.commit()
            print("Record deleted")
        else:
            print("ACTION CANCELLED")

#2.5 Exit - In Main Loop

#3 Purchase Details
#3.1 Add new one to inventory
    def purchdetails(self,name,book_name,contact_info,address,status,purchase_date,cost,date_of_return,username="Null"):
        count=self.purchase_id()
        if date_of_return != "Null":
            date_of_return = "'"+date_of_return+"'"
        if username == "Null":
            self.mycursor.execute("insert into purchase_rent_details values({0},'{1}','{2}','{3}','{4}','{5}',{6},{7},{8})".format(count+1,name,contact_info,address,status,purchase_date,cost,date_of_return,str(self.get_book_id(book_name))))
        else:
            self.mycursor.execute("insert into purchase_rent_details values({0},'{1}','{2}','{3}','{4}','{5}',{6},{7},{8},'{9}')".format(count+1,name,contact_info,address,status,purchase_date,cost,date_of_return,str(self.get_book_id(book_name)),self.get_user_id(username)))
        self.myconnect.commit()
        print('Record added')

    #3.2 Display details of purchase
    def display_purch_details(self,name1):
        self.mycursor.execute("select * from purchase_rent_details where name='%s'"%(name1))
        records=self.mycursor.fetchall() # Check Kar
        print(tabulate(records,headers = ["ID", "Name", "Author", "Publisher","Date Of Purchase", "Purchase Cost", "No of Copies"]))

    #3.3 Update purch records
    def update_purch_record(self,name,field,value):
        if field in ['sl_no','cost','cost_of_purchase']:
            self.mycursor.execute("update book_details set {0}={1} where name='{2}'".format(field,int(value),name))
            self.myconnect.commit()
        else:
            self.mycursor.execute("update book_details set {0}='{1}' where name='{2}'".format(field,str(value),name))
            self.myconnect.commit()
        print('Record Updated')

    #3.4 Delete record
    def delete_purch_record(self,name1):# name 1 is name of person
        self.mycursor.execute("select * from purchase_rent_details join book_details on purchase_rent_details.Book_id = book_details.book_id where name='"+name1+"'")
        row=self.mycursor.fetchall()
        for i in range(len(row)):
            purchid=row[i][0]
            book_name=row[i][5]
            date_of_purchase=row[i][10]
        print(f"Details\n\nID: {purchid}\nName: {name1}\nBook Name: {book_name}\nDate of Purchase: {date_of_purchase}")
        p=input('Do you wish to proceed with the action (y/n): ')
        if p.lower()=='y':
            self.mycursor.execute("delete from purchase_rent_details where name='"+name1+"'")
            self.myconnect.commit()
            print("Record deleted")
        else:
            print("ACTION CANCELLED")

    #3.5 Exit - In Main Loop
    #4 IDEK Name 
    #4.1
    def userdetails(self,name,user_name,password):
        count=self.userid()
        self.mycursor.execute("insert into user_details values({0},'{1}','{2}','{3}')".format(count+1,name,user_name,password))
        self.myconnect.commit()
        print('Record added')
    #4.2
    def display_user_details(self,name):
        self.mycursor.execute("select * from user_details where name='%s'"%(name))
        records=self.mycursor.fetchall()
        while True:
            passwd=input("Would you like to know passwords as well? (Y/n) : ")
            if passwd in 'Yy':
                print(tabulate(records,headers = ["ID", "Name", "Username", "Password"]))
                break
            elif passwd in 'Nn':
                mod_records=[]
                for i in records:
                    mod_records.append([i[0],i[1],i[2]])
                print(tabulate(mod_records,headers = ["ID", "Name", "Username"]))
                break
            else:
                print("Wrong input")
    #4.3
    def update_user_details(self,username,field,value):
        if field in ['user_id']:
            self.mycursor.execute("update user_details set {0}={1} where username='{2}'".format(field,int(value),username))
            self.myconnect.commit()
        else:
            self.mycursor.execute("update user_details set {0}='{1}' where username='{2}'".format(field,str(value),username))
            self.myconnect.commit()
        print('Record Updated')
    #4.4
    def delete_user_record(self,username):
        self.mycursor.execute("select * from user_details where username='"+username+"'")
        row=self.mycursor.fetchall()
        for i in range(len(row)):
            uid=row[i][0]
            name=row[i][2]
        print(f"Details\n\nUser ID: {uid}\nName: {name}\nUsername: {username}")
        p=input('Do you wish to proceed with the action (y/n): ')
        if p.lower()=='y':
            self.mycursor.execute("delete from user_details where username='"+username+"'")
            self.myconnect.commit()
            print("Record deleted")
        else:
            print("ACTION CANCELLED")
