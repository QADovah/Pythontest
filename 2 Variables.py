# Variables 
# Con guiones bajos si hay espacios entre palabras, y todo en minusculas.


my_variable = "Mi texto variable"
print(my_variable)

my_int_variable = 123
print(my_int_variable)


my_bool_variable = True
print(my_bool_variable)


#concatenación de variables
print(my_bool_variable,",", my_int_variable,",",my_bool_variable)


type(print(my_variable))
#my_int_variable = 5
#print(my_int_variable)
#print(my_bool_variable, str(my_int_variable), my_variable)


#Se imprime el tipo de dato print. Pero como es función, no devuelve tipo de dato valido. 
print(type(print(my_variable)))


#Imprime la cantidad de caracteres de la variable.
print(len(my_variable))



#Variables en una sola linea. 
nombre, apellido, alias, edad = "Federico", "Astray", "Kala", 38
print (nombre, apellido, alias, edad)

nombre = input("Identifiques con el nombre:")
edad = input("Ingrese la edad:")
address: str = "Sanchez 2011"
print("Gracias, usted ha sido identificado como:", nombre, apellido, "con el alias de:", alias, "y actualmente tiene", edad, "años de edad, y la dirección asignada como constante es:", address)