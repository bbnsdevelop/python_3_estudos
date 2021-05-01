
class Casa(object):
    def __init__(self):
        self.__portas = 4
        self.__janelas = 6
    
    def getPortas(self):
        return self.__portas
    
    def setPortas(self, portas):
        self.__portas = portas

if __name__ =="__main__":
    mansao = Casa()
    print(mansao.getPortas())
    mansao.setPortas(20)
    print(mansao.getPortas())
    