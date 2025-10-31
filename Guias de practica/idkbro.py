agente = 'encargado'
platillo = []
precios = []

#1
name = input("Ingrese el nombre del agente: ")
while name.lower() != agente:
    print("Agente no registrado")
    name = input("Favor ingrese el nombre del agente: ")
    
#2
OpcionesIniciadas = True

while OpcionesIniciadas:
    print("Seleccione una opcion: 1.Creación de platillos.  2.Consulta de platillos y precios.  3.Colocar un pedido.  4.Salir")
    seleccion = int(input())
    
    if seleccion == 4: # Salir
        OpcionesIniciadas = False
        print("Gracias por usar este servicio!")
    elif seleccion == 1: #Creación de platillos
        platillo.append(input("Ingrese el nombre del platillo a crear: "))
        precios.append(float(input("Ingrese el precio del platillo a crear: ")))
         
    elif seleccion == 2: #Consulta y precios
        if len(platillo) == 0:
            print("Actualmente no hay platillos ingresados")
        else:
            for i in platillo:
                print(i)
            
    elif seleccion == 3: #Colocar un pedido
        ()
    else:
        print("Opción no válida")
    