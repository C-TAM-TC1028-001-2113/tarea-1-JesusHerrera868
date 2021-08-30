def main():
    # escribe tu código abajo de esta linea
    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    m = (y2 - y1) / (x2 - x1)
    print("Pendiente:", m)

if __name__ == '__main__':
    main()