# coding=utf-8

# -*- coding: utf-8 -*-


# se assemelham bastante com listas


t1 = (1, 2, 3, 4)
t = ('one', 2, 123, [1, 9, 8])


print(type([1, 2, 3]) == list)

for index in t:
    if isinstance(index, str):
        print('Não é numero -> ' + index)
    else:
        if type(index) == list:
            for i in index:
                print('é numero -> ' + str(i))
        else:
            print('é numero -> ' + str(index))
