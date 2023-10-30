"""Tests for the school module"""
import pytest
from source.school import Teacher, Student, TooManyStudents, Classroom


# Helper function to create a classroom with some initial students
def create_classroom_with_students():
    """Create a classroom with some initial students"""
    teacher = Teacher("Severus Snape")
    students = [Student("Harry Potter"), Student("Hermione Granger")]
    return Classroom(teacher, students, "Potions Class")


def test_add_student_to_classroom():
    """Test adding a student to a classroom"""
    classroom = create_classroom_with_students()
    new_student = Student("Ron Weasley")
    classroom.add_student(new_student)
    assert new_student in classroom.students


def test_remove_student_from_classroom():
    """Test removing a student from a classroom"""
    classroom = create_classroom_with_students()
    student_name = "Hermione Granger"
    classroom.remove_student(student_name)
    assert all(student.name != student_name for student in classroom.students)


def test_change_teacher_in_classroom():
    """Test changing the teacher in a classroom"""
    classroom = create_classroom_with_students()
    new_teacher = Teacher("Remus Lupin")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == new_teacher.name


def test_too_many_students_exception():
    """Test that a TooManyStudents exception is raised when adding too many students"""
    classroom = create_classroom_with_students()
    with pytest.raises(TooManyStudents):
        for _ in range(25):
            student = Student("Random Student")
            classroom.add_student(student)
