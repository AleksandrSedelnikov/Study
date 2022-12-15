if [ $# -eq 0 ] || [ $# -eq 1 ] || [ $# -gt 10 ]
then
echo -e "Нарушен синтаксис.\nРазрешено вводить не более 10-ти параметров и не меньше 2-х.\nВведено: $#"
else
count=`echo $#`
for ((i=1;i<=$count;i++))
do
if [ $i -eq 1 ]
then
file=`echo $1`
else
echo -e "Параметр $1 добавлен в файл с именем $file."
echo $1 >> $file
fi
shift
done
fi
 
