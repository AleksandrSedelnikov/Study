students = []
stud_name_buff = []
check_one = 0

var = input("Вы в интерактивном меню, доступные команды:\n1)Внести студента и его контрольный срок\nНачните ввода: ")
if (var == "1"):
    stud_name_buff = input("Введите имена студентов, которых Вы хотите добавить[через пробел]: ").split()
    if (len(stud_name_buff) == 0):
        print("Ни одно Имя не введено.")
    else:
        for i in stud_name_buff:
            for j in i:
                if (j in """1234567890.,;'!?"""):
                    check_one = 1
        if (check_one != 1):
            for i in range(len(stud_name_buff)):
                ks = input(f'Введите контрольный срок для {stud_name_buff[i]}: ')
                if (ks not in """1234567890"""):
                    print("Введён неверный контрольный срок, стандартное значение null применено.")
                    students.append([stud_name_buff[i],"null"])
                else:
                    students.append([stud_name_buff[i],ks])
            print("Список студентов:")
            for i in range(len(students)):
                print(f'Имя студента: {students[i][0]}[ID {i}], его контрольный срок: {students[i][1]}')
        else:
            print("В введённых Именах студентов найдены запрещённые символы, продолжение ввода контрольного срока невозможно.")