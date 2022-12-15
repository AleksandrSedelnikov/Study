count_str=`cat $1 | wc -l`
if [ $count_str -le 10 ]
then
cymbol=`cat $1 | wc -c`
echo "Количество символов в файле $1 - $cymbol"
else
echo "Количество строк в файле $1 - $count_str"
fi
