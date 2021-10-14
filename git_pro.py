def hello():
    return "Hello World!"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"Your name is {self.name} and you're {self.age} years old"



henkilo = Person("JP", 20)
print(henkilo)
