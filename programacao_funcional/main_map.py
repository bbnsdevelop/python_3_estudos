#!/usr/bin/python
# coding: utf-8

temp = [9,22,30,110]

def fahrenheit(T):
    return (9/5) * T + 32

temp_calc = list(map(fahrenheit, temp))

print(temp_calc)

# ou

temp_calc = list(map(lambda t: (9/5) * t + 32, temp))
print(temp_calc)

