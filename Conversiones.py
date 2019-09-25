#Declaro la variable  str con numeros
numero="5678"
#La salida es un dato type
print (type(numero))
#Se convierte la cadena a  int
numero=int (numero)
#Se muestra como cambio el tipo de variable y se usa de nuevo
print (type(numero))
#Se sustituye donde  iran  los valores
impresion="El numero es {}"
print(impresion.format(numero))