num = int(input("ingresa el año: "))
par=num%4
if par == 0: # nos muestra que año es bisiesto 
    print("Es un año bisiesto")
else:
    print("No es bisiesto")