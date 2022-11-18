count=`ls -la | egrep -v ^d | awk '{print $2 " " $9}' | sed '1d' | wc -l` # количество файлов
for ((i=1;i<=$count;i++)) # цикл i по количеству файлов
    do
        line=`ls -la | egrep -v ^d | awk '{print $2 " " $9}' | sed '1d' | sed -n $i"p"` # берём строчку
        hard=`echo $line | awk '{print $1}'` # берём количество жёстких ссылок на файл
        if [ $hard  -ne 1 ] # проверяем, если количество жёстких ссылок больше 1
            then
                echo $line | awk '{print $2}' >> result # записываем название файла в файл "result"
        fi
done
echo "Скрипт завершил свою работу."