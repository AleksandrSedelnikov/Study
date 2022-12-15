script() {
    for i in "$1"/*
    do
        if [ -d "$i" ]
        then
            script "$i"
        elif [ -f "$i" ]
        then
                count=`expr $count + 1`
		echo $count
        fi
    done
}
count=0
count_cur=`script ~`
count_res=`echo $count_cur | wc -w`
echo "Количество файлов в домашней директории: $count_res"

