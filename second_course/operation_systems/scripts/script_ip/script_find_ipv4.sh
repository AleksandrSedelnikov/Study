namesinterface=`ifconfig | cut -d" " -f1` # переменная содержащая названия сетевых интерфейсов
for i in $namesinterface # цикл по интерфейсам
do
    IP=`ip -4 addr show $i | grep -oP '(?<=inet\s)\d+(\.\d+){3}'` # запись IPv4 для интерфейса [Поясненение про grep: ?<=inet\s(вывести содержание строки содержащей слово inet), d+(число)(\.\d+) - разделитель ., {3} (повторить 3 раза)}]
    #IP=`ip addr show ens33 | grep -v "inet6" | grep "inet" | awk '{print $2}' | cut -d"/" -f1` # усложнённый вариант 
    echo -e "\033[01;33mInterface\033[00;0m: $i\n\033[01;38mIPv4 address\033[00;0m: $IP" # вывод названия интерфейса и его IPv4 адрес
done