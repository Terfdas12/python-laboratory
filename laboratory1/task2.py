def exercise2() :
    print("Визначення яка з двох точок знаходиться ближче до початку координат")
    x_1 = float(input("Введіть абсцису точки А: "))
    y_1 = float(input("Введіть ординатуі точки А: "))
    XY_1 = (x_1**2 + y_1**2)**(1/2)
    x_2 = float(input("Введіть абсцису точки В: "))
    y_2 = float(input("Введіть ординату точки В: "))
    XY_2 = (x_2 ** 2 + y_2 ** 2)**(1/2)
    if XY_1 > XY_2 :
        print("Точка В лежить ближче до початку координат")
    else:
        print("Точка А лежить ближче до початку координат")