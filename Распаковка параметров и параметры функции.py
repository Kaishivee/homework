def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
# print_params('nice', 2, 3, True, 2.3) -------> #ошибка, т.к. кол-во аргументов не соответствует кол-ву параметров)

print_params(b = 25) #работает, т.к. а=1, с=True (параметры по умолчанию), а значение параметра 'b' изменилось
print_params(c = [1,2,3]) #работает, т.к. а=1, b='строка' (параметры по умолчанию), а значение параметра 'с' изменилось

values_list = ['nature', False, 23]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'elevator']  # работает, т.к. a=2, b='elevator', c=42
print_params(*values_list_2, 42)