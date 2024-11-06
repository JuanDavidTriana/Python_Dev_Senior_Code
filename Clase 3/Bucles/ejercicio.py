import random 

numero_secreto = random.randint(1, 10)

vidas = 3

while vidas > 0:
    intento = int(input("Adivina el numero:"))
    if intento == numero_secreto:
        print("Felicidades, adivinaste el numero")
        break
    elif intento < numero_secreto:
        print("El numero es mayor")
        vidas -= 1
    else:
        print("El numero es menor")
        vidas -= 1
        
if vidas == 0:
    print("Perdiste, el numero era", numero_secreto)
    