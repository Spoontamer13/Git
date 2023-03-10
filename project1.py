a = float(input("Введите первое число: "))
c=a
g=0
r = int(input("Введите количество опираций"))
t=0
for g in range(r):
    b = int(input("Выберете опирацию:1-сложение,2-вычитание,3-умножение,4-деление,5- возведение в степень: "))
    d = float(input("Введите второе число: "))
    match b:
        case 1: 
            c=c+d 
            print (c)
            g+=1
        case 2:
            c=c-d
            print(c) 
            g+=1
        case 3:
            c=c*d
            print(c)
            g+=1
        case 4:
            if d != 0:
                c=c/d
                print(c)
                g+=1
            else:
                print("Невозможно")
        case 5:
            c=c**d
            print(c)
            g+=1
   

