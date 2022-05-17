"""Simple implementation of human"""

from typing import List, Union


class Human:
    """Basic human class"""

    energy = 100

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.__index = 0

    def __str__(self):
        return f"{self.name.title()} {self.surname.title()}"

    def __repr__(self):
        return f"Human {self.name.title()} {self.surname.title()}"

    def __call__(self):
        return "Who called me?"

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        __full_info = [self.name, self.surname, self.age]
        if self.__index >= len(__full_info):
            raise StopIteration
        index = self.__index
        self.__index += 1
        return __full_info[index]

    @property
    def fullname(self):
        """Returns full human name"""
        return f"{self.name.title()} {self.surname.title()}"

    @fullname.setter
    def fullname(self, new_name: str):
        """Sets humans fullname"""
        name, surname = new_name.split()
        self.name = name
        self.surname = surname

    @fullname.deleter
    def fullname(self):
        """Deletes human's full name"""
        self.name = None
        self.surname = None

    def eat(self):
        """Adds 5 energy"""
        if self.energy < 150:
            self.energy += 5

    def sleep(self):
        """Adds 25 energy"""
        if self.energy < 150:
            self.energy += 25

    def walk(self):
        """Subtracts 10 energy"""
        if self.energy > 15:
            self.energy -= 10


class Adult(Human):
    """Adult class"""

    def __init__(self, name: str, surname: str,
                 age: int, election: bool = False):
        super().__init__(name, surname, age)
        self.election = election

    def elect(self):
        """
        If true, then adult
        can go to en election,
        else can't.
        """
        if self.election:
            return f"{self.name.title()}'s going to an election."
        return f"{self.name.title()} isn't going to an election."


class Child(Human):
    """Child class"""

    def __init__(self, name: str, surname: str,
                 age: int, is_playing: bool = True):
        super().__init__(name, surname, age)
        self.is_playing = is_playing

    def play(self):
        """
        If play - True, then child is playing,
        else - isn't playing
        """
        if self.is_playing:
            return f"{self.name} is playing."
        return f"{self.name} doesn't want to play."


class Student(Human):
    """Basic student class"""

    study_hours = 300

    def __init__(self, name: str, surname: str, age: int, subject: str):
        super().__init__(name, surname, age)
        self.subject = subject
        self.marks: List[int] = []
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        __full_info = [self.name, self.surname, self.age]
        if self.__index >= len(__full_info):
            raise StopIteration
        index = self.__index
        self.__index += 1
        return __full_info[index]

    def study(self):
        """Subtracts 1.5 hours from student hours"""
        if Student.study_hours > 0:
            Student.study_hours -= 1.5
        return f"{self.name} studies {self.subject}"

    @property
    def student_marks(self):
        """Returns student's marks"""
        return f"{self.name}'s marks: " \
               + ", ".join([str(mark) for mark in self.marks])

    @student_marks.deleter
    def student_marks(self):
        """Deletes student's marks"""
        self.marks = []


class Worker(Adult):
    """Simple implementation of worker"""

    increase_pay = 1.02

    def __init__(self, name: str, surname: str,
                 age: int, pay: Union[int, float]):
        super().__init__(name, surname, age)
        self.pay = pay

    def work(self):
        """Increases worker's pay"""
        self.pay *= Worker.increase_pay
        return self.pay


class Teacher(Worker):
    """Class Teacher for working with class Student"""

    increase_pay = 1.04

    def __init__(self, name: str, surname: str,
                 age: int, pay: Union[int, float],
                 subject: str, *students):
        super().__init__(name, surname, age, pay)
        self.subject = subject
        self.students = \
            [student for student in students if isinstance(student, Student)]
        self.black_list_of_students: List[Student] = []
        self.__index = 0

    def __len__(self):
        return len(self.students)

    def __getitem__(self, index):
        try:
            return self.students[index]
        except IndexError:
            return "No student was found by this index"

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.students):
            raise StopIteration
        index = self.__index
        self.__index += 1
        return self.students[index]

    def evaluate_student(self, mark: int, student: Student):
        """Adds a mark for a student if student in students
        list and student is Student
        """
        if type(mark) is not int:
            raise TypeError(f"mark must be an integer, except got: {mark}")
        if student.subject == self.subject \
                and student in self.students \
                and isinstance(student, Student):
            student.marks.append(mark)

    def accept_student(self, *students: Student):
        """Adds a new student to a students list
        is student not in students list and student
        is Student.
        """
        for student in students:
            if student not in self.students and type(student) is Student:
                self.students.append(student)

    def remove_student(self, student: Student) -> str:
        """Removes student from a students list
        is student is in students list or student's study
        hour's - 0.
        """
        if student in self.students or Student.study_hours == 0:
            self.students.remove(student)
            return f"{student} was removed."
        return "Student couldn't be removed"

    def add_student_to_black_list(self, student: Student):
        """Adds a student to black list
        if student is in student's list.
        """
        if student in self.students:
            self.black_list_of_students.append(student)

    @property
    def blacklist(self) -> str:
        """Returns a blacklist of students"""
        return 'Black list: ' + \
               ', \n'.join(str(student)
                           for student in self.black_list_of_students)

    @property
    def students_list(self) -> str:
        """Returns students list"""
        return 'Students: ' + \
               ', '.join(str(student) for student in self.students)
