"""
********* Usman School Management *********
1: View All Students
2: Add New Student
3: Edit a student
4: Expell a student
5: Search a student
0: Exit

===1
Roll No.    First Name.     Last Name.     Class       Fee
..
...
===2
Enter First Name: _
Enter Last Name: _
Enter Date Of Birth: _
Enter Class: _
Enter Fee: _
===3
Enter Roll Number: __
1: Change First Name
2: Change Last Name
3: Change Fee
4: Change Class

===4
Enter Roll Number: _
Do you want to expell {first_name} {last_name} ?(y/n)
    ===y
    {roll_number} has been expelled
===5
1: Search by first name
2: Search by last name
3: Search by roll number name
4: Search by class
        Roll No.    First Name.     Last Name.     Class       Fee
        ...
        ...
"""
from functions import *


while True:
    dashboard()
    choice_()
    