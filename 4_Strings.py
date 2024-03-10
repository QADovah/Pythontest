##Strings##

mi_string = "Lo que va en el string" #
mi_otro_string = "Lo que va en el 2do string" #
mi_string_numerico = "123"
mi_escapado = "\tEste string es \n escapado"

print(len(mi_string))

print(len(mi_otro_string))

print(mi_string + ". " + mi_otro_string)

print(3 + (float(mi_string_numerico))) #el string numerico que esta como texto, lo paso a float y lo convierto a float, y lo sumo.

print(mi_escapado)


########################

#FORMATEO#

name, surename, age = "Federico", "Astray", 38
#print ("Mi nombre es", name, surename, age)

print ("Mi formato es, {} {} {}".format(name, surename, age))
##print ("Mi 2do formato es %s %s y mi edad es %d" %(name, surename, age)) #Se tiene que definir el simbolo % y luego la s minuscula, y luego del string % y entre parentesis las variables que se le pasan. ESTA ES LA MEJOR OPCION. O LA DE ARRIBA
print ("Mi 2do formato es %s %s y mi edad es %d" %(name, surename, (age))) #Se tiene que definir el simbolo % y luego la s minuscula, y luego del string % y entre parentesis las variables que se le pasan
print (f"Mi 3er formato es {name} {surename} y mi edad es {age}") #Esta tambien es muy buena forma de ver que se esta infiriendo  (LA F va adelante)


#Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f =  language
print(a)
print(b)
#En este caso imprimiria "P" y despues la "y".

#División
nombre = "Nombre"
language_slice= nombre[0:5]
print(language_slice) #En este caso imprime los caracteres desde la posición 0 hasta la posición 5

#Reversed

reversed_language = language [::-1]
print(reversed_language)