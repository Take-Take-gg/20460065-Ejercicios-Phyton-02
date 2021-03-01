# Bucles 01
"""
1.- Escribe una función que reciba una lista de 6 números enteros ingresados por
teclado e imprima cuales son pares, impares y a su vez si son primos o no.

al final retorna la suma de todos los números.
"""

# Manera fachera facherita de hacerlo

def propiedades(num):
    def primates(num):
        contador=0
        for i in range(1,num):
            if num % i == 0:
                contador += 1
        if num == 1:
            return "No es primo"
        elif contador == 1:
            return "es primo"
        else:
            return "NO es primo"  
    def pares(num):
        if num % 2 == 0:
            return "par"
        elif num % 2 ==1:
            return "impar"
        else:
            print("No deberias llegar hasta aqui")

    return (f"El numero {num} es {pares(num)} y {primates(num)}")

lista=[]
try:
    for i in range(0,6):
        numero=int(input("Dame un numero: "))
        lista.append(numero)

    for i in lista:
        print(propiedades(i))

    suma =0
    for i in lista:
        suma = suma +i
    print(f"La suma total es : {suma} y {propiedades(suma)}")

except:
    print("Hacedlo bien porfa, que me da amsiemdad")


# Manera convencional y bien de hacerlo, pero Nah
"""
def es_primo(num):
    contador=0
    for i in range(1,num):
        if num % i == 0:
            contador += 1
    if num == 1:
        print("El uno no se considera primo")
    elif contador == 1:
        print(f"El numero {num} es primo")
    else:
        print(f"El numero {num} no es primo")

def es_par_o_impar(num):
    if num % 2 == 0:
        print(f"El numero {num} es par")
    elif num % 2 ==1:
        print(f"El numero {num} es impar")
    else:
        print("No deberias llegar hasta aqui")

lista=[]
try:
    for i in range(0,6):
        numero=int(input("Dame un numero: "))
        lista.append(numero)

    for i in lista:
        es_primo(i)
        es_par_o_impar(i)

except:
    print("Hacedlo bien porfa, que me da amsiemdad")
"""