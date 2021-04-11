class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def show_data(self):
        dia_format = "0"+str(self.dia) if self.dia < 10 else self.dia
        mes_format = "0"+str(self.mes) if self.mes < 10 else self.mes
        print(f'{dia_format}/{mes_format}/{self.ano}')

    def __str__(self):
        dia_format = "0" + str(self.dia) if self.dia < 10 else self.dia
        mes_format = "0" + str(self.mes) if self.mes < 10 else self.mes
        return f'{dia_format}/{mes_format}/{self.ano}'


d1 = Data(1, 5, 2021)
d1.dia = 23
d2 = Data(d1.dia, d1.mes, d1.ano)
d2.dia = 24
d1.show_data()
d2.show_data()
print(d2)
