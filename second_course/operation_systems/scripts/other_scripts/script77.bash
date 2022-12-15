echo "" > DB_gt16
echo "" > DB_16F
for i in `find ~/logs -size +16k 2>~/error`
do
echo $i
echo $i >> DB_gt16
name_file=`echo $i | sed "s/.*\///"`
result=`head -3 $i | tail -n 1`
if [ "$result" != "" ]
then
echo "$i:$result" >> DB_16F
fi
done
 
