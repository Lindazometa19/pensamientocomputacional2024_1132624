dormitorio = {"1" : "22",
           "2" : "22",
           "3" : "22",
           "4" : "22",
           "5" : "22",
           "6" : "22",
           "7" : "22",
           "8" : "22",
           "9" : "22",
           "10" : "22",
           "11" : "22",
           "12" : "22",
           "13" : "22",
           "14" : "22",
           "15" : "22",
           "16" : "22",
           "17" : "22",
           "18" : "22",
           "19" : "22",
           "20" : "22",
           "21" : "22",
           "22" : "22",
           "23" : "22",
           "24" : "22",
           
           
           
           }

sala = {"1" : "22",
           "2" : "22",
           "3" : "22",
           "4" : "22",
           "5" : "22",
           "6" : "22",
           "7" : "22",
           "8" : "22",
           "9" : "22",
           "10" : "22",
           "11" : "22",
           "12" : "22",
           "13" : "22",
           "14" : "22",
           "15" : "22",
           "16" : "22",
           "17" : "22",
           "18" : "22",
           "19" : "22",
           "20" : "22",
           "21" : "22",
           "22" : "22",
           "23" : "22",
           "24" : "22",
           }

cocina = {"1" : "22",
           "2" : "22",
           "3" : "22",
           "4" : "22",
           "5" : "22",
           "6" : "22",
           "7" : "22",
           "8" : "22",
           "9" : "22",
           "10" : "22",
           "11" : "22",
           "12" : "22",
           "13" : "22",
           "14" : "22",
           "15" : "22",
           "16" : "22",
           "17" : "22",
           "18" : "22",
           "19" : "22",
           "20" : "22",
           "21" : "22",
           "22" : "22",
           "23" : "22",
           "24" : "22",
           }

salas = {
    "dormitorio": dormitorio, 
    "sala": sala, 
    "cocina": cocina
}

historial_modificaciones = {
    "dormitorio": [],
    "sala": [],
    "cocina": []
}

seguir = True
while seguir == True:
    print("""
    1. configurar temperatura del día para un espacio
    2. modificar una hora específica
    3. ver historial de modificaciones
    4. mostrar el horario con las temperaturas configuradas actuales
    """)

    menu = input("Que desea hacer? ")
    if menu == "1":
        espacio = input("en que espacio desea modificar? ")
        temp = input("A que temperatura quiere?: ")
        if espacio in salas:
            for i in salas[espacio]:
                salas[espacio][i] = temp
                historial_modificaciones[espacio].append(f"Se configuró todo el día a {temp}°")




        print("dorm: ",dormitorio, "cocina: ",cocina, "sala: ",sala)


    if menu == "2":
        espacio = input("en que espacio desea modificar? ")
        cambio = input("A que hora desea el cambio?: ")
        temp = input("A que temperatura quiere?: ")
        if espacio in salas and cambio in salas[espacio]:
            
                    salas[espacio][cambio] = temp
                    historial_modificaciones[espacio].append(f"La hora {cambio}:00 se cambió a {temp}°")
                    
        print("dorm: ", dormitorio, "cocina: ", cocina, "sala: ", sala)

    elif menu == "3":
        espacio = input("¿De qué espacio desea ver el historial? ")
        
        if espacio in historial_modificaciones:
            print(f"El historial de modificaciones para {espacio} es:")
            
            for registro in historial_modificaciones[espacio]:
                print(registro)
        else:
            print("Ese espacio no está registrado, ingrese uno que si")
            
    elif menu == "4":
        
        print("Dormitorio:")
        
        for clave, valor in dormitorio.items():
            print(f"{clave}:00 - Temperatura: {valor}°")
        print("Sala:")
        
        for clave, valor in sala.items():
            print(f"{clave}:00 - Temperatura: {valor}°")
        print("Cocina:")
        
        for clave, valor in cocina.items():
            print(f"{clave}:00 - Temperatura: {valor}°")

    desea_seguir = input("desea seguir? ")
    if desea_seguir == "":
        seguir = False

