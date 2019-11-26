class Person:
    def __init__(self, p_name, p_age):
        self.name = p_name
        self.age = p_age

    def get_age(self):
        print(self.age)

    def get_name(self):
        print(self.name)


class Student(Person):
    def __init__(self, name, age, percentage):
        Person.__init__(self, name, age)
        self.percent = percentage

    def get_percent(self):
        print(self.percent)


p = Person("Deepak", 30)
p.get_age()
p.get_name()

s = Student("Deepak", 15, "99.9")
s.get_name()
s.get_age()
s.get_percent()


class CarA:
    def __init__(self):
        super().__init__()
        self.car = "CarA"
        self.gears = 5


class CarB:
    def __init__(self):
        super().__init__()
        self.car = "CarB"
        self.gear = "Automatic"


class CarC(CarB, CarA):
    def __init__(self):
        super().__init__()

    def get_car(self):
        return self.car


c = CarC()
print(c.get_car())
print(CarC.__mro__)


class MetaClass:
    pass


mc = MetaClass()

print(type(mc))

print(type(MetaClass))

print(type(type))
