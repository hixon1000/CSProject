import FinalCscProject as cs
test = cs.project()

def employee_add():
    name = input("Enter employee name : ")
    age = test.force_int("Enter employee age : ")
    occupation = input("Enter occupation : ")
    date_of_joining = test.force_date("Enter date of joining (yyyy-mm-dd) : ")
    contact_info = input("Enter contact information : ")
    salary = test.force_int("Enter the salary : ")
    test.employeedetails(name,age,occupation,date_of_joining,contact_info,salary)
def display_employee_record():
    test.display_emp_details(input("Enter employee name : "))
def update_employee_records():
    name = input("Enter employee name : ")
    field = input("Enter the feild to change : ")
    value = input("Enter changed value : ")
    test.update_emp_record(name,field,value)
def delete_employee_records():
    name = input("Enter employee name : ")
    test.delete_record(name)
def book_add():
    name = input("Enter book name : ")
    author = input("Enter author name : ")
    publisher = input("Enter publisher name : ")
    purchase_date = test.force_date("Enter purchase date (yyyy-mm-dd) : ")
    purchase_cost = test.force_int("Enter purchase cost of book : ")
    copies = test.force_int("Enter the number of copies : ")
    test.bookdetails(name,author,publisher,purchase_date,purchase_cost,copies)
def book_display():
    test.display_book_details(input("Enter book name"))
def book_update():
    name = input("Enter book name : ")
    field = input("Enter the feild to change : ")
    value = input("Enter changed value : ")
    test.update_book_record(name, field,value)
def book_delete():
    name = input("Enter book name : ")
    test.delete_book_record(name)
def purchase_add():
    name = input("Enter customer name : ")
    contact = input("Enter contact number : ")
    book_name = input("Enter book name : ")
    address = input("Enter your address : ")
    status = input("Enter book stats (Purchased or issued) : ")
    purchase_date = test.force_int("Enter the purchase date : ")
    cost = test.force_int("Enter the cost : ")
    date_of_return = "Null"
    while True:
        n = input("Is the customer registered?")
        if n in "Yy":
            username = input("Enter customer username : ")
            test.purchdetails(name,book_name,contact,address,status,purchase_date,cost,date_of_return,username)
            break
        elif n in "Nn":
            test.purchdetails(name,book_name,contact,address,status,purchase_date,cost,date_of_return)
            break
        else:
            print("Invalid input")
def purchase_display():
    test.display_purch_details(input("Enter customer name : "))
def purchase_update():
    name = input("Enter customer name : ")
    field = input("Enter the feild to change : ")
    value = input("Enter changed value : ")
    test.update_purch_record(name, field,value)
def purchase_delete():
    test.delete_purch_record(input("Enter customer name : "))
def user_add():
    name = input("Enter customer name : ")
    user_name = input("Enter a new username : ")
    password = input("Enter the password : ")
    test.userdetails(name,user_name,password)
def user_display():
    test.display_user_details(input("Enter the username : "))
def user_update():
    name = input("Enter user name : ")
    field = input("Enter the feild to change : ")
    value = input("Enter changed value : ")
    test.update_user_details(name, field, value)
def user_delete():
    test.delete_user_record(input("Enter the username : "))
print("Welcome to our program!")
while True:
    print("1)Employee management")
    print("2)Inventory of books")
    print("3)Exit")
    choice = test.force_int("Enter your choice : ")
    if choice == 1:
        print("Entered employee management")
        while True:
            print("1)Add employee")
            print("2)Display employee details")
            print("3)Update employee information")
            print("4)Remove an employee")
            print("5)Enter back to main")
            choice = test.force_int("Enter your choice : ")
            if choice == 1:
                employee_add()
            elif choice == 2:
                display_employee_record()
            elif choice == 3:
                update_employee_records()
            elif choice == 4:
                delete_employee_records()
            elif choice == 5:
                break
            else:
                print("Invalid input")
    elif choice == 2:
        print("Entered book inventory")
        while True:
            print("1)Add book")
            print("2)Display book details")
            print("3)Update book information")
            print("4)Remove a book")
            print("5)Enter back to main")
            choice = test.force_int("Enter your choice : ")
            if choice == 1:
                book_add()
            elif choice == 2:
                book_display()
            elif choice == 3:
                book_update()
            elif choice == 4:
                book_delete()
            elif choice == 5:
                break
            else:
                print("Invalid input")
    elif choice == 3:
        print("Entered purchase information")
        while True:
            print("1)Add an entry")
            print("2)Display a record")
            print("3)Update a record")
            print("4)Remove a record")
            print("5)Enter back to main")
            if choice == 1:
                purchase_add()
            elif choice == 2:
                purchase_display()
            elif choice == 3:
                purchase_update()
            elif choice == 4:
                purchase_delete()
            elif choice == 5:
                break
            else:
                print("Invalid input")
    elif choice == 4:
        print("Entered user management")
        while True:
            print("1)Add a new user")
            print("2)Display a user's information")
            print("3)Update user information")
            print("4)Remove a user")
            print("5)Exit back to main")
            if choice == 1:
                user_add()
            elif choice == 2:
                user_display()
            elif choice == 3:
                user_update()
            elif choice == 4:
                user_delete()
            elif choice == 5:
                break
            else:
                print("Invalid input")
    elif choice == 5:
        print("Bye!")
        break
    else:
        print("Invalid input")