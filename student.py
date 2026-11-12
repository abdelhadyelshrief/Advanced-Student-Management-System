
class Student : 
    def __init__(self, name, student_id, age, gpa):
        self.name = name 
        self.student_id = student_id
        self.age =age
        self.gpa = gpa

    def getInfo(self):
        return f"Name:{self.name}\n idNumber: {self.student_id}\n age:{self.age}\n GPA:{self.gpa}"


    def update_gpa(self, new_gpa):
        self.gpa=new_gpa

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "age": self.age,
            "gpa": self.gpa
        }
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <10:
            raise ValueError("Age must be greater than 10")
        else:
            self._age = value
    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        if value <0 or value >4.0 :
            raise ValueError("GPA must be between 0 and 4.0")
        else:
            self._gpa = value   

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if len(str(value)) != 9:
            raise ValueError("Student ID must be a 9-digit number")
        else:
            self._student_id = value

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            student_id=data.get("student_id"),
            age=data.get("age"),
            gpa=data.get("gpa")
        )
    @staticmethod
    def is_valid_gpa(gpa):
        return 0 <= gpa <= 4.0

    @gpa.setter
    def gpa(self, value):
        if not self.is_valid_gpa(value):
            raise ValueError("GPA must be between 0 and 4.0")
        else:
            self._gpa = value

class GraduateStudent(Student):
    def __init__(self, name, student_id, age, gpa, research_topic):
        super().__init__(name, student_id, age, gpa)
        self.research_topic = research_topic

    def getInfo(self):
        return f"Name:{self.name}\n idNumber: {self.student_id}\n age:{self.age}\n GPA:{self.gpa}\n Research Topic:{self.research_topic}"





