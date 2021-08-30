def main():
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))
    operacion1 = (palabras / 475)
    operacion2 = int(operacion1)
    if operacion1 - operacion2 > 0:
        operacion2 = operacion2 + 1
        precio = operacion2 * 60 * 0.90
        print("El costo de la publicación es:", precio)

if __name__ == '__main__':
    main()
