i=1
while [ $i -lt 255 ]
do
if [ `ping -c 1 192.168.55.$i  | grep "received" | awk '{print $4}'` -eq 1 ]
then
echo 192.168.55.$i is available
echo 192.168.55.$i >> ~/testing_page/DP_IP
else
echo 192.168.55.$i is not available
fi
i=`expr $i + 1`
done

