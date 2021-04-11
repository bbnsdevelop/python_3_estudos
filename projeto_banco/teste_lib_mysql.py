try:
    from mysql import connector
except ModuleNotFoundError as e:
    print('Errooooooooooooooo', e)
else:
    print('sucesoooooooooo')
