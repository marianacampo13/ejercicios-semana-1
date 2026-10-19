tarjeta = int(input("ingresa saldo de la tarjeta: "))
cupo=int(input("cuanto tienes de cupo: "))
if tarjeta  <= cupo:
    print ("Transaccion aprobada")
else:
    print("Transaccion rechazada por cupo insuficiente")