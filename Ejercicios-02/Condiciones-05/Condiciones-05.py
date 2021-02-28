# Condiciones 05
"""
5.- Escribe un programa que pida tres números y que escriba si son los tres iguales,
si hay dos iguales o si son los tres distintos.
"""

try:
    num1=(int(input("Dame un primer numero: ")))
    num2=(int(input("Dame un segundo numero: ")))
    num3=(int(input("Dame un tercer numero: ")))
except:
    print("Algo fallo, lmao")
else:
    if (num1 == num2 == num3):
        print("Los tres numeros son iguales")
    elif (num1==num2 or num2 == num3 or num3 == num1):
        if(num1==num2):
            print("El primer y segundo numero son iguales")
        elif(num2==num3):
            print("El segundo y tercer numero son iguales")
        elif(num3==num1):
            print("El tercer y primer numero son iguales")
    else:
        print("Ninguno es igual lmao")