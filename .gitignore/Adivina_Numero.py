# Ulises Thompson python3

import msvcrt
import random


MENSAJE1 = "El rango de numero a adivinar va desde el 1 hasta el?... "
MENSAJE2 = "Ingresa cuántas oportunidades habrá para adivinar el numero... "
MENSAJE3 = "Cuál es el número?... "

def pedirNumero(mensaje):
        """Retorna un numero ingresado por el usuario"""
        ingreso = 0
        numero = False
        while not numero :
            try:
                ingreso = int(input(mensaje))
                numero = True
            except ValueError:
                print("\n Solo numeros por favor:")
            except KeyboardInterrupt:
                print("\n Hasta luego!")
                exit()
            except:
                print("\n Error imprevisto")
                exit()
        return ingreso


def generar_numero(a=0):
    rango = random.randint(1, a)  # Se genera el número al azar a partir del rango especificado
    return rango


def main():
    cont = 0  # Contador para cerrar el ciclo
    m = pedirNumero(MENSAJE1)
    n = generar_numero(m)
    b = pedirNumero(MENSAJE2)
    cont = int(cont)
    while cont != b:
        x = pedirNumero(MENSAJE3)
        if x == n:  # Si el número es correcto, se termina el ciclo
            cont = b
            print("Felicidades es correcto")
        else:  # Si el número ingresado es incorrecto, se acumenta el contador y se disminuyen las oportunidades
            cont += 1
            print("Numero equivocado, Tiene ", b - cont, " oportunidad más")
    print("El número es ", n)  # para terminar se imprime el numero oculto
    print("GAME OVER")


if __name__ == "__main:__":
                main()
main()

msvcrt.getch()  # Mantiene la ventana de ejecución abierta hasta presionar cualquier tecla