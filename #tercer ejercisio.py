#tercer ejercisio
a=3+2
b=2*5
c=a/b
d=c**2
print(d)
#cuarto ejercisio
variable1=input("ingrese el numero de horas trabajadas\n")
variable2=int (variable1)
variable3= input("ahora ingrese cuanto le pagan la hora\n")
variable4=int (variable3)
rta=variable2*variable4
print("tu pago es de\n",rta)
#sexto ejercisio
n=input("escriba un numero entero\n")
conversion= int(n)
suma= conversion*(conversion+1) / 2
print(suma)
#septimo ejercisio
peso_kg=input("escribe tu peso en kilogramos\n")
peso_decimal=float(peso_kg)
peso_entero=int(peso_decimal)
altura_cm=input("escribe tu altura en centimetros\n")
altura_decimal=float(altura_cm)
altura_entero=int(altura_entero)
calculo_imc=peso_decimal/(altura_decimal**2)
decimal=float(calculo_imc)
print("su indice de masa corporal es\n",decimal)
#noveno ejercisio
cantidad=input("ingrese la cantidad a invertir\n")
interes_anual=input("ingrese el porcentaje de interes anual\n")
cantidad_De_años=input("cantidad de años")
inversion=int(cantidad)
interes_decimal=float(interes_anual)
cantidad_años_entero=int(cantidad_De_años)
operacion=inversion*cantidad_años_entero*interes_decimal
print=(operacion)
