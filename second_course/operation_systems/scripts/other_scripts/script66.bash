for i in `find ~ -type f 2>~/error`
do
result=`grep -o "3" $i 2>~/error`
if [ "$result" != "" ]
then
names+="$i "
fi
done
tar -zcvf archive66.tar.gz $names

