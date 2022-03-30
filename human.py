class Human:
    energy = 100

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name.title()} {self.surname.title()}. Age: {self.age}"

    def __repr__(self):
        return f"Human {self.name.title()} {self.surname.title()}, age: {self.age}"

    def __call__(self):
        return "Who called me?"

    def eat(self):
        if Human.energy < 150:
            Human.energy += 5

    def sleep(self):
        if Human.energy < 150:
            Human.energy += 25

    def walk(self):
        if Human.energy > 15:
            Human.energy -= 10


class Adult(Human):

    def __init__(self, name, surname, age, election=False):
        super().__init__(name, surname, age)
        self.election = election

    def go_to_the_polling(self):
        if self.election:
            return f"{self.name}'s going to the polling."
        else:
            return f"{self.name} isn't going to the polling."


class Child(Human):
    def __init__(self, name, surname, age, play=False):
        super().__init__(name, surname, age)
        self.play = play

    def play(self):
        if play:
            return f"{self.name} is playing."
        else:
            return f"{self.name} doesn't want to play."

class Student(Adult):
    study_hours = 300

    def __init__(self, name, surname, age, election, subject):
        super().__init__(name, surname, age, election)
        self.subject = subject

    def study(self):
        if Student.study_hours > 0:
            Student.study_hours -= 1.5
        return f"{self.name} studies {self.subject}"


class Worker(Adult):
    increase_pay = 1.02

    def __init__(self, name, surname, age, pay):
        super().__init__(name, surname, age)
        self.pay = pay

    def work(self):
        self.pay *= self.increase_pay


class Teacher(Worker):
    increase_pay = 1.04

    def __init__(self, name, surname, age, pay, subject, students=None, black_list_of_students=None):
        super().__init__(name, surname, age, pay)
        self.subject = subject
        if students:
            self.students = students
        else:
            self.students = []
        if black_list_of_students:
            self.black_list_of_students = black_list_of_students
        else:
            self.black_list_of_students = []

    def __len__(self):
        return len(self.students)

    def __getitem__(self, index):
        try:
            return self.students[index]
        except:
            return "No student was found by this index"
        
    def accept_student(self, student):
        if student not in self.students:
            self.students.append(student)
        return 'Students: ' + ', '.join(student for student in self.students)

    def remove_student(self, student):
        if student in self.students or Student.study_hours == 0:
            self.students.remove(student)
        return f"{student} was removed."

    def add_student_to_black_list(self, student):
        if student in self.students:
            self.black_list_of_students.append(student)
        return 'Black list: ' + ', '.join(student for student in self.black_list_of_students)
