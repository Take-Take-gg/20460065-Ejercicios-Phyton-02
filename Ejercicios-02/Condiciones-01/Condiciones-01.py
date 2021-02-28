# Condiciones 01
"""
1.- Escribe un programa que pida dos números enteros y que calcule su división,
escribiendo si la división es exacta o no.
"""
"""
2.- Mejora el programa anterior haciendo que tenga en cuenta que no se puede
dividir por cero.
"""

try:
    num=(float(input("Dame un primer numero: ")))
    num2=(float(input("Dame un segundo numero: ")))
    res=num/num2
except ZeroDivisionError:
    print("No divido entre zero :P")
except:
    print("Error en alguna parte, bye")
else:
    if (res)%1==0:
        print("La division es exacta")
    else:
        print("La division NO es exacta")