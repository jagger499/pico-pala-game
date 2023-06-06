import random

def generar_numero_clave():
    numeros = list(range(10))
    random.shuffle(numeros)
    clave = numeros[:4]
    return clave

def contar_picas(clave, intento):
    picas = 0
    for i in range(4):
        if intento[i] in clave and intento[i] != clave[i]:
            picas += 1
    return picas

def contar_fijas(clave, intento):
    fijas = 0
    for i in range(4):
        if intento[i] == clave[i]:
            fijas += 1
    return fijas

def mostrar_mensaje(intentos):
    if intentos <= 2:
        print("¡Excelente, eres un maestro! Estás fuera del alcance de los demás.")
    elif intentos <= 4:
        print("¡Muy bueno! Puedes ser un gran competidor.")
    elif intentos <= 8:
        print("Bien, estás progresando. Debes buscar tus límites.")
    elif intentos <= 10:
        print("Regular. Aún es largo el camino por recorrer.")
    else:
        print("Mal, este juego no es para ti.")

def jugar():

    clave = generar_numero_clave()
    intentos = 0

    while intentos < 12:
        
        intento = input("Ingresa un número de 4 cifras: ")
        if len(intento) != 4 or not intento.isdigit():
            print("Ingresa un número válido de 4 cifras.")
            continue
        
        intentos += 1
        intento = list(map(int, intento))
        
        picas = contar_picas(clave, intento)
        fijas = contar_fijas(clave, intento)

        print(f"Picas: {picas}")
        print(f"Fijas: {fijas}")

        if fijas == 4:
            mostrar_mensaje(intentos)
            return
    
    print("Lo siento, no has logrado adivinar el número en 12 intentos.")
    mostrar_mensaje(intentos)

# Inicio del juego
jugar()
