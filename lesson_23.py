class Person:
    def __init__(self, first, last):
        print('Person.__init__() ->')
        self.first = first
        self.last = last
        print('Person.__init__() <-')


class FullnamePerson(Person):
    def __init__(self, first, last):
        print('FullnamePerson.__init__() ->')
        super().__init__(first, last)
        self.fullname = f"{self.first} {self.last}"
        print('FullnamePerson.__init__() <-')


class AbbrevPerson(Person):
    def __init__(self, first, last):
        print('AbbrevPerson.__init__() ->')
        super().__init__(first, last)
        self.abbrev = f"{self.first[0]} {self.last[0]}"
        print('AbbrevPerson.__init__() <-')


class RealPerson(FullnamePerson, AbbrevPerson):
    def __init__(self, first, last):
        print('RealPerson.__init__() ->')
        super().__init__(first, last)
        print('Person.__init__() <-')


real_p = RealPerson('Master', 'Yoda')
print(FullnamePerson.mro())
