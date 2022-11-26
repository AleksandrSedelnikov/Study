namesinterface=`ifconfig | cut -d" " -f1` # переменная содержащая названия сетевых интерфейсов
for i in $namesinterface # цикл по интерфейсам
do
    IP=`ip -4 addr show $i | grep -oP '(?<=inet\s)\d+(\.\d+){3}'` # запись IPv4 для интерфейса
    echo -e "\033[01;33mInterface\033[00;0m: $i\n\033[01;38mIPv4 address\033[00;0m: $IP" # вывод названия интерфейса и его IPv4 адрес
done