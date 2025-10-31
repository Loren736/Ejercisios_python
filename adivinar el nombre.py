numero_secreto = 65
print("Bienvenido a el juego de adivina el numero :)")
print("he pensado en un numero del 1 al 100 ¿quieres adivinarlo?") 
string_usuario=input("hey.ingresa un numero que estas pensando:")
intento=int(string_usuario)
if intento==numero_secreto :
    print("lo encontraste" )
else :
    print("sigue intentando ")