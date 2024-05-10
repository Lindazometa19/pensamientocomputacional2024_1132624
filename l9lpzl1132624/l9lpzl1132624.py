#numero 1

def main():
    edad = int(input("ingresa tu edad: "))
    if edad > 18:
        print("Debes tramitar tu DPI")
    else:
        print("Eres menor .")
if __name__ == "__main__":
    main()


#numero 2 

def main():
    numero = float(input(" ingresa un número: "))
    if numero > 0:
        print("El número", numero, "es positivo.")
    elif numero < 0:
        print("El número", numero, "es negativo.")
    else:
        print("El número es cero.")
if __name__ == "__main__":
    main()


#numero 3

def main():
    numero = int(input(" ingrese un número del 1 al 5: "))
    numeros_letras = {
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
        5: "cinco"
    }
    if numero in numeros_letras:
        print("El número", numero, "en letras es:", numeros_letras[numero])
    else:
        print("Número no definido.")

if __name__ == "__main__":
    main()


#numero 4 

def main():
    numero = 2  

    print("Tabla de multiplicar del número", numero, ":")
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

if __name__ == "__main__":
    main()
