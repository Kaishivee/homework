grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

pup = sorted(students)

grade_list1 = []
for i in grades:
    aver = round(sum(i) / len(grades))
    grade_list1.append(aver)

dict(zip(pup, grade_list1))
print(dict(zip(pup, grade_list1)))