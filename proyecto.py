class Transmetro:
    def __init__(self):
        self.estaciones = {
            51: "Estación Javier",
            61: "Estación Trébol",
            71: "Estación Don Bosco",
            82: "Estación Plaza Municipal"
        }
        self.rutas = {
            (51, 61): 39,
            (51, 71): 18,
            (51, 82): 23,
            (61, 82): 8,
            (82, 51): 42
        }
        self.boletos_vendidos = {}
        self.ingresos = 0

    def mostrar_estaciones(self):
        print("Estaciones vigentes:")
        for codigo, nombre in self.estaciones.items():
            print(f"{codigo}: {nombre}")

    def comprar_boleto(self):
        print("Compra de boleto")
        partida = int(input("Ingrese el número de estación de partida: "))
        destino = int(input("Ingrese el número de estación de destino: "))
        if (partida, destino) not in self.rutas:
            print("La ruta ingresada no existe.")
            return

        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        embarazada = input("¿Está embarazada? (s/n): ").lower() == 's'

        distancia = self.rutas[(partida, destino)]
        precio = 1.50 + (distancia - 8) * 0.25 if distancia > 8 else 1.50
        if embarazada:
            precio = 0
        elif 15 <= edad <= 25:
            precio *= 0.75

        tiempo_viaje = distancia / 20
        print("\nDetalles del boleto:")
        print("Estación de partida:", self.estaciones[partida])
        print("Estación de destino:", self.estaciones[destino])
        print("Precio del boleto: Q", precio)
        print("Tiempo estimado de viaje:", tiempo_viaje, "horas")

        self.boletos_vendidos[(partida, destino)] = self.boletos_vendidos.get((partida, destino), 0) + 1
        self.ingresos += precio

    def mostrar_reportes(self):
        print("\nReportes:")
        for ruta, cantidad_boletos in self.boletos_vendidos.items():
            print(f"Ruta {self.estaciones[ruta[0]]} - {self.estaciones[ruta[1]]}: {cantidad_boletos} boletos")
        print("Total de ingresos: Q", self.ingresos)

    def ejecutar(self):
        while True:
            print("\nMenú:")
            print("1. Ver las estaciones existentes")
            print("2. Comprar boleto")
            print("3. Reportes")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.mostrar_estaciones()
            elif opcion == "2":
                self.comprar_boleto()
            elif opcion == "3":
                self.mostrar_reportes()
            elif opcion == "4":
                print("¡Gracias por utilizar el sistema de Transmetro!")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

# Inicializar y ejecutar el programa
transmetro = Transmetro()
transmetro.ejecutar()
