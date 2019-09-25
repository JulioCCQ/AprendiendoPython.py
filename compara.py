#Pides variables para hacer la comparacion
numero1=input("Numero 1: ")
numero2=input("Numero 2: ")
salida="Numeros proporcionados: {} y {}.{}."
if (numero1==numero2):
    #aqui entra los numeros capturados si son iguales o no
    print(salida.format(numero1,numero2,"Los numeros son iguales"))
     #Este ciclo retorna  cual es mayor que el otro
else:
    if numero1>numero2:
        print(salida.format(numero1,numero2,"El mayor es el primero"))
    else:
        print(salida.format(numero1,numero2,"El mayor es el segundo"))
