#LISTAS

my_list=[50, 20, 35, 45, 55]
mi_other_list=[21, 1.60, "lenin", "correa"]
print(mi_other_list)
print(len(mi_other_list))
print(type(mi_other_list))
print(mi_other_list.count(21))
print("-----------------------------")





#de adelante a atras
print(mi_other_list[3])
#de atras a adelante
print(mi_other_list[-3])
print("-----------------------------")




#deb coincidir con los elementos de la lsita
age, heigth, name, surname=mi_other_list
print(name)

name, age, heigth, surname=mi_other_list[2], mi_other_list[0], mi_other_list[1], mi_other_list[3]
print(age)
print("-----------------------------")




#union de listas
print(my_list + mi_other_list)
print("-----------------------------")





#operaciones en la lista
my_list.append("devsoft")
print(my_list)

my_list.insert(2, "Azul")
print(my_list)

my_list.remove("Azul")
print(my_list)

my_list.pop()
print(my_list)

#elimina por indice
del my_list[0]
print(my_list)

#copia la lista
my_new_list=my_list.copy()
print(my_new_list)

#lista en reversa
my_new_list.reverse()
print(my_new_list)

#ordena mayor a menor
my_new_list.sort()
print(my_new_list)

#imprime lo que haya entre los elementos 1 y 3
print(my_new_list[1: 3])

#limpia la lista
my_list.clear()
print(my_list)
