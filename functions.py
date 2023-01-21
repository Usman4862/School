# FUNCTIONS___________
import os
from random import randint
roll_number = randint(1, 100)
storage = {
    roll_number : {
        'firstname': 'Usman', 
        'lastname': 'Malik', 
        'dateofbirth': '26/10/2002', 
        'class': '10th', 
        'fees': '25000'
    },
    roll_number : {
        'firstname' : 'mubashir',        
        'lastname' : 'haider',
        'dateofbirth' : '28/10/2003',
        'class' : '10th',
        'fees' : '25000'
    }
}


def dashboard():
    # os.system("cls")
    print("**************ROYAL EDUCATION COMPLEX******************")
    print("1: View All Students")
    print("2: Add New Student")
    print("3: Edit a Student")
    print("4: Expell a Student")
    print("5: Search a Student")
    print("0: Exit")



def choice_():
    user_choice = input("Enter Your Choice: ")
    # os.system("cls")
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
        exit()
    else:
        exit("Invalid Choice")

def view_all_students():
    for keys, values in storage.items():
        print(f"{keys}----{values['firstname']}-----{values['lastname']}-----{values['class']}-----{values['fees']}")
        continue

def add_new_student():
    # os.system("cls")
    print("****Add New Student****")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    date_of_birth = input("Enter Date of Birth: ")
    class_ = input("Enter class: ")
    fees = input("Enter fees: ")

    students = {
        "firstname" : first_name,
        "lastname" : last_name,
        "dateofbirth" : date_of_birth,
        "class" : class_,
        "fees" : fees,
        }
    storage[roll_number] = students
    print(f"*************{first_name} {last_name}***************")
    print("Added Sucessfully")




def edit_student():
    pass
def expell_student():
    pass
def search_student():
    pass


