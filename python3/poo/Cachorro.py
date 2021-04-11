from poo.Animal import Animal


class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cachorro')

    def latir(self):
        print('Au Au')
