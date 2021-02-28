# Condiciones 04
"""
4.- Escribe un programa que pida dos números enteros y que escriba si el mayor es
múltiplo del menor.
"""
try:
    num1=(int(input("Dame un primer numero: ")))
    num2=(int(input("Dame un segundo numero: ")))
except:
    print("Algo fallo, lmao")
else:
    if num1 > num2:
        print(f"El {num1} es mayor que el {num2}")
        if num1 % num2 == 0:
            print(f"Y el {num1} es multiplo de {num2}")
        else:
            print(f"Y el {num1} NO es multiplo de {num2}")
    elif num1 < num2:
        print(f"El {num2} es mayor que el {num1}")
        if num1 % num2 == 0:
            print(f"Y el {num2} SI es multiplo de {num1}")
        else:
            print(f"Y el {num2} NO es multiplo de {num1}")
    else:
        print("Apuesto a que son los mismos numeros :P")