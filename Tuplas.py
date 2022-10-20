tupla = ('Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo')
 
indice = int(input("Un numero de la semana: "))
 
if indice>=0 and indice<len(tupla):
    print(tupla[indice])
else:
    print("No es un numero de la semana")
    