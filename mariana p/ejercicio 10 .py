saldo=int(input("ingresa saldo actual: "))
salRe=int(input("Cuanto vas a retirar: "))
if saldo >= salRe:
    print ("Retiro exitoso")
else:
    print("Error: Saldo insuficiente")