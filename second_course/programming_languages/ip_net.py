# функция принимающая входные данные и отправляющая в функцию обработки и по итогу возвращает ответ
def input_values():
    ip = input('Введите IP-адрес: ').split(".")
    mask = input('Введите маску: ').split(".")
    result_ip_net = ip_net(ip, mask)
    return result_ip_net

# функция обрабатывающая входные данные и находит начальный ip-адрес сети
def ip_net(ip, mask):
    if (len(ip) == len(mask) and len(ip) == 4):
        current_ip = ""
        for i in range(len(ip)):
            new_oct = str(int(ip[i]) & int(mask[i]))
            if (i != len(ip) - 1):
                current_ip += "{}.".format(new_oct)
            else:
                current_ip += "{}".format(new_oct)
        return current_ip
    else:
        return 1

# основная функция кода
def main():
    result = input_values()
    if (result != 1):
        print('IP-адрес сети: {}'.format(result))
    else:
        print('Неверный входные данные.')


if __name__ == "__main__":
    main()
