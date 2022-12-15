for i in `find . -maxdepth 1 -type f 2>~/error`
do
cat $i | head -n 1 | tail -n 1 >> $1
cat $i | tail -n 1 >> $1
done
echo "Выполнено."
