
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
            par=0
            while [ $par == 0 ]
                do
                    echo -n "Введите нужный путь или код отмены 01: "; read o
                    if [ "$o" != "01" ]
                    then
                        for((i=0;i<$k;i++))
                        do
                            echo -n "Проверяется путь: ${array[i]} — "
                            if [ "${array[i]}" == "$o" ]
                                then
                                    echo -e "\033[32mdetected.\033[0m"
                                    j=${array[i]}
                                    par=1
                                else
                                    echo -e "\033[31mundetected.\033[0m"
                            fi
                        done
                    else
                        par=1
                        j=0
                    fi
            done
            if [ "$j" != "0" ]
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
                    echo -e "\033[35mИсполнен код выхода из скрипта.\033[0m"
            fi
    else
        echo -e "\033[31mДанного каталога не существует.\033[0m"
fi