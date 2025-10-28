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