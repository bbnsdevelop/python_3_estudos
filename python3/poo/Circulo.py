class Circulo(object):
    pi = 3.14

    def __init__(self, raio = 1):
        self.raio = raio
    
    def area(self):
        return self.raio **2 * self.pi
    
    def setRaio(self, raio):
        self.raio = raio
        
    def getRario(self):
        return self.raio