class Human:
    energy = 100

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.__full_info = [name, surname, age]
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
        if self.__index >= len(self.__full_info):
            raise StopIteration
        index = self.__index
        self.__index += 1
        return self.__full_info[index]

    @property
    def fullname(self):
        return f"{self.name.title()} {self.surname.title()}"

    @fullname.setter
    def fullname(self, string):
        name, surname = string.split()
        self.name = name
        self.surname = surname

    @fullname.deleter
    def fullname(self):
        self.name = None
        self.surname = None

    def eat(self):
        if self.energy < 150:
            self.energy += 5

    def sleep(self):
        if self.energy < 150:
            self.energy += 25

    def walk(self):
        if self.energy > 15:
            self.energy -= 10


class Adult(Human):

    def __init__(self, name, surname, age, election=False):
        super().__init__(name, surname, age)
        self.election = election

    def elect(self):
        if self.election:
            return f"{self.name.title()}'s going to an election."
        return f"{self.name.title()} isn't going to an election."


class Child(Human):
    def __init__(self, name, surname, age, play=True):
        super().__init__(name, surname, age)
        self.play = play

    def play(self):
        if self.play:
            return f"{self.name} is playing."
        return f"{self.name} doesn't want to play."


class Student(Human):
    study_hours = 300

    def __init__(self, name, surname, age, subject):
        super().__init__(name, surname, age)
        self.subject = subject
        self.marks = []
        self.__index = 0
        self.__full_info = [name, surname, age]

    def study(self):
        if Student.study_hours > 0:
            Student.study_hours -= 1.5
        return f"{self.name} studies {self.subject}"

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__full_info):
            raise StopIteration
        index = self.__index
        self.__index += 1
        return self.__full_info[index]

    @property
    def student_marks(self):
        return f"{self.name}'s marks: " + ", ".join([str(mark) for mark in self.marks])

    @student_marks.deleter
    def student_marks(self):
        self.marks = []


class Worker(Adult):
    increase_pay = 1.02

    def __init__(self, name, surname, age, pay):
        super().__init__(name, surname, age)
        self.pay = pay

    def work(self):
        self.pay *= Worker.increase_pay
        return self.pay


class Teacher(Worker):
    increase_pay = 1.04

    def __init__(self, name, surname, age, pay, subject, *students):
        super().__init__(name, surname, age, pay)
        self.subject = subject
        self.students = list(students) if students else []
        self.black_list_of_students = []
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

    def evaluate_student(self, mark, student):
        if type(mark) is not int:
            raise TypeError(f"mark must be an integer, except got: {mark}")
        if student.subject == self.subject and student in self.students and isinstance(student, Student):
            student.marks.append(mark)

    def accept_student(self, *students):
        for student in students:
            if student not in self.students and type(student) is Student:
                self.students.append(student)

    def remove_student(self, student):
        if student in self.students or Student.study_hours == 0:
            self.students.remove(student)
            return f"{student} was removed."

    def add_student_to_black_list(self, student):
        if student in self.students:
            self.black_list_of_students.append(student)

    @property
    def blacklist(self):
        return 'Black list: ' + ', \n'.join(str(student) for student in self.black_list_of_students)

    @property
    def students_list(self):
        return 'Students: ' + ', '.join(str(student) for student in self.students)
