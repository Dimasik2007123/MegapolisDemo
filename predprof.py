##Задача 1
'''
Все ребята сдали свои проекты и получили оценки на защите, но Хадаров Владимир все прослушал 
и просит помочь ему узнать какую оценку за проект он получил. Пожалуйста, подскажите 
Владимиру какую оценку он получил. Формат вывода: Ты получил: <ОЦЕНКА>, за проект - <id>
Пока помогали Владимиру увидели, что многие ученики потеряли свои оценки при выкачке с 
сайта. Из-за этого нет возможности посмотреть общую статистику. Чтобы избежать путаницы 
поставьте вместо ошибки среднее значение по классу и округлите до трех знаков после запятой. 
Сохраните данные в новую таблицу с названием student_new.csv
##'''
fin = open('students.csv','r',encoding='utf-8')
title = fin.readline()
print(title)
students = [x.strip().split(',') for x in fin]
fin.close()
bal_sum = {} #bal_sum{key - номер класса,value - сумма оценок}
bal_cnt = {} #bal_cnt{key - номер класса,value - количество оценок}
for x in students:
    x[0]- порядковый №
    x[1]- ФИО
    x[2]- № проекта
    x[3]- класс
    x[4]- оценка за проект
    if x[4]!='None':
        if x[3] in bal_sum:
            bal_sum[x[3]] += int(x[4])
            bal_cnt[x[3]] += 1
        else:
            bal_sum[x[3]] = int(x[4])
            bal_cnt[x[3]] = 1         
    fio = x[1].split()
    if fio[0]=='Хадаров' and fio[1]=='Владимир':
        print(f'Ты получил: {x[4]}, за проект - {x[2]}')
for x in students:
    if x[4]=='None':
        x[4]=f'{bal_sum[x[3]]/bal_cnt[x[3]]:.3f}'
fout = open('student_new.csv','w',encoding='utf-8')
fout.write(title)
for x in students:
    s = ','.join(x)+'\n'
    print(s)
    fout.write(s)
fout.close()
'''
Задача 2
Данные из таблицы student.csv необходимо отсортировать по столбцу оценки(score) с помощь 
сортировки вставками (В задаче нельзя использовать встроенные функции сортировок!). Из 
полученного списка выделите первых 3х победителей из 10 класса. Данные о победителях 
необходимо вывести в формате:
<X> класс:
1 место: <И. Фамилия>
2 место: <И. Фамилия>
3 место: <И. Фамилия>
'''
fin = open('students.csv','r',encoding='utf-8')
title = fin.readline()
print(title)
students = [x.strip().split(',') for x in fin]
fin.close()
for i in range(1,len(students)):
    for j in range(i,0,-1):
        if students[j][4]<students[j-1][4]:
            students[j],students[j-1] = students[j-1],students[j]
        else:
            break
cnt = 0
for x in students:
    if '10' in x[3] and x[4]=='5':
        cnt+=1
        fio = x[1].split()
        print(f'{cnt} место: {fio[1][0]}. {fio[0]}')
        if cnt==3:
            break
'''
Задача 3
Ввод: стандартный ввод
Вывод: стандартный вывод
Напишите небольшую программу, которая на вход будет получать id проекта (гарантируется, что 
вводимые числа всегда целые), а на выходе будет предоставлять информацию о ученике, который 
делал этот проект и его оценку за этот проект в формате: Проект № <N> делал: <И. Фамилия> 
он(а) получил(а) оценку - <ОЦЕНКА>. Если по заданному запросу ничего не найдено вывести: 
Ничего не найдено.
Поиск ученика необходимо осуществить с помощью линейного поиска в файле students.csv.
Ваша программа должна всегда работать и отключиться только в случае, когда пользователь 
введет СТОП
'''
fin = open('students.csv','r',encoding='utf-8')
title = fin.readline()
print(title)
students = [x.strip().split(',') for x in fin]
fin.close()
while True:
    N = input('Введите № проекта (или СТОП):')
    if N.upper()=='СТОП':
        break
    for x in students:
        if x[2]==N:
            fio = x[1].split()
            print(f'Проект № {x[2]} делал: {fio[1][0]}. {fio[0]} он(а) получил(а) оценку - {x[4]}.')
            break
    else:
        print('Ничего не найдено')
'''
Задача 4
Вам необходимо создать личные кабинеты для каждого пользователя, чтобы каждый из них видел 
свои достижения и мог лично взаимодействовать с вами. Для этого необходимо создать логины и 
пароли для каждого из школьников. Реализуйте методы/функции, которые будут генерировать 
логины и пароли для пользователей. Логин должен состоять из фамилии и инициалов, например, 
если школьника зовут Соколов Иван Иванович, его логин должен выглядеть как Соколов_ИИ. 
Также для каждого пользователя необходимо сгенерировать пароль, пароль должен состоять из 8 
символов, включать в себя заглавные, строчные буквы английского алфавита и цифры. 
“0,Сербин Геннадий Михаилович,7,8в,2” → “0,Сербин Геннадий 
Михаилович,7,8в,2,Сербин_ГМ,fhGi45Bq”
'''
from random import choice
fin = open('students.csv','r',encoding='utf-8')
title = fin.readline().strip()
print(title)
students = [x.strip() for x in fin]
fin.close()
symbol='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
cifri='0123456789'
big='QWERTYUIOPASDFGHJKLZXCVBNM'
small='qwertyuiopasdfghjklzxcvbnm'
for i in range(len(students)):
    da=0
    ci=0
    bi=0
    sm=0
    s = students[i].split(',')
    fio = s[1].split()
    login = fio[0]+'_'+fio[1][0]+fio[2][0]
    password = ''
    while da!=True:
        for _ in range(8):
            password+=choice(symbol)
            if password[-1] in cifri: ci=1
            if password[-1] in big: bi=1
            if password[-1] in small: sm=1
            if ci+bi+mi==3: da=1
    students[i] = students[i]+','+login+','+password
fout = open('students_password.csv','w',encoding='utf-8')
fout.write(title+',login,password\n')
for x in students:
    s =x+'\n'
    fout.write(s)
fout.close()

    
