#ejercisio 1
print("hola mundo ")
# ejercisio instrucciones hasta el sena
print("Primero sali de mi casa a las 5 y 45 am \n")
print("Despues camine hacia la av cali aproximadamente 8 cuadras \n")
print("Y espere el bus a 410 en el paradero \n")
print("Despues de cinco minutos cogi el bus que estaba lleno\n")
print("Espere 45 minutos hasta llegar a la parada frente a la camara de conercio de bogota \n")
print("Me baje del bus y camine 6 cuadras hasta llegar enfrente de la estacion de transmilenio las flores \n")
print("Cruce hacia el lado de la fundacion universitaria horizonte y camine hasta la puerta \n")
print("Fin")
#Ejercisio3
nombre=input("¿cual es tu nombre?\n")
print("Hola", nombre)
#ejercisio 4
print("¿Como llegar a mi casa?")
print("Primero salimos de la fundacion universitaria horizonte\n")
print("Camino derecho por donde sali 4 cuadras y volteo a mano izquierda para la parada que esta enfrente de capillas de la fé \n")
print("Espero el bus f 410 y cuando llega me subo \n ")
print("Espero hasta llegar a la avenida cali y me bajo en los mataderos \n")
print("Cruzo la avenida por el semaforo y camino derecho 6 cuadras y volteo a mano derecha\n")
print("Camino derecho otra cuadra y volteo en la esquina a mano izquierda\n")
print("camino derecho y diagonal al salon comunal andalucia segundo sector esta mi casa\n")
#ejercisio pan
plata_pal_pan=5000
costo_pan=500
panes_que_comio=plata_pal_pan/costo_pan
print("comiste",panes_que_comio,"panes")
#ejercisio cine (datos fijos)
print("Para ir al cine debes tener en cuenta")
tiempo_ir_cine=30
tiempo_pelicula=120
costo_entrada=12
costo_de_comida=25
tiempo_total=tiempo_ir_cine+tiempo_pelicula
costo_total=costo_entrada+costo_de_comida
print("Te gastas",tiempo_total,"minutos")
print("Te gastas",costo_total,"mil")
#ejerciso cine (pedir datos)
print("Quieres saber cuanto te gastas en el cine?")
Presupuesto=input("¿cuanto dinero tienes disponible?\n")
presup_entero=int(Presupuesto)
DURACION_PELI=input("porfavor ingresa duanto dura la pelicula en minutos \n")
ENT_PELI=int(DURACION_PELI)
Tiempo_ir_cine=input("¿Sabes cuanto tiempo te toma llegar al cine? Digitalo \n")
ENT_CAMINO=int(Tiempo_ir_cine)
tiempo_total=ENT_CAMINO+ENT_PELI
comida=input("quieren comer algo? cuanto vale lo que quieren comer ?\n")
comida_ent=int(comida)
entrada=input("cuanto valen las entradas?\n")
entrada_ent=int(entrada)
costo_total=comida_ent+entrada_ent
if costo_total>presup_entero:
    print("no tienes el dinero suficiente para salir al cine, ahorre papi")
else:
    print("puedes salir, Felicitaciones")
semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
#ejercisio def
def puedes_salir(dia):
    if dia=="sabado":
        print("puedes salir")
for dia in semana:
    if dia=="sabado"or dia =="domingo":
        print("puedes salir el dia \n",dia)
    #print("el dia de la semana es", dia):
    dia=="sabado"or dia =="domingo" if print("puedes salir el dia ") else print("no puedes salir")
    # ejercisio while 
    numero=0
while numero <5:
    print(f"el numero es: {numero}")
    numero+=1

