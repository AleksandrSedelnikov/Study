import socket
check = []
flag = 0

f = open('service.db', 'a')
while (flag == 0):
    try:
        port = input('Введите номер порта (для выхода из ввода введите !): ')
        if (port == "!"):
            flag = 1
            print("Инициирован выход из скрипта.")
            f.write('Конец файла.')
            pass
        else:
            port = int(port)
            result = 'Номер порта: {} | Порт: {}.'.format(port, socket.getservbyport(port))
            if port not in check:
                f.write('{}\n'.format(result))
                check.append(port)
                print(result)
            else:
                print('Данный порт уже был успешно внесён ранее.')
    except Exception as e:
        if (str(e) == "port/proto not found"):
            print("Ошибка: порт не найден.")
        else:
            print('Error: {}'.format(e))
        continue
