flag1 = 1
students = []
f = open('baza.txt', 'w')

while (flag1 == 1):
    try:
        student_buff = input('Student: ')
        ks_buff = input('KS: ')
        students.append([student_buff, ks_buff])
        f.write('Студент: {} | Контрольный срок: {}\n'.format(student_buff, ks_buff))
        response = input("Хотите продолжить ввод? да/нет: ")
        if (response == "да"):
            flag1 = 1
        else:
            flag1 = 0
            f.close()
    except Exception as e:
        print('Ошибка: {}'.format(e))
        f.close()