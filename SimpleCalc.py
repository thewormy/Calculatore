import math
#импорты нужных библиотек

print ("Привет я калькулятор. Меня создал абобус по имени Кирилл. Пользуйся. Я могу умножать,делить,складывать,вычитать. Скоро будут новые функции:)")
print ("Первое число сюда:")
fn = int(input())
print ("Второе число сюда:")
sn = int(input())
print ("Что сделаем с числами?(*-умножить,/-делить,+-сложить,- -вычесть,NOD = нод чисел, NOK = нок чисел.):")
ss = (input())
result = 0
#клиентская часть

def nod_finder(fn, sn):
    if (sn == 0):
        return fn
    if (fn == 0):
        return sn
    else:
        return nod_finder(sn, fn % sn)
#нахождения НОДа 

if ss == "*":
    result = int(fn * sn)
    print ("получилось:")
    print (result)
elif ss == "/":
    result = int(fn / sn)
    print ("получилось:")
    print (result)
elif ss == "+":
    result = int(fn + sn)
    print ("получилось:")
    print (result)
elif ss == "-":
    result = int(fn - sn)
    print ("получилось:")
    print (result)
elif ss == "NOD":
    result = nod_finder(fn,sn)
    print ("получилось:")
    print (result)
elif ss == "NOK":
    result = (math.lcm(fn, sn))
    print ("получилось:")
    print (result)
elif ss == "python love":
    print("i love you too bro....")

#механическая часть
