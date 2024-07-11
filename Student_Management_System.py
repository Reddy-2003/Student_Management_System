student_grades={ }

def add_student(name,grades):
    student_grades[name]=grades
    print(f"student {name} is added")

def update_student(name,grades):
    if name in student_grades:
        student_grades[name]=grades
        print(f"The updated name of student is {name}")
    else:
        print(f"Student name {name} is not found ")

def delete_student(name,grades):
    if name in student_grades:
        del student_grades[name]
        print(f"Deleted name of student is {name}")
    else:
        print(f"Name {name} is not found")

def display_student():
    if student_grades:
        for names,grade in student_grades.items():
            print(f"{names} :{grade}")
    else:
        print("No students found")
while True:
    print("\nStudent Management System")
    print("1.Add")
    print("2.Update")
    print("3.Delete")
    print("4.Display")
    print("5.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        name=input("Enter the name of student:")
        grades=int(input("Enter the grade of the student"))
        add_student(name,grades)
    elif ch==2:
        name=input("Enter the name of student:")
        grades=int(input("Enter the grade of the student"))
        update_student(name, grades)
    elif ch==3:
        name=input("Enter the name of student:")
        grades=int(input("Enter the grade of the student"))
        delete_student(name, grades)
    elif ch==4:
        display_student()
    elif ch==5:
        break
    else:
        print("Invalid Choice")
        
            
            