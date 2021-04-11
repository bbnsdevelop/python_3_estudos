class Pessoa:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_people(self):
        formatted = 'Name: {}, Age: {}'.format(self.name, self.age)
        print(formatted)
