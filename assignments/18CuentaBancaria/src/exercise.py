def main():
    # escribe tu código abajo de esta línea
    anterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    operacion1 = ((anterior + ingresos) - egresos - (13 * cheques))
    operacion2 = (operacion1 * 7.5) / 100
    final = operacion1 - operacion2
    print("El saldo final de la cuenta es:", final)


if __name__ == '__main__':
    main()
