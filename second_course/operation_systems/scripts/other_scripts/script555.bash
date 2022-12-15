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
echo "check"

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
}
func 1
