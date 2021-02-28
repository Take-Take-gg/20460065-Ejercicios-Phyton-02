# Condiciones 03
"""
3. - Escribe un programa que pida dos números y que conteste cuál es el menor y
cuál el mayor o que escriba que son iguales.
"""

try:
    num1=(float(input("Dame un primer numero: ")))
    num2=(float(input("Dame un segundo numero: ")))
except:
    print("Algo fallo, lmao")
else:
    if num1 > num2:
        print(f"El numero {num1} es mayor que {num2}.")
    elif num1 < num2:
        print(f"El numero {num1} es menor que {num2}.")
    elif num1==num2:
        print("Son los mismos numeros")