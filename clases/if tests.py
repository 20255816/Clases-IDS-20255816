""""nota = int(input())

if nota == 10:
    print("Nice")
else:
    if nota >= 9:
        print("pro")
    else:
        if nota >=8:
            print("j")
        else:
            print("bro idk")"""
            
"""#aplicar impuestos de     
monto = float(input())
tipo = str(input("Ingrese el tipo (Local/Exportacion)"))
impuesto = 0 

if tipo.lower == "local" and monto > 500:
    impuesto = 0.1
elif tipo.lower == "export" and monto > 500:
    impuesto = 0.14"""
    
    
#usos del while
aprobacion = True 
while aprobacion:
    eleccion = input("Quieres seguir jugando? (Y/N)")
    
    if eleccion.lower == 'n':
        aprobacion = False
    else:
        print('No se que es eso we :v')
    
    
