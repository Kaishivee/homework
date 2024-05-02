n = int(input("Введите натуральное число: "))  # ЗАДАЧА 1
for i in range(n, 0, -1):
    print('*' * i)
print()

a, b, c, d = 7, 10, 5, 6  # ЗАДАЧА 2
if (a, b, c, d < 10) or (a <= b) or (c <= d):
    print('', end='\t')
    for i in range(c, d + 1):
        print(i, end='\t')
    print('')
    for j in range(a, b + 1):
        print(j, end='\t')
        for k in range(c, d + 1):
            print(j * k, end='\t')
        print('')

print()

n = int(input('Введите натуральное число: '))  # ЗАДАЧА 3
int_ = 0
for i in range(1, n + 1):
    for j in range(i):
        int_ += 1
        print(int_, end=' ')
    print()

print()

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))  # ЗАДАЧА 4

if (a == b != c) or (a == c != b) or (b == c != a):
    print('Равнобедренный')
elif a == b == c:
    print('Равносторонний')
else:
    print('Разносторонний')

print()

a = int(input("Введите первое число: "))  # ЗАДАЧА 5
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if c < a < b:
    print(a)
elif c < b < a:
    print(b)
elif a < c < b:
    print(c)
else:
    print(':(')

print()

a = 'красный'  # ЗАДАЧА 6
b = 'синий'
с = 'желтый'

col1 = input("Введите первый цвет (красный/синий/желтый): ")
col2 = input("Введите второй цвет (красный/синий/желтый): ")

if (col1 == 'красный' and col2 == 'синий') or (col1 == 'синий' and col2 == 'красный'):
    print('фиолетовый :)')
elif (col1 == 'красный' and col2 == 'желтый') or (col1 == 'желтый' and col2 == 'красный'):
    print('оранжевый :)')
elif (col1 == 'желтый' and col2 == 'синий') or (col1 == 'синий' and col2 == 'желтый'):
    print('зеленый :)')
else:
    print(' УПС, ОШИБОЧКА ВЫШЛА :((( ')
