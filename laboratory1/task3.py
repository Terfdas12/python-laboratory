def exercise3():
    print("Обчислення функції в залежності від значення введеної змінної")
    x = float(input("Введіть число замість x : "))
    if x >= 3 :
       result = str((-x)**2+3*x+9)
       print("Результатом обчислення є число " + result)
    else :
       result = str(1/(x**3-6))
       print("Результатом обчислення є число " + result)