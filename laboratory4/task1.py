def ex1():
    x_A1=int(input("Введіть абсцису точки А для першого трикутника: "))
    y_A1=int(input("Введіть оординату точки А для першого трикутника: "))
    x_B1=int(input("Введіть абсцису точки B для першого трикутника: "))
    y_B1=int(input("Введіть оординату точки B для першого трикутника: "))
    x_C1=int(input("Введіть абсцису точки C для першого трикутника: "))
    y_C1=int(input("Введіть оординату точки C для першого трикутника: "))
    x_A2=float(input("Введіть абсцису точки А для другого трикутника: "))
    y_A2=float(input("Введіть оординату точки А для другого трикутника: "))
    x_B2=float(input("Введіть абсцису точки B для другого трикутника: "))
    y_B2=float(input("Введіть оординату точки B для другого трикутника: "))
    x_C2=float(input("Введіть абсцису точки C для другого трикутника: "))
    y_C2=float(input("Введіть оординату точки C для другого трикутника: "))
    A_1=(((x_A1 - x_B1)**2)+((y_A1 - y_B1)**2))**(1/2)
    B_1=(((x_C1 - x_B1)**2)+((y_C1 - y_B1)**2))**(1/2)
    C_1=(((x_C1 - x_A1)**2)+((y_C1 - y_A1)**2))**(1/2)
    A_2=(((x_A2 - x_B2)**2)+((y_A2 - y_B2)**2))**(1/2)
    B_2=(((x_C2 - x_B2)**2)+((y_C2 - y_B2)**2))**(1/2)
    C_2=(((x_C2 - x_A2)**2)+((y_C2 - y_A2)**2))**(1/2)
    def mnojena(A,B,C):
        p=(A+B+C)/2
        S=(p*(p-A)*(p-B)*(p-C))**(1/2)
        return S
    while x_A1==x_B1 and x_B1==x_C1 or y_A1==y_B1 and y_B1==y_C1  :
        print("Перший трикутник не є трикутником бо 3 вершини лежать на одній прямій")
        x_A1 = int(input("Введіть абсцису точки А для першого трикутника: "))
        y_A1 = int(input("Введіть оординату точки А для першого трикутника: "))
        x_B1 = int(input("Введіть абсцису точки B для першого трикутника: "))
        y_B1 = int(input("Введіть оординату точки B для першого трикутника: "))
        x_C1 = int(input("Введіть абсцису точки C для першого трикутника: "))
        y_C1 = int(input("Введіть оординату точки C для першого трикутника: "))
    while x_A2==x_B2 and x_B2==x_C2 or y_A2==y_B2 and y_B2==y_C2  :
        print("Другий трикутник не є трикутником бо 3 вершини лежать на одній прямій")
        x_A2 = float(input("Введіть абсцису точки А для другого трикутника: "))
        y_A2 = float(input("Введіть оординату точки А для другого трикутника: "))
        x_B2 = float(input("Введіть абсцису точки B для другого трикутника: "))
        y_B2 = float(input("Введіть оординату точки B для другого трикутника: "))
        x_C2 = float(input("Введіть абсцису точки C для другого трикутника: "))
        y_C2 = float(input("Введіть оординату точки C для другого трикутника: "))
    if mnojena(A_1,B_1,C_1)>mnojena(A_2,B_2,C_2):
        print("Площа першого трикутника більша ніж площа другого трикутника")
    elif mnojena(A_1,B_1,C_1)==mnojena(A_2,B_2,C_2):
        print("Площі трикутників рівні")
    elif mnojena(A_1,B_1,C_1)<mnojena(A_2,B_2,C_2):
        print("Площа першого трикутника меньша ніж площа другого трикутника")