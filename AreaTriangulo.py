base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))

def calcularArea(base, altura):
    area = (base*altura)/2
    return area
resultado = calcularArea(base, altura)
#resultado_entero = int(resultado)

print(f"el area del triangula de base {base} y de altura {altura} es de: {resultado}")

