#Известно, что X кг конфет стоит A. Определить, сколько стоит 1 кг и Y кг этих же конфет.
try:
    x = int(input("введите количество конфет (в кг): "))
    a = int(input("введите стоимость конфет (в руб): "))
    p = (a/x)
    print ("стоимость 1 кг:", p)
    y = int(input("введите количество конфет(в кг): " ))
    r = (y*p)
    print ("стоимость", y, 'кг:', r)
except ValueError:
    print("ошибка")