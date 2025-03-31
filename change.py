def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(f"{money}\n")
    print ("Vuelto\n")
    print ("Pesos:")
    vuelto = money-expense
    pesos=int(vuelto)
    cents=vuelto - pesos
    cents=int(cents*100)
    print (pesos)
    print("Centavos:")
    print(cents)
