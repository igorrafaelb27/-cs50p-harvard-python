class Wizard:
    def __init__(self, name):
        if not name: raise ValueError("Name cannot be empty")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)  # Call the parent class's __init__ method
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the parent class's __init__ method
        self.subject = subject

    ...

wizard = Wizard("Albus Dumbledore")
student = Student("Harry Potter", "Gryffindor")
professor = Professor("Severus Snape", "Potions")



