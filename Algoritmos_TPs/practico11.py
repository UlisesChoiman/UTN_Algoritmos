#1

import random
import sys


def generar_lista(n=10, minimo=0, maximo=99):
    return [random.randint(minimo, maximo) for _ in range(n)]

def main():
    lista = generar_lista()
    print("Lista generada:", lista)

    try:
        entrada = input("Ingrese un número entero para buscar: ").strip()
        numero = int(entrada)
    except ValueError:
        print("Entrada no válida. Debe ingresar un número entero.")
        sys.exit(1)

    posiciones = [i + 1 for i, v in enumerate(lista) if v == numero]  # posiciones 1-based
    if posiciones:
        print(f"El número {numero} se encuentra en la lista en la(s) posición(es): {', '.join(map(str, posiciones))}")
    else:
        print(f"El número {numero} NO se encuentra en la lista.")

if __name__ == "__main__":
    main()


#2

def buscar_alumno(lista_alumnos, alumno_buscado):
    return alumno_buscado in lista_alumnos

def main_alumnos():
    alumnos = ["Juan", "Maria", "Pedro", "Ana", "Luis"]
    print("Lista de alumnos que rindieron:", alumnos)

    try:
        nombre = input("Ingrese el nombre del alumno a buscar: ").strip().capitalize()
        if buscar_alumno(alumnos, nombre):
            print(f"{nombre} sí se presentó a rendir el examen.")
        else:
            print(f"{nombre} NO se presentó a rendir el examen.")
    except KeyboardInterrupt:
        print("\nBúsqueda cancelada.")
        sys.exit(1)

if __name__ == "__main__":
    main_alumnos()


#3

def buscar_ocurrencias(lista, valor):
    posiciones = [i + 1 for i, v in enumerate(lista) if v == valor]
    return posiciones if posiciones else [1]

def main():
    lista = generar_lista()
    print("Lista generada:", lista)

    try:
        entrada = input("Ingrese un número entero para buscar: ").strip()
        numero = int(entrada)
    except ValueError:
        print("Entrada no válida. Debe ingresar un número entero.")
        sys.exit(1)

    posiciones = buscar_ocurrencias(lista, numero)
    if posiciones == [1]:
        print(f"El número {numero} NO se encuentra en la lista.")
    else:
        print(f"El número {numero} se encuentra en la lista en la(s) posición(es): {', '.join(map(str, posiciones))}")

def main_alumnos():
    alumnos = ["Juan", "Maria", "Pedro", "Ana", "Luis"]
    print("Lista de alumnos que rindieron:", alumnos)

    try:
        nombre = input("Ingrese el nombre del alumno a buscar: ").strip().capitalize()
        posiciones = buscar_ocurrencias(alumnos, nombre)
        if posiciones == [1]:
            print(f"{nombre} NO se presentó a rendir el examen.")
        else:
            print(f"{nombre} sí se presentó a rendir el examen.")
    except KeyboardInterrupt:
        print("\nBúsqueda cancelada.")
        sys.exit(1)

    
    #4

    def jugar_adivinar_numero():

        # Pedir intervalo válido a < b
        while True:
            try:
                entrada = input("Ingrese dos enteros a y b separados por espacio (a < b) o 'salir' para terminar: ").strip()
                if entrada.lower() == "salir":
                    print("Salida solicitada.")
                    return
                partes = entrada.split()
                if len(partes) != 2:
                    print("Debe ingresar exactamente dos valores.")
                    continue
                a = int(partes[0])
                b = int(partes[1])
                if a >= b:
                    print("Debe cumplirse a < b.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Ingrese dos enteros.")
            except KeyboardInterrupt:
                print("\nInterrumpido por el usuario.")
                return

        # Jugar
        listo = input(f"Piense un número en el intervalo [{a}, {b}] y presione Enter cuando esté listo (o escriba 'salir'): ").strip()
        if listo.lower() == "salir":
            print("Salida solicitada.")
            return

        bajo, alto = a, b
        while bajo <= alto:
            intento = (bajo + alto) // 2
            try:
                resp = input(f"¿Su número es {intento}? Responda 'mayor', 'menor', 'igual' o 'salir': ").strip().lower()
            except KeyboardInterrupt:
                print("\nInterrumpido por el usuario.")
                return

            if resp == "salir":
                print("Salida solicitada.")
                return
            if resp not in {"mayor", "menor", "igual"}:
                print("Respuesta inválida. Use exactamente 'mayor', 'menor', 'igual' o 'salir'.")
                continue

            if resp == "igual":
                print(f"¡La computadora adivinó su número: {intento}!")
                return
            elif resp == "mayor":
                bajo = intento + 1
            else:  # "menor"
                alto = intento - 1

            if bajo > alto:
                print("Las respuestas dadas son contradictorias: no hay números posibles en el intervalo. Fin del juego.")
                return