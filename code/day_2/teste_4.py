class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        print(self.name)
        print(self.age)

p1 = Person("Fernando", 26)

print(p1.get_person())
