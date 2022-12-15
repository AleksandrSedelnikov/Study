trace=`traceroute linux.org | awk 'NR>=2' | awk '{print $3}' | cut -d"(" -f2 | cut -d")" -f1`
echo "IP адреса до linux.org:"
for i in $trace 
do 
if [ "$i" == "*" ] 
then 
continue 
else 
echo $i 
fi 
done
time=`ping -c1 linux.org | grep "time=" | awk '{print $7 $8}' | cut -d"=" -f2`
echo "Время прохождения первого пакета до linux.org: $time"
