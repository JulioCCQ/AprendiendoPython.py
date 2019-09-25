import random
#variable tipo float  con un valor
num1=float(10.5)
#Se declara la funcion con la que se trabajara y hara el proceso
def aleatorio():
    num2=float(random.randrange(1,10))
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(num1,num2,num1+num2))


aleatorio()