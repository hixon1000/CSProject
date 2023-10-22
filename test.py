import FinalCscProject as cs
main = cs.project()
Logged_in = main.logged_in
def employee_add():
    name = input("Enter employee name : ")
    age = main.force_int("Enter employee age : ")
    occupation = input("Enter occupation : ")
    date_of_joining = main.force_date("Enter date of joining (yyyy-mm-dd) : ")
    contact_info = input("Enter contact information : ")
    salary = main.force_int("Enter the salary : ")
    main.employeedetails(name,age,occupation,date_of_joining,contact_info,salary)
def display_employee_record():
    main.display_emp_details(input("Enter employee name : "))
def update_employee_records():
    name = input("Enter employee name : ")
    field = input("Enter the feild to change : ")
    value = input("Enter changed value : ")
    main.update_emp_record(name,field,value)
def delete_employee_records():
    name = input("Enter employee name : ")
    main.delete_record(name)
def book_add():
    name = input("Enter book name : ")
    author = input("Enter author name : ")
    publisher = input("Enter publisher name : ")
    purchase_date = main.force_date("Enter purchase date (yyyy-mm-dd) : ")
    purchase_cost = main.force_int("Enter purchase cost of book : ")
    copies = main.force_int("Enter the number of copies : ")
    main.bookdetails(name,author,publisher,purchase_date,purchase_cost,copies)
def book_display():
    main.display_book_details(input("Enter book name"))
def book_update():
    name = input("Enter book name : ")
    field = input("Enter the feild to change : ")
    value = input("Enter changed value : ")
    main.update_book_record(name, field,value)
def book_delete():
    name = input("Enter book name : ")
    main.delete_book_record(name)
def purchase_add():
    name = input("Enter customer name : ")
    contact = input("Enter contact number : ")
    book_name = input("Enter book name : ")
    address = input("Enter your address : ")
    status = input("Enter book stats (Purchased or issued) : ")
    purchase_date = main.force_int("Enter the purchase date : ")
    cost = main.force_int("Enter the cost : ")
    while True:
        date = input("Is there a date of return (Y/n) : ")
        if date in "Yy":
            date_of_return = main.force_date("Enter date of return : ")
            main.purchdetails(name,book_name,contact,address,status,purchase_date,cost,date_of_return)
            break
        else:
            main.purchdetails(name,book_name,contact,address,status,purchase_date,cost,main.user)
def purchase_display():
    main.display_purch_details(input("Enter customer name : "))
def purchase_update():
    name = input("Enter customer name : ")
    field = input("Enter the feild to change : ")
    value = input("Enter changed value : ")
    main.update_purch_record(name, field,value)
def purchase_delete():
    main.delete_purch_record(input("Enter customer name : "))
def user_add():
    name = input("Enter employee/represntative name : ")
    user_name = input("Enter a new username : ")
    password = input("Enter the password : ")
    emp_id = main.force_int("Enter employee id : ")
    main.userdetails(name,user_name,password,emp_id)
def user_display():
    main.display_user_details(input("Enter the username : "))
def user_update():
    name = input("Enter user name : ")
    field = input("Enter the feild to change : ")
    value = input("Enter changed value : ")
    main.update_user_details(name, field, value)
def user_delete():
    main.delete_user_record(input("Enter the username : "))
if Logged_in:
    print("Welcome to library management system!")
while Logged_in:
    print("1)Employee management")
    print("2)Inventory of books")
    print("3)Purchase information")
    print("4)User management (Mostly for admin)")
    print("5)Exit")
    choice = main.force_int("Enter your choice : ")
    if choice == 1:
        print("Entered employee management")
        while True:
            print("1)Add employee")
            print("2)Display employee details")
            print("3)Update employee information")
            print("4)Remove an employee")
            print("5)Enter back to main")
            choice = main.force_int("Enter your choice : ")
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
            choice = main.force_int("Enter your choice : ")
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
            choice = main.force_int("Enter your choice : ")
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
            choice = main.force_int("Enter your choice : ")
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