#Esta variable  almacena un dato 
numero=int(input("Dame un numero entero: "))
#Se almacen el valor proporcionado y 
# si es el residuo cero se da como numero multiplo
Multiplo3=((numero%3)==0)
Multiplo5=((numero%5)==0)
Multiplo7=((numero%7)==0)
#En las siguientes lineas se utiliza las tablas de verdad
#"OR" y "AND" cada una con sus condiciones
if ((Multiplo3 and Multiplo5) or Multiplo7 ):
    print ("Correcto.")
else:
        print ("Incorrecto.")
