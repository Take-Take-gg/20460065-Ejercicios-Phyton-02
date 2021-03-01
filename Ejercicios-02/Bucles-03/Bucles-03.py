# Bucles 03
"""
3.- Escriba un programa que pregunte cuántos números se van a introducir, pida
esos números, y muestre un mensaje cada vez que un número no sea mayor que el
primero.
"""
try:
    num= int(input("Escribe cuantos numeros quieres agregar: "))
    lista = []
    for i in range(num):
        registro = int(input(f"Dame el valor del numero {(i+1)}: "))
        lista.append(registro)

    for i in lista:
        print (i, end=", ")
        if i < lista[0]:
            print(f"El numero {i} no es mayor que el primer numero ({lista[0]})", end=", ")
except:
    print("Algo salio mal lmao")