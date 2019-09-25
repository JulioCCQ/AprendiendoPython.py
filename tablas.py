for i in range (1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    print ()
    #solo salta una linea por mera estetica
    #Un ciclo dentro de otro
    for j in range (1,11):
     #aqui i contiene el numero base de la tabla
     #y el j el sig elemento
     salida="{} x {} = {}"
     print(salida.format(i,j,i*j))
    else:
         print()

