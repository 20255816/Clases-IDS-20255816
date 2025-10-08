nombre = "Ernesto"
print(nombre)

edad = 18
ciudad = "San Salvador"
profesion = "no lo se" 
print(edad,ciudad,profesion)
# una variable sirve para crear una lista de datos, guardarlos y usarlos despues
newmsg = "Bienvenido al curso de Python"
print(newmsg)
anio_actual = 2025
anio_nacimiento = 2006
print(anio_actual-anio_nacimiento)
Pi = 3.14159265359 
print(f"El valor de Pi es:{Pi:.4f}")
# una variable entera guarda números, una cadena texto

#Sección 2 - Del usuario

print("Sección de usuario...")
usrname = input("Hola, ¿cuál es tu nombre?: " )
print(f"Bienvenido, {usrname}")
usrage = int(input("Cuál es tu edad: "))
print(f"El doble de tu edad sería: {usrage*2}, jaja xd")

entero1 = int(input("Dame un número entero: "))
entero2 = int(input("Dame otro número entero: "))
print(f"La suma de estos 2 enteros sería: {entero1 + entero2}")

decimal1 = float(input("Ahora dame un decimal: "))
print(f"La mitad de ese decimal es: {decimal1 / 2} ")
entero3 = int(input("dame un número entero: "))
print(f"Eso al cuadarado es: {entero3**2}")

nprom1, nprom2 = input("Dame 2 números sepadados por coma: ").split(",")
nprom1 = int(nprom1)
nprom2 = int(nprom2) 
print(f"El promedio de esos números es: {(nprom1 + nprom2) / 2}" )
