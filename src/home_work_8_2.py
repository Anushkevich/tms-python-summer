"""
 Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)[03-10.32]
"""
s_1 = str(input('Введите трислова : '))
s_1 = s_1.split()
s_2 = s_1[-1::-1]
calc=0
for i in range(3):
    if s_2[i] == s_1[i]:
        calc +=1
    elif calc>0:
     print('да')
    elif calc<0:
     print( 'нет')


