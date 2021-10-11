import datetime

first = []
second = [1, 2, 3]
third = [4, 5, 6]
# first += second
# first += third
first.append(second)
first.append(third)
print(first)


class Toy(object):
    def __init__(self):
        self._elems = []  # underscore : this attributes is private

    def add(self, new_elems):
        '''new elems is a list'''
        self._elems += new_elems

    def size(self):
        return len(self._elems)

    def __len__(self):
        return len(self._elems)

    def __add__(self, other):
        new_toy = Toy()
        new_toy._elems = self._elems + other._elems
        return new_toy

    def __eq__(self, other):
        return self._elems == other._elems

    def __str__(self):
        return str(self._elems)

    def __hash__(self):
        return id(self)


t1 = Toy()
t2 = Toy()
t1.add([1, 2])
t2.add([3, 4])
t3 = t1 + t2
print(f'The value of t3 is {t3}')
print(f'The length of t3 is {len(t3)}')
d = {t1: 'A', t2: 'B'}
print(f'The value of {d[t1]} is associated with the key t1 in d.')

print(type(Toy))
print(type(Toy.__init__))
print(type(Toy.add))
print(type(Toy.size))

s = Toy()
sample = [1, 2, 3]
s.add(sample)
print(s._elems)


class Person(object):
    def __init__(self, name):
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank + 1:]
        except:
            self._last_name = name

        self.birthday = None

    def get_name(self):
        return self._name

    def get_last_name(self):
        return self._last_name

    def set_birthday(self, birthday):
        self._birthday = birthday

    def get_age(self):
        if self._birthday == None:
            return ValueError

        return (datetime.date.today() - self._birthday).days

    def __lt__(self, other):
        if self._last_name == other._last_name:
            return self.name < other.name
        return self._last_name < other._last_name

    def __str__(self):
        return self._name


me = Person('Michael Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print(him.get_last_name())
him.set_birthday(datetime.date(1961, 8, 4))
her.set_birthday(datetime.date(1958, 8, 16))
print(him.get_name(), 'is', him.get_age(), 'days old')

pList = [me, him, her]

for p in pList:
    print(p)

pList_sort = sorted(pList)

for p in pList_sort:
    print(p)

his_name = 'Barack Hussein Obama'
print(his_name[his_name.rindex(' ') + 1])


#  inheritance
class mit_person(Person):
    _next_id_num = 0

    def __init__(self, name):
        super().__init__(name)
        self._id_num = mit_person._next_id_num
        mit_person._next_id_num += 1

    def get_id_num(self):
        return self._id_num

    def __lt__(self, other):
        return self._id_num < other._id_num


p1 = mit_person('Barbara Beaver')
print(str(p1) + '\'s id number is ' + str(p1.get_id_num()))

p1 = mit_person('Mark Guttag')
p2 = mit_person('Billy Bob Beaver')
p3 = mit_person('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

print(p1._id_num)
print(p2._id_num)
print(p3._id_num)

#  Encapsulation and Information Hiding


class Grades(object):
    def __init__(self):
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        try:
            return self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def get_grade(self, student):
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')

    def get_students(self):
        if not self._is_sorted:
            self.students.sort()
            self._is_sorted = True
        return self._students[:]
