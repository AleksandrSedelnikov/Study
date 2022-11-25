script() {
    for i in "$1"/*
    do
        if [ "$1/*" = $i ]
        then
            continue
        fi
        if [ -d $i ]
        then
            script $i
        elif [ -f $i ]
        then
            result=`echo $i | sed "s/.*\///" | grep "a"`
            if [ "$result" != "" ]
            then
                echo $i
            fi
        fi
    done
}
names=`script ~`
tar -zcvf archive.tar.gz $names
