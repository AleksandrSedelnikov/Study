import socket
import datetime
global connection_count
global message_count

# функция получения/разрыва соединения с клиентской частью
def connection(server):
    global connection_count
    global message_count
    connection_count = 1
    while True:
        conn, addr = server.accept()
        print('= = =\n[Server-Info]: Получено соединение [ID {}][IP {} | PORT {}]\n= = ='.format(connection_count,addr[0], addr[1]))
        start_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        message_count = 0
        result = message_response(conn)
        if (result == 0):
            return 0
        elif (result == 1):
            print('= = =\n[Server-Info]: Разорвано соединение [ID {}][IP {} | PORT {}]'.format(connection_count,addr[0], addr[1]))
            date_format = "%d.%m.%Y %H:%M:%S"
            reset_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            buff_time_start = datetime.datetime.strptime(start_time, date_format)
            buff_time_reset = datetime.datetime.strptime(reset_time, date_format)
            delta = buff_time_reset - buff_time_start
            print('Время соединения: {} дней, {} часов, {} минут, {} секунд.\n= = ='.format(delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds))

        connection_count += 1

# функция обработки и отправки сообщения
def message_response(connect):
    global connection_count
    global message_count
    BUFFER_SIZE = 100
    while True:
        data = connect.recv(BUFFER_SIZE).decode('utf-8')
        if not data:
            return 1
        if (data[:4] == "POST"):
            if (data[5:].lower() == "serv off"):
                return 0
            else:
                message_count += 1
                date_input = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                print('= = =\nПолучено: {}\nВремя получения: {}\n= = ='.format(data, date_input)) 
                msg = input('Начните ввод ответа > ')
                if (len(msg) == 0):
                    print('= = =\n[Server-Error]: Empty data\n= = =')
                    connect.send('К сожалению, сервер не указал ниодного символа в сообщении, повторите запрос...'.encode())
                    continue
                try:
                    connect.send(msg.encode())
                except Exception:
                    print('= = =\n[Server-Info]: Соединение с клиентской частью было разорвано...\n= = =')
                    continue
                date_send = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                print('= = =\nОтправлено: {}\nВремя ответа: {}\n= = ='.format(msg, date_send)) 
        elif (data[:4] == "GET "):
            start = data.find("?")
            end = data.find('HTTP/1.1')
            data = data[start + 1:end - 1]
            if (str(data).lower() == "debug"):
                with open('index.html') as file:
                    html = file.read()
                connect.send(str(html).encode())
                #msg = '\n[Debug-Info]\nНомер соединения: {}\nКоличество сообщений за соединение: {}'.format(connection_count, message_count)
                #connect.send(msg.encode())
                print('= = =\n[Server-Info]: ВНИМАНИЕ! Была отправлена техническая информация\n= = =')
                continue
            elif (str(data).lower() == "datetime"):
                date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                msg = '\n[Time-Info]\nТекущее время сервера: {}'.format(date)
                connect.send(msg.encode())
                continue
            else:
                msg = '[GET-Error]: Введён неверный GET-запрос.'
                connect.send(msg.encode())
                continue

# основная функция серверной части
def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5022
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        print("= = =\n[Server-Info]: Открываем INET сокет...")
        server.bind((TCP_IP, TCP_PORT))
        server.listen(5)
        print("[Server-Info]: Сервер настроен на прослушивание...\n= = =")
        try:
            if (connection(server) == 0):
                server.close()
                print('= = =\n[Server-Info]: Сервер выключен...\n= = =')
                exit(1)
        except KeyboardInterrupt:
            server.close()
            print("= = =\n[Server-Info]: Сервер выключен...\n= = =")
    return 0

if __name__ == "__main__":
    main()