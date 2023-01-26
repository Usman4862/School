# FUNCTIONS___________
import os
# from random import randint
from sys import platform


def clear_screen():
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")


target_ = 1

storage = {
    target_ : {
        'firstname': 'Usman', 
        'lastname': 'Malik',
        'dateofbirth': '26/10/2002', 
        'class': '10th', 
        'fees': '25000'
    }
}


def dashboard():
    clear_screen()
    print("**************ROYAL EDUCATION COMPLEX******************\n")
    print("1: View All Students")
    print("2: Add New Student")
    print("3: Edit a Student")
    print("4: Expell a Student")
    print("5: Search a Student")
    print("0: Exit")


def choice_():
    user_choice = input("Enter Your Choice: ")
    # os.system('cls')
    if user_choice == "1":
        view_all_students()
    elif user_choice == "2":
        add_new_student()
    elif user_choice == "3":
        edit_student()
    elif user_choice == "4":
        expell_student()
    elif user_choice == "5":
        search_student()
    elif user_choice == "0":
        clear_screen()
        exit()
    else:
        clear_screen()
        exit("\nInvalid Choice")


def view_all_students():
    clear_screen()
    print("**************\n")
    print("All Students \n")
    for roll, values in storage.items():
        print(f"{roll}----{values['firstname']}-----{values['lastname']}-----{values['class']}-----{values['fees']} \n")
    input("Press enter to go back: ")


def add_new_student():
    # os.system("cls")
    print("\n****Add New Student****\n")
    first_name = input("Enter first name: \n")
    last_name = input("Enter last name: \n")
    date_of_birth = input("Enter Date of Birth: \n")
    class_ = input("Enter class: \n")
    fees = input("Enter fees: \n")

    student = {
        "firstname" : first_name,
        "lastname" : last_name,
        "dateofbirth" : date_of_birth,
        "class" : class_,
        "fees" : fees,
        }
    from random import randint
    roll_number = randint(0,999999)
    storage[roll_number] = student
    
    print(f"*************{first_name} {last_name}***************")
    print("Added Sucessfully\n")


def edit_student():
    clear_screen()
    print("\n *************")
    print("\nEdit Student")
    _edit = input("Enter Roll Number: ")
    while True:
        if _edit == str(target_):
            print("1- Edit first name: ")
            print("2- Edit last name: ")
            print("3- Edit Roll number: ")
            print("4- Edit date of birth: ")
            print("5- Edit class: ")
            print("6- Edit fees: ")
            print("0- Go Back: ")
            choice = input("Enter Your choice: ")
            if choice == "1":
                first_name = input("Enter first name of Student: ")
                storage[target_]["firstname"] = first_name
                print(f"\n First name has been change to {first_name}")
            elif choice == "2":
                last_name = input("Enter last name of Student: ")
                storage[target_]["lastname"] = last_name
                print(f"\n Last name has been change to {last_name}")
            elif choice == "3":
                roll_number = input("Enter roll number of Student: ")
                storage[target_] = roll_number
                print(f"\n Roll number has been change to {roll_number}")
            elif choice == "4":
                date_of_birth = int(input("Enter date of birth of Student: "))
                storage[target_]["dateofbirth"] = date_of_birth
                print(f"\n Date of Birth has been change to {date_of_birth}")
            elif choice == "5":
                class_ = input("Enter class of Student: ")
                storage[target_]["class"] = class_
                print(f"\n Class has been change to {class_}")
            elif choice == "6":
                fees = input("Enter fees of Student: ")
                storage[target_]["fees"] = fees
                print(f"\n fees has been change to {fees}")
            elif choice == "0":
                break
            else:
                clear_screen()
                print("Invalid Choice \n")
        else:
            print("Student not exist")


def expell_student():
    clear_screen()
    print("**************\n")
    print("Remove a Student\n")
    remove = input("Enter Roll Number of a student:")
    if remove == str(target_):
        del storage[target_]
        print(f"{target_} has been removed\n")
    else:
        print("Student not Exists\n")
    input("Press Enter to go back: ")

def search_student():
    clear_screen()
    print("**************\n")
    print("------Search a student------- \n ")
    search_ = input("Enter roll number: ")
    search_ = storage[target_]
    search_ = storage.get(target_, None)
    if search_ == None:
        print("Not Found")
    else:
        for roll, values in storage.items():
            print(f"{roll}----{values['firstname']}-----{values['lastname']}-----{values['class']}-----{values['fees']}")
    input("Press Enter to go back: ")

