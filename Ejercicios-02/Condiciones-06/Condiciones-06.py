# Condiciones 06
"""
6.- Escribe un programa que pida los coeficientes de una ecuación de primer grado
(a x + b = 0) y escriba la solución.

Se recuerda que una ecuación de primer grado puede no tener solución, tener una
solución única, o que todos los números sean solución. Se recuerda que la fórmula
de las soluciones es x = -b / a
"""
print("Te daremos la solucion de (a x + b = 0)")
a = float(input("Dame el valor de a: "))
b = float(input("Dame el valor de b: "))

if a == 0:
    print("Todos los numeros son solucion")
else:
    x = -b/a
    print(f"El valor de x es: {x}")
