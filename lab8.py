#numero1

# Solicitar al usuario las longitudes de los 3 lados del triángulo
A = float(input("Ingrese la longitud del lado A: "))
B = float(input("Ingrese la longitud del lado B: "))
C = float(input("Ingrese la longitud del lado C: "))

# Determinar el tipo de triángulo
if A == B and B == C:
    print("El triángulo es equilátero.")
elif A == B or A == C or B == C:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
    
#numero2

def multiplicar_sin_multiplicar(a, b):
    # Inicializar el resultado
    resultado = 0
    
    # Si alguno de los números es negativo, hacer una lógica para manejar los signos
    negativo = False
    if a < 0:
        a = -a
        negativo = not negativo
    if b < 0:
        b = -b
        negativo = not negativo

    # Sumar 'a' a sí mismo 'b' veces
    for _ in range(b):
        resultado += a

    # Ajustar el signo del resultado si es necesario
    if negativo:
        resultado = -resultado

    return resultado

# Solicitar al usuario los dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Llamar a la función y mostrar el resultado
resultado = multiplicar_sin_multiplicar(num1, num2)
print(f"El resultado de {num1} multiplicado por {num2} es: {resultado}")


#numero 3

def calcular_promedio_edades():
    n = int(input("Ingrese la cantidad de edades: "))
    

    if n <= 0:
        print("La cantidad de edades debe ser un número positivo.")
        return

    # Inicializar la suma de las edades
    suma_edades = 0

    for i in range(n):
        edad = int(input(f"Ingrese la edad {i + 1}: "))
        suma_edades += edad

    # Calcular el promedio
    promedio = suma_edades / n

    # Mostrar el promedio
    print(f"El promedio de las edades ingresadas es: {promedio:.2f}")

# Llamar a la función para ejecutar el algoritmo
calcular_promedio_edades()

#numero4

def es_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

# Solicitar al usuario un número
num = int(input("Ingrese un número: "))

if es_primo(num):
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")



