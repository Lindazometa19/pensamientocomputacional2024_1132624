# Numero 3

palabra= ['agua', 'cocacola', 'jamaica','horchata','sprite''1988','fanta','uva']
palabra=input("introduce una palabra: ")
conteo = palabra.count(palabra)
print(f"la palabra '(palabra)'aparece '(conteo)' veces en la lista")

# Numero 2

abecedario = list ('abcdefghijklmnñopqrstuvwxyz')
def eliminar_multiplos_de_tres(lista) :
    return [letra for i, letra in enumerate(lista, start =1)if i % 3 ! = 0]
lista_resultante = eliminar_multiplos_de_tres(abecedario)
print("listaresultante: ", lista_resultante)


# Numero 1
precios = [50,75,46,22,80,65,8]
def obtener_mayor_precio(lista) : 
    mayor= lista [0]
    for precio in lista :
        if precio < mayor :
            mayor = precio 
            return mayor 
        def obtener_menor_precio(lista) : 
            menor= lista [0]
            for precio in lista :
                if precio < menor :
                    menor = precio 
                    return menor
                mayor_precio =
                obtener_mayor_precio(precios)
                menor_precio=
                obtener_menor_precio(precios)
                print("el mayor precio es:", mayor_precio)
                print("el menor precio es: ", menor_precio )
                

        