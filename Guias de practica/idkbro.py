#configuracion inicial
agente = 'encargado'
platillo = []
precios = []

# Ingreso a la aplicacion
name = input("Ingrese el nombre del agente: ")
while name.lower() != agente:
    print("Agente no registrado")
    name = input("Favor ingrese el nombre del agente: ")
    
# Gestion del menu princial
OpcionesIniciadas = True

while OpcionesIniciadas:
    print("Seleccione una opcion: 1.Creación de platillos.  2.Consulta de platillos y precios.  3.Colocar un pedido.  4.Salir")
    seleccion = int(input())
    
    if seleccion == 4: # Salir 
        OpcionesIniciadas = False
        print("Gracias por usar este servicio!")
    elif seleccion == 1: #Creación de platillos
        platillo.append(input("Ingrese el nombre del platillo a crear: ").lower())
        precios.append(float(input("Ingrese el precio del platillo a crear: ").lower()))
         
    elif seleccion == 2: #Consulta y precios
        if len(platillo) == 0:
            print("Actualmente no hay platillos ingresados")
        else:
            for i in range(len(platillo)):
                print(f"{platillo[i]}: ${precios[i]:.2f}")
            
    elif seleccion == 3: #Colocar un pedido
        EleccionPedido = input("Indique el nombre del platillo para su orden: ")
        if EleccionPedido.lower() in platillo:
            number = platillo.index(EleccionPedido.lower())
            print(f"Usted ha elegido {platillo[number]} con un precio de ${precios[number]:.2f}")
        else:
            print("Ese platillo no existe actualmente")
    else:
        print("Opción no válida")
    