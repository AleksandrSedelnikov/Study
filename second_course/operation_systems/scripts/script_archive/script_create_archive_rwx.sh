func() {
if [ "$1" = "1" ]
then
    for i in "$2/"*
    do
    if [ -r "$i" ]
    then
        echo $i
    fi
    done
fi
if [ "$1" = "2" ]
then
    for i in "$2/"*
    do
    if [ -w "$i" ]
    then
        echo $i
    fi
    done
fi
if [ "$1" = "3" ]
then
    for i in "$2/"*
    do
    if [ -x "$i" ]
    then
        echo $i
    fi
    done
fi
}
dir=`pwd`
namer=`func 1 $dir`
namew=`func 2 $dir`
namex=`func 3 $dir`
tar -zcvf readfile.archive.tar.gz $namer
tar -zcvf writefile.archive.tar.gz $namew
tar -acvf executablefile.archive.tar.gz $namex