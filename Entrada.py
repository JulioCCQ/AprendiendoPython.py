entrada=input()
print(type(entrada))
#esta variable se encarga de verificar 
# si es entero y por ende sera 
# verdadero (true), si es decimal sera falso
entero=(entrada.isdigit() and entrada.find(".")==-1)
#Esta ciclo funcionara para retornar si es entero o no al usuario
if (entero):
    print ("El dato es entero. Muy bien!")
else:
    print ("Tu dato no es entero.Intentalo de nuevo")
