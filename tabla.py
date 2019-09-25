numero=input("Ingresa un numero del 1 al 9:")
numero=int(numero)
#ciclo para ejecutar una serie de numero determinados
#no se pone el numero de terminacion ya que solo seria del 1 al 10
for v in range (1,11):
    #v cambia constantemente
    salida="{} x {} = {}"
    print (salida.format(numero,v,v*numero))