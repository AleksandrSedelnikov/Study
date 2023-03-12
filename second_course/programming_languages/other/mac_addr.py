import subprocess

def mac_addr(interface):
    mac_addres = subprocess.check_output("ifconfig {} | grep 'HWaddr' |  cut -d' ' -f10".format(interface),stderr=subprocess.STDOUT,shell=True, universal_newlines=True)
    return mac_addres
    

def main():
    interface = input('Введите название интерфейса: ')
    result = mac_addr(interface)
    if (result.find('Устройство не обнаружено') != -1):
        print('Интерфейс {} не найден.'.format(interface))
    elif (result == ""):
        print('MAC-addres для интерфейса {} не найден.'.format(interface))
    else:
        print('MAC-addres для интерфейса {} : {}'.format(interface,result))

if __name__ == "__main__":
    main()