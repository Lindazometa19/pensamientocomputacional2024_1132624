# numero 1 

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    print("Ingrese las longitudes de los lados del triángulo:")
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        print("Las longitudes de los lados deben ser mayores que cero.")
    elif lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado1 + lado3 <= lado2:
        print("Las longitudes de los lados no forman un triángulo válido.")
    else:
        tipo = tipo_triangulo(lado1, lado2, lado3)
        print("El triángulo es:", tipo)

if __name__ == "__main__":
    main()


# numero 2 

import math

def obtener_perimetro(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

def obtener_area(radio):
    area = math.pi * radio ** 2
    return area

def obtener_volumen(radio):
    volumen = (4/3) * math.pi * radio ** 3
    return volumen

def main():
    radio = float(input("Ingrese el radio del círculo: "))

    perimetro = obtener_perimetro(radio)
    area = obtener_area(radio)
    volumen = obtener_volumen(radio)

    print("Perímetro de la circunferencia:", perimetro)
    print("Área de la circunferencia:", area)
    print("Volumen de la esfera:", volumen)

if __name__ == "__main__":
    main()


# Numero 3

def imprimir_nombre_mes(numero):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    if numero in meses:
        print("El mes correspondiente al número", numero, "es:", meses[numero])
    else:
        print("El número ingresado no es válido. Por favor, ingrese un número del 1 al 12.")

def main():
    numero = int(input("Ingrese un número del 1 al 12: "))

    imprimir_nombre_mes(numero)

if __name__ == "__main__":
    main()
