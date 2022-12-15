i=0
count=0
echo "Введено параметров: $#"
while [ -n "$1" ]
do
if [ -d $1 ]
then
files=`find $1 -maxdepth 1 -type f 2>~/error`
for i in $files
do
echo $i
stroki=`cat $i | wc -l`
count=`expr $count + $stroki`
done
else
stroki=`cat $1 | wc -l`
count=`expr $count + $stroki`
fi
shift
done
echo "Количество строчек в файлах: $count"
