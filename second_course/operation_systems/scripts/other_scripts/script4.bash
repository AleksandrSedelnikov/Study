count=0
for i in `find ~ -type f 2>~/error`
do
raz=`grep -o "$1" $i | wc -l`
if [ $raz -ne 0 ]
then
echo $i
fi
count=`expr $count + $raz`
done
echo $count
