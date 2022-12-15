for i in `find ~ -type f 2>~/error`
do
file_name=`echo $i | sed "s/.*\///"`
name=`echo $i | sed "s/.*\///" | wc -c`
name_cur=`expr $name - 1`
if [ $name_cur -eq 4 ]
then
result=`head -4 $file_name | tail -n 1`
echo $result >> F_eq4
fi
done
