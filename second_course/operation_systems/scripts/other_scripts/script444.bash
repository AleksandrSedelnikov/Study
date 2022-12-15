func() {
echo $1
if [ "$1" = "1" ]
then
    for i in "./"*
    do
    if [ -r "$i" ]
    then
        echo $i
    fi
    done
fi
if [ "$1" = "2" ]
then
    for i in "./"*
    do
    if [ -w "$i" ]
    then
        echo $i
    fi
    done
fi
if [ "$1" = "3" ]
then
    for i in "./"*
    do
    if [ -x "$i" ]
    then
        echo $i
    fi
    done
fi
}
namer=`func 1`
namew=`func 2`
namex=`func 3`
tar -zcvf readfile.archive.tar.gz $namer
tar -zcvf writefile.archive.tar.gz $namew
tar -acvf executablefile.archive.tar.gz $namex
