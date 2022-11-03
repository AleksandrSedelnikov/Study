
o=`find ~ -name "dir" -type d 2>~/error`
k=`find ~ -name "dir" -type d 2>~/error | wc -l`
array=(`find ~ -name "dir" -type d 2>~/error`)
if [ $k = 1 ]
    then
        h=`find $o -type d 2>~/error | wc -l`
        h1=`expr $h - 1`
        if [ $h1 != 0 ]
            then
                l=`echo $o | grep -o "/" | wc -l`
                d=`expr $l + 2`
                k=`ls -d $o/*/ | cut -f"$d" -d'/'`
                echo -e "\033[32mВложенные директории:\033[0m"
                echo -e "\033[34m$k\033[0m"
            else
                echo "\033[31mВ каталоге отсутствуют вложенные директории\033[0m"
        fi
    elif [ "$k" -gt "1" ]
        then
            echo "Данных каталогов $k, укажите точный путь до нужного Вам каталога:"
            echo $o 
            echo -n "Введите нужный путь: "; read o
            for((i=0;i<$k;i++))
            do
                if [ "${array[i]}" == "$o" ]
                    then
                    j=${array[i]}
                fi
            done
            if [ "$j" != "" ]
                then
                    h=`find $j -type d 2>~/error | wc -l`
                    h1=`expr $h - 1`
                    if [ $h1 != 0 ]
                        then
                        l=`echo $j | grep -o "/" | wc -l`
                        d=`expr $l + 2`
                        k=`ls -d $j/*/ | cut -f"$d" -d'/'`
                        echo -e "\033[32mВложенные директории:\033[0m"
                        echo -e "\033[34m$k\033[0m" 
                    else
                        echo -e "\033[31mВ каталоге отсутствуют вложенные директории\033[0m"
                    fi
                else
                echo "Был введён неверный путь до каталога."
            fi
    else
        echo -e "\033[41mДанного каталога не существует.\033[0m"
fi
