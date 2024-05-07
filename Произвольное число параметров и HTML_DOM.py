def test(txt, *args, **values):
    print(txt)
    print(args)
    for key, value in values.items():
        print(key, value)


test('Распределение домашних обязанностей: ', 1, 2, 3, Dasha='стирка', Max='влажная уборка', Kostya='посуда')

print()


def recursion(n):
    if n == 1:
        return 1
    else:
        return n * recursion(n - 1)


print(recursion(4))