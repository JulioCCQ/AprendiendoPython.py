#se declara variables int y str
acumulado=int(0)
numero=str("")
#En este ciclo se utiliza while with true
#como condicion en el cual se formara un ciclo
#infinito hasta que el numero sea vacio
# y se utilice el comando break
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        #Este imprime si el estatus esta vacío y sale
        print("Vacío. Salida de programa")
        break
    else:
        #Si se proporciona valor se suma para ser calculado
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))