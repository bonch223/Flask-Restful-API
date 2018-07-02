class Student:
    def __init__(self, name, school, marks):
        self.name = name
        self.school = school
        self.marks = marks

    def get_average(self):
        return sum(self.marks) / len(self.marks)

anna = Student("Anna", "MIT", [1,2,3,4,5])
print(anna.get_average())