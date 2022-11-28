script() {
    for i in "$1"/*
    do
        if [ -d "$i" ]
        then
            script "$i"

        elif [ -f "$i" ]
        then
            name=`echo $1 | sed "s/.*\///" | grep "D"`
            if [ "$name" != "" ]
            then
                echo $i
            fi
        fi
    done
}
names=`script ~`
tar -zcvf archive.tar.gz $names