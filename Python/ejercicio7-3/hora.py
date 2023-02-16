
import datetime

hora = datetime.datetime.now()

tiempo_de_trabajo = datetime.time(19, 0, 0)

horaactual = datetime.datetime.strftime(hora, '%H:%M')
print("La hora actual es " + horaactual)

if hora.time() > tiempo_de_trabajo:
    print("Son más de las 19:00 , ya se puede ir a casa")
else:
    tiempo_restante = datetime.datetime.combine(datetime.date.today(), tiempo_de_trabajo) - datetime.datetime.combine(datetime.date.today(), hora.time())
    print("Queda por trabajar " + str(tiempo_restante))
