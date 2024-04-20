immutable_var = "love", 1,2, False
print(immutable_var)
#immutable_var[0] = "hate"
#print(immutable_var)   нельзя изменить, т.к. кортеж - неизменяемый тип данных
mutable_list = ["Kostya", "Dasha", "Kris", 100, True]
mutable_list[2] = 6
mutable_list[3] = "Denis"
print(mutable_list)