vyr = int(input('Выручка фирмы:'))
vyruchka = print(vyr)
izd = int(input('Издержки фирмы:'))
izderzhki = print(izd)

if vyr > izd:
    print('Прибыль')
    rent = (vyr - izd) / vyr
    staff = int(input('Количество сотрудиков:'))
    print(staff)
    prib_na_sotr = (vyr - izd) / staff
    print('Прибыль на одного сотрудника:')
    print(prib_na_sotr)
else:
    print('Убыток')