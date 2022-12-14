# запустить данный скрипт с помощью nice "название скрипта" (таким образом дочерние скрипты унаследуют данный приоритет)

result=`find ~ -perm /ugo=x -type f 2>~/error` # поиск файлов с правом на выполнение для: пользователя,группы,остальных
for i in $result # цикл i в количестве найденных файлов
    do
        source $i > /dev/null # запустить файл с приоритетом 10, однако если это файл с выводом на экран (например скрипт, который будет ждать от вас ответа, то остальные файлы не будут стартовать)
        source $i > /dev/null &  # запустить файл с приоритетом 10 в фоне, тогда все файлы запустятся, т.к. на экран ничего выводить не нужно будет (из-за того что фоновый процесс)
    done
# * "> /dev/null" можно отбросить, это было для теста команды yes