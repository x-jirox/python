#variables

my_string_variable="Mi vriable string"
print(my_string_variable)

my_int_variable=5
print(my_int_variable)

my_float_variable=5.5
print(my_float_variable)

my_boolean_variable=True
print(my_boolean_variable)
print("-----------------------------")


#Concatenacion de variables en un print
print(my_string_variable, " , " ,my_int_variable," , " , my_float_variable, " , " , my_boolean_variable)
print("-----------------------------")


#variables utilizando str
my_int_variable_str=str(my_int_variable)
print(my_int_variable)
print(type(my_int_variable))
print("-----------------------------")


#funciones del sistema, cuenta la cadena
print(len(my_string_variable))
print("-----------------------------")


#concatenacion de variables con print
print("este es el integer de mi variable: ", my_int_variable)
print("-----------------------------")


#variables en una sola linea , no se debe abusar de esta centencia
first_name, second_name, alias, age= "Lenin","Correa","jiro",21
print ("Me llamo: ",first_name," ", second_name," , ","Mi alias es : ", alias," , ","Mi edad es : ", age)
print("-----------------------------")


#Uso de imputs
first_name_imput= input("what is your name: ")
age_input= input("What is your age: ")

print("Hello: ",first_name_imput)
print("Your age is: ",age)