# COndiciones 07
"""
7.-Escribe un programa que contenga una función que reciba los coeficientes de
una ecuación de segundo grado (a x2 + b x + c = 0) y retorne la solución.
Se recuerda que una ecuación de segundo grado puede no tener solución, tener
una solución única, tener dos soluciones o que todos los números sean solución.

Se recuerda que la fórmula de las soluciones cuando hay dos soluciones 
es x = (-b ± √(b2-4ac) ) / (2a)
"""
import math

print("Te daremos la solucion de (ax^2 + bx + c = 0)")
a = float(input("Dame el valor de a: "))
b = float(input("Dame el valor de b: "))
c = float(input("Dame el valor de c: "))

# x = (-b ± √(b**2-4ac) ) / (2a)
def segundo_grado (a,b,c):
    primera_parte = (b**2 - 4*a*c)
    if(a == 0 and b == 0 and c == 0):
        return"Todos los numeros son solucion"
    elif (a == 0 and b == 0):
        return "Sin solucion"
    elif primera_parte == 0:
        # Se trata de una sola solucion
        x = -b / 2*a
        return f"El unico valor es: {x}"
    elif primera_parte < 0:
        # Sin solucion real
        return "Sin solucion real"
    elif (a == 0):
        x = -c/b
        return f"El unico valor es: {x}"
    else:
        # Dos soluciones
        # print(round(math.sqrt(10),2))
        # x = (-b ± √(b**2-4ac) ) / (2a)
        raiz = round(math.sqrt(primera_parte),3)
        primera_solucion = (-b + raiz)/(2*a)
        segunda_solucion = (-b - raiz)/(2*a)
        return f"El primer resultado es: {primera_solucion} \nEl segundo resultado es: {segunda_solucion}"

print(segundo_grado(a,b,c))

# Ta bien
# x = (-b ± √(b**2-4ac) ) / (2a)
# raiz (49 - 24) = 5
# x1 = -7 + 5 = 2 / 2 * a == 2 / 4 = .5
# x2 = -7 -5 = -12 / 2 * a == -12 / 4 = -3