from student import Student
from student_manger import StudentManger


manger=StudentManger()
manger.load_students()  # Load students from file at the start of the program

            
while True:
    print("\n----Student Management System----\n")
    print("1.Add Student : ")
    print("2.Find Student : ")
    print("3.Delete Student : ")
    print("4.Display Student : ")
    print("5.Update GPA :  ")
    print("6.Statistics : ")
    print("7.EXIT: ")

    try:
        choice = int(input("Choose : "))
    except ValueError:
        print("Please enter a valid option")
        continue

    if choice == 1:
        name = input("Enter Name of Student: ")
        try: 
            student_id = int(input("Enter your ID: "))
            age = int(input("Enter Your age: "))
            gpa = float(input("Enter your gpa: "))
            student = Student(name, student_id, age, gpa) 

        except ValueError as e:
            print(f"Error: {e}")
            continue


        student = Student(name, student_id, age, gpa)
        if manger.add_student(student):
            print("Student added successfully")
        else:
            print("Student could not be added")

        
        manger.save_students()  # Save students after adding a new one

    elif choice == 2:
        try:
            student_id = int(input("Enter your id: "))
        except ValueError:
            print("Please enter a valid numeric value for student ID")
            continue
        student = manger.find_student(student_id)
        if student:
            print(student.getInfo())
        else:
            print("Student not found")

    elif choice == 3:
        try:
            student_id = int(input("Enter your id : "))
        except ValueError:
            print("Please enter a valid numeric value for student ID")
            continue
        if manger.delete_student(student_id):
            print("The student has been deleted")
        else:
            print("Student not found")

    elif choice == 4:
        if not manger.students:
            print("No students to display")
        else:
            manger.display_students()
            print("Those are all students")

    elif choice == 5:
        try:
            student_id = int(input("Enter your id : "))
        except ValueError:
            print("Please enter a valid numeric value for student ID")
            continue
        try:
            gpa = float(input("Enter your gpa: "))
        except ValueError:
            print("Please enter a valid numeric value for GPA")
            continue
        if manger.update_students(student_id, gpa):
            print("Your GPA has been updated successfully")
        else:
            print("Student not found or GPA is invalid")

    elif choice == 6:
        manger.get_statistics()

    elif choice == 7:
        print("GOOD Bye")
        break

    else:
        print("This option is not found")



