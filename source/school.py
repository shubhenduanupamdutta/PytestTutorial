"""Demo for using chatGPT for pytest"""


class Person:
    """Class to represent a person"""

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


class Teacher(Person):
    """Class to represent a teacher"""

    def __init__(self, name: str, age: int = 32):
        super().__init__(name)
        self.age = age

    def change_age(self, new_age: int):
        """Change the age of the teacher"""
        self.age = new_age

    def change_name(self, new_name: str):
        """Change the name of the teacher"""
        self.name = new_name


class Student(Person):
    """Class to represent a student"""

    def __init__(self, name: str, year: int = 3):
        super().__init__(name)
        self.year = year

    def change_year(self, new_year: int):
        """Change the year of the student"""
        self.year = new_year

    def change_name(self, new_name: str):
        """Change the name of the student"""
        self.name = new_name


class TooManyStudents(Exception):
    """Exception raised when too many students are added to a class"""

    def __init__(self, message):
        super().__init__(message)


class Classroom:
    """Class to represent a classroom"""

    def __init__(self, teacher: Person, students: list[Person], course_title: str):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title

    def add_student(self, student: Person):
        """Add a student to the class"""
        if len(self.students) > 20:
            raise TooManyStudents("Too many students in this class")
        self.students.append(student)

    def remove_student(self, name: str):
        """Remove a student from the class"""
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break

    def change_teacher(self, new_teacher: Person):
        """Change the teacher of the class"""
        self.teacher = new_teacher
