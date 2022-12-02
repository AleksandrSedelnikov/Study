script() {
    for i in "$1"/*
    do
        if [ -d "$i" ]
        then
            script "$i"

        elif [ -f "$i" ] && [ -x "$i" ]
        then
            echo $i
        fi
    done
}
names=`script ~`
tar -zcvf testArchive.tar.gz $names