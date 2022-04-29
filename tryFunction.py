from function import countPassedStudents
from function_M1 import countPassedStudentsM1
from function_M2 import countPassedStudentsM2


def tryCountPassedStudents(students, courses, grades):
    try:
        return countPassedStudentsM2(students, courses, grades)
    except TypeError:
        raise TypeError
