script() {
    for i in "$1"/*
    do
        if [ "$1/*" = $i ] # если изначальный каталог пустой скипнуть данный i
        then
            continue # скип-скип i
        fi
	if [ -d "$i" ]
        then
	    #echo "$i это директория"
            script "$i"

        elif [ -f "$i" ] && [ -x "$i" ]
        then
	    #echo "$i это исполняемый файл"
            echo $i
	#else
	    #echo "$i не подошёл"
        fi
    done
}
names=`script ~`
#script ~
#echo $names
#tar -zcvf testArchive.tar.gz $names
