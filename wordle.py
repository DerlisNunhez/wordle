palabra = 'cielo'
letras_verificadas = []
intentos = 6
palabra_correcta = list(palabra)

print('Bienvenido a Wordle Python Edition')
print('Tiene 6 intentos\nAdivine la palabra')
print(f'La palabra a adivinar contiene {len(palabra_correcta)} letras\n')


def verificador_palabra(palabra_correcta, intentos):
    for turno in range(intentos):
        letra = input('Por favor ingrese la palabra\n').lower()
        if len(letra) < len(palabra_correcta) or len(letra) > len(palabra_correcta):
            print(f'La palabra debe tener {len(palabra_correcta)} letras\n')
            break
        palabras = list(letra)

        if palabras == palabra_correcta:
            print('Felicidades, ganaste el juego')
            return 

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

verificador_palabra(palabra_correcta, intentos)

print(f'La palabra correcta era {palabra}')
print('Gracias por jugar, vuelva pronto')