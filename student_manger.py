import json
from student import Student
from constants import DATA_FILE
class StudentManger:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        for existing_student in self.students:
            if  existing_student.student_id == student.student_id :
                return False
        self.students.append(student)
        return True

            
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id :

                return student
        return None

    
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id ==student_id:
                self.students.remove(student)
                self.save_students()  
                return True
                
        return False

    def display_students(self):
        for student in self.students:
            print (student.getInfo())

    def update_students(self, student_id , gpa):
        if gpa < 0 or gpa > 4.0:
            return False
        for student in self.students:
            if student.student_id == student_id:
                student.update_gpa(gpa)
                self.save_students()
                return True
               
        return False

    def get_statistics(self):
        count = len(self.students)
        if count == 0:
            print("No students found")
            return
        total_gpa = 0 
        for student in self.students:
            total_gpa =total_gpa + student.gpa
        average = total_gpa / count
        highest = 0 
        for student in self.students:
            if student.gpa > highest:
                highest = student.gpa 
        print(f"The Highest GPA is : {highest:.2f}")
        print(f"The total number of student : {count}")
        print(f"The Average GPA : {average:.2f}")

    def save_students(self):
        students_data = []
        for student in self.students:
            student_data= student.to_dict()
            students_data.append(student_data)
        with open(DATA_FILE, "w") as file:
            json.dump(students_data, file )

    def load_students(self,):
        try:
            with open(DATA_FILE , "r") as file:
                data = json.load(file)
                for student_data in data:
                    student = Student.from_dict(student_data)
                    self.students.append(student)
        except FileNotFoundError:
            print("No existing student data found.")