num1 = int(input("Cantidad de personas en el espacio publico: "))
num2 = int(input("aforo maximo de personas: "))
if num1 <= num2:
    print("Ingreso permitido")
else:
    print("Aforo completo, espere afuera")