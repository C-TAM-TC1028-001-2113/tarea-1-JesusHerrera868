def main():
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))
    operacion1 = (palabras / 475)
    if operacion1 > 1:
        operacion2 = (60 * 2)
        operacion3 = (operacion2 * 10) / 100
        final = (operacion2 - operacion3)
        print("El costo de la publicación es:", final)
    else:
        operacion4 = (60 * 1)
        operacion5 = (operacion4 * 10) / 100
        final2 = (operacion4 - operacion5)
        print("El costo de la publicación es:", final2)


if __name__ == '__main__':
    main()
