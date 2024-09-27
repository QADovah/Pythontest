#Esta es una calculadora de AREA.
#La idea es que el usuario ingrese sus datos, y luego con la autenticación, pueda calcular en principio el area de un cuadrado, rectangulo, y si estoy motivado, un circulo





#usuario = input("Bienvenido, por favor ingrese su nombre para autenticarse: ")

base = 1
altura = 1
unidad_de_medida = "a"


#print("Hola", usuario, ". Este programita de consola es una calculadora de área. Esperemos que te resulte util.")
print("Seleccione que tipo de figura desea calcular: \n Las opciones son: ")
clase = input("\n 1: Cuadrado \n 2: triangulo \n 3: circulo \n")
if (clase) == 1:
    print("Usted ha seleccionado que desea calcular el area de un cuadrado")
    base == float(input("Ingrese la Base: "))
    print("La base ingresada es ", base)
    altura = float(input("Ingrese la altura: "))
    area = float(base * altura)
    print("El area del cuadrado con las medidas ingresadas es de ", area, "centimetros")
    
print("Usted ha seleccionado la opción  ")
      


##elif clase == 2:
##    base = float(input("Ingrese la Base de lo que quiere calcular: "))
##    print("La base ingresada es ", base)
#    altura = float(input("por favor ingrese la altura para completar la operación: "))
#    area = float(base * altura) /2
#    print("El area del triangulo con las medidas ingresadas es de ", area, "centimetros")




##
#base = float(input("Ingrese la Base de lo que quiere calcular: "))
#print("La base ingresada es ", base)
#
#altura = float(input("por favor ingrese la altura para completar la operación: "))
#area = float(base * altura)
#print("El area de la figura con las medidas ingresadas es de ", area, "centimetros")
##
