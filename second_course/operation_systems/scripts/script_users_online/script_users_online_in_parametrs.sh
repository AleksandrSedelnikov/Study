case $# in

*)
        count=0 # переменная для подсчёта количества сеансов в сети
        while [ -n "$1" ] # проверяется, если консольный параметр не пустая строка, то выполняется далее вайл
        do 
        echo "Проверяется пользователь: $1"
        a=`last | grep -w 'logged in' | cut -d" " -f1 | grep -w "$1" | wc -l` # ласт выводит все сеансы, греп ищет совпадения слов в кавычках в выполненной команде ласт, кат вырезает имя пользователя(1 столбец), второй греп ищет совпадения по введённому имени пользователя в списке пользователей онлайн, вц -л количество совпадений
        if [ $a = 1 ] # проверка если есть совпадения, то выполняется иф
                then
                        count=`expr $count + 1` # к переменной count добавляется единичка
                        echo "Пользователь $1 в сети." 
                        echo " "
                else
                        echo "Пользователь $1 не сети."
                        echo " "
        fi
        shift # переход к следующему параметру (был допустим такой список AP103_22 AP103_2, то после этой команды перейдёт к параметру AP103_2)
        done # если строка оказалась пустой (скрипт продолжает работу если даже параметры введены следующим способом: AP103_22 "пусто" AP103_2)
        echo "Количество пользователей по введённым именам в сети: $count" # выводится количество авторизованных сессий
;;
esac 