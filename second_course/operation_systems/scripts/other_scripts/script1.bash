times=0.0
time=`traceroute linux.org | awk 'NR>=2' | awk '{print $4}'`
for i in $time
do
if [ "$i" == "*" ]
then
continue
else
times=$(bc<<<"scale=3;$times+$i")
echo "Значение i: $i, значение times: $times"
fi
done
echo "Время прохождения первого пакета до linux.org: $times"

