palabra = 'cielo'
letras_verificadas = []
intentos = 6
palabra_correcta = list(palabra)
#Presentamos el juego y como se juega
print('Bienvenido a Wordle Python Edition')
print('Tiene 6 intentos\nAdivine la palabra')
print(f'La palabra a adivinar contiene {len(palabra_correcta)} letras\n')
print(f'Tambien debe utilizar palabras de {len(palabra_correcta)} para jugar\n')
print('[] = Palabra correcta, lugar correcto\nLa () = Palabra correcta, diferente posicion\n')

#Se abre una funcion, en este caso es solo para tener ordenada la presentacion, logica del juego y el mensaje final
def verificador_palabra(palabra_correcta, intentos):
    #Definimos las veces que va a jugar con la variable 'intento', que en este caso estaba definida
    for turno in range(intentos):
        letra = input('Por favor ingrese la palabra\n').lower()
        #Establecemos una condicion que avise al usuario cuantas letras deberia tener la palabra ingresada y se procede a cerrar el juego
        if len(letra) < len(palabra_correcta) or len(letra) > len(palabra_correcta):
            print(f'La palabra debe tener {len(palabra_correcta)} letras\n')
            break
        #Agrega las letras de la palabra ingresada a una lista
        palabras = list(letra)

        if palabras == palabra_correcta:
            print('Felicidades, ganaste el juego')
            print(f'La palabra correcta era {palabra}')
            return 
        #Desglosamos la palabra correcta y comparamos letra por letra la palabra ingresada
        for i in range(len(palabra_correcta)):
            if palabras[i] == palabra_correcta[i]:
                letras_verificadas.append(f"[{palabras[i]}]")
            elif palabras[i] in palabra_correcta:
                letras_verificadas.append(f"({palabras[i]})")
            else:
                letras_verificadas.append(palabras[i])


        intentos_restantes = intentos - turno - 1
        print(letras_verificadas)
        print(f'Le quedan [{intentos_restantes}] intentos\n')

    return 
while True:
    verificador_palabra(palabra_correcta, intentos)
    if input("¿Jugar otra vez? (s/n): ") != 's':
        break

print('Gracias por jugar, vuelva pronto')