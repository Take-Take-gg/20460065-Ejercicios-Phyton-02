# Bucles 05
"""
5.- Escriba un programa que pregunte cuántos números se van a introducir, pida
esos números, y escriba el mayor, el menor y la media aritmética.
"""

try:
    num= int(input("Te muestrare el mayor, el menor y la media aritmetica,\
         \nEscribe cuantos numeros quieres agregar: "))
    lista = []

    for i in range(num):
        registro = float(input(f"Dame el valor del numero {(i+1)}: "))
        lista.append(registro)

    suma = 0
    mayor = menor = lista[0]
    for i in lista:
        if mayor < i:
            mayor = i
        if menor > i:
            menor = i
        suma+=i

    print(f"El numero mayor es: {mayor}, el menor es: {menor} y la media es: {suma/num}")

except:
    print("Algo salio mal lmao")