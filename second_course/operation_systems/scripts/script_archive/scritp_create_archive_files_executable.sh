script() {
    for i in "$1"/* # цикл по содержимому директории
    do
        if [ "$1/*" = $i ] # если каталог пустой, то пропускать этот каталог
        then
            continue # скип
        fi
        if [ -d "$i" ] # если i это директория
        then
            script "$i" # вызов функции с параметром директории

        elif [ -f "$i" ] && [ -x "$i" ] # если это файл и он исполняемый
        then
            echo $i # вернуть абсолютный путь до файла
        fi
    done
}
names=`script ~` # изначальный вызов функции и запись всех возвратов из неё в переменную names
tar -zcvf testArchive.tar.gz $names # создание сжатого архива с найденными файлами