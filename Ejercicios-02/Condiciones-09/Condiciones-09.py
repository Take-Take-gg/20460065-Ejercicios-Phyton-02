# Condiciones 09
"""
9.- Escribe un programa que pida una distancia en centímetros y que escriba esa
distancia en kilómetros, metros y centímetros (escribiendo todas las unidades).
"""
try:
    km = m = 0
    cm = int(input("dame una distancia entera en centimetros y yo te digo cuantos km, m y cm tiene: "))
    Centi=cm

except ValueError:
    print("Valor no admitido, chao chao")
else:
    
    if cm >= 1000:
        km = cm // 1000
        cm = cm - (km *1000)

    if cm >= 100:
        m = cm //100
        cm = cm - (m*100)

    print(f"En {Centi} centimetros Hay: {km} km, {m} m, y {cm} cm en ")