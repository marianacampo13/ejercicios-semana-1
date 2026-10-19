valor = int(input("cuanto vale el producto: "))
pago = input("efectivo o tarjeta")
if pago == "efectivo":
    descuento=(valor*10)/100
    total=valor-descuento
    print("el total del producto es: ", total)
else:
    print("el total del producto es: ", producto)