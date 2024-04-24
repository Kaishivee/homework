x = 55
print("hey")
if x < 0:                           #условие не выполняется, т.к. 55>0
    print('below zero')
print('bye')



a, b = 2, 12

if a > b:
    print('a > b')     #условие не выполняется, т.к. 2<12

if a > b and a > 0:
    print('right')         #условие не выполняется, т.к. False and True

if (a < b) and (a > 0 or b < 1000): #условие выполняется, т.к. True and True
    print('right')

if 12 <= b and b < 10:             #условие не выполняется, т.к. True and False
    print('right')



if '23' > '124':
    print('success')

if '124' > '12':
    print('success')

if [3, 5] > [4, 1]:            #условие не выполняется, т.к. 3<4
    print('success')



if 'peace' > [2,6]:         #нельзя сравнивать разные типы данных
    print('OK')

if 'grape' != 1:            #нельзя сравнивать разные типы данных
    print('OK')

if [1,2,3] <= 123:          #нельзя сравнивать разные типы данных
    print('OK')