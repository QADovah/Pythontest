def calcular_area():
    opcion = int(input("Ingresa 1 para calcular el área de un cuadrado o 2 para un triángulo: "))

    if opcion == 1:
        lado = float(input("Ingresa la longitud del lado del cuadrado: "))
        area = lado ** 2
        print(f"El área del cuadrado es: {area} unidades cuadradas.")
    elif opcion == 2:
        base = float(input("Ingresa la longitud de la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = 0.5 * base * altura
        print(f"El área del triángulo es: {area} unidades cuadradas.")
    else:
        print("Opción no válida. Por favor, ingresa 1 o 2.")

calcular_area()