count=0 # счётчик количества раз встречи слова заданного первым параметром при запуске скрипта (bash название_скрипта параметр)
for i in `find . -type f 2>~/error` # цикл по всем файлам текущей директории и поддиректориях
do
raz=`grep -o "$1" $i | wc -l` # количество раз встречи слова $1(параметр) в файле
count=`expr $count + $raz` # прибавление количества раз к общему счётчику
done
echo "Слово $1 встречается в файлах текущей директории и поддиректориях: $count раз." # вывод количества раз