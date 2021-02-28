# Condiciones 08
"""
8.- Escribe un programa que pregunte primero si se quiere calcular el área de un
triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un
triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura
y escribir el área. Si se contesta que se quiere calcular el área de un círculo
(escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el
área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.
"""
def main():
    print("Quieres calcular el area de un triangulo o circulo?")
    print("Escribir: T o t para trinagulo, C o c para circulo")
    res=input("Su respuesta -> ")
    # Puedo hacer que respuesta se convierta en minusculas, pero no lo hare
    print(mi_funcion(res))

def mi_funcion(res):
    if res=="T" or res == "t":
        base = float(input("Dame la base del triangulo: "))
        altura = float(input("Dame la altura del triangulo:"))
        return f"El area del triangulo es: {(base * altura /2)}"
    elif res=="C" or res == "c":
        radio = float(input("Dame el radio del circulo: "))
        return f"El area del circulo es: {radio ** 2 * 3.141592}"
    elif res == "no":
        return "A weno adios master"
    else:
        return "Valor no admitido"

main()