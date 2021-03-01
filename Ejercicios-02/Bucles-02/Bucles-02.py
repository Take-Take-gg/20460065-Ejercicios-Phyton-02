# Bucles 02
"""
2.- Escriba un programa que pida un número entero mayor que cero y que escriba
sus divisores.
"""
try:
    num = int(input("Dame un numero mayor que 0 y te digo sus divisores: "))
    if num <= 0:
        print("Que fue lo que te dije?")
    else:
        def prop(num):
            lista = []
            for i in range(1,num):
                if num % i == 0:
                    lista.append(i)
            lista.append(num)
            return lista

        print(f"Los divisores de {num} son: {prop(num)}")
except:
    print("Valio maiz")
