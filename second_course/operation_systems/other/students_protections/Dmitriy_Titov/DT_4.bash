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
times=0.0 # переменная для подсчёта времени
time=`traceroute linux.org | awk 'NR>=2' | awk '{print $4}'` # столбец времени прохождения пакета по ip до linux.org
for i in $time # цикл по значениям в переменной time
do
if [ "$i" == "*" ] # убрать звёздочки
then
continue # если это звезда пропускаем
else
times=$(bc<<<"scale=3;$times+$i") # если не звезда, то делаем сложение
fi
done
echo "Время прохождения первого пакета до linux.org: $times ms" # вывод времени прохождения
