#noveno ejercisio
cantidad=input("ingrese la cantidad a invertir\n")
interes_anual=input("ingrese el porcentaje de interes anual\n")
cantidad_De_años=input("cantidad de años")
inversion=int(cantidad)
interes_decimal=float(interes_anual)
cantidad_años_entero=int(cantidad_De_años)
operacion=inversion*cantidad_años_entero*interes_decimal
print("la capital obtenida es :\n", operacion)
#ejercisio 10
cant_payasos=input("ingrese el numero de payasos vendidos\n")
cant_muñecas=input("ingrese el numero de muñecas\n")
cant_payasos_enteros= int(cant_payasos)
cant_muñecas_enteros= int(cant_muñecas)
payasos_total=cant_payasos_enteros*112
muñecas_total=cant_muñecas_enteros*75
peso_total=payasos_total+muñecas_total
print("el peso total del envio es\n",peso_total)