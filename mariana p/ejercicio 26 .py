hora = int(input("dame la hora actual(hora de 0 a 23): "))
if hora >= 6 and hora <= 18:
    print("Turno diurno") # nos muestra si tiene horario diurno o nocturno 
else:
    print("Turno nocturno")