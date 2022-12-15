time=0 # переменная для подсчёта времени
trace=`traceroute linux.org | awk 'NR>=2' | awk '{print $3}' | cut -d"(" -f2 | cut -d")" -f1` # записываются все IP-адреса и неотвеченные (*) в переменную trace
echo "IP адреса до linux.org:" # вывод IP адресов до linux.org
for i in $trace  # цикл по содержимому переменной trace
do  
if [ "$i" == "*" ] # если i это звезда (неотвеченный канал) 
then 
continue # далее
else # если не звезда то выводится IP
echo $i # вывод IP
fi 
done
#time=`ping -c1 linux.org | grep "time=" | awk '{print $7 $8}' | cut -d"=" -f2` # время прохождения первого пакета до linux.org
# или
time=`traceroute linux.org | awk '{print $4}'`
for i in $time
do
if [ "$i" == "*" ]
then
continue
else
echo $i
time=$(bc<<<"scale=3;$time+$i")
fi
done
echo "Время прохождения первого пакета до linux.org: $time"
