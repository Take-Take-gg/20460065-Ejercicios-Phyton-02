# Bucles 04
"""
4.- Escriba un programa que pregunte cuántos números se van a introducir, pida
esos números y escriba cuántos negativos ha introducido.
"""

try:
    num= int(input("Escribe cuantos numeros quieres agregar, te muestro los negativos: "))
    lista = []
    lista_negativa = []
    for i in range(num):
        registro = int(input(f"Dame el valor del numero {(i+1)}: "))
        lista.append(registro)


    print("Lista Normal: ")

    for i in lista:
        print (i, end=", ")
        if i < 0:
            lista_negativa.append(i)

    print("\b\b\nLista Negativa: ")

    for i in lista_negativa:
        print (i, end=", ")

    print(f"\b\b\nHay {len(lista_negativa)} numero negativos en total")
         
except:
    print("Algo salio mal lmao")