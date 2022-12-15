script() {
    echo "Директория: $1"
    for i in "$1"/*
    do
	name=""
        if [ -d "$i" ]
        then
	    name=`echo $i | sed "s/.*\///"`
	    if [ "$name" != "AP103_22" ]
	    then
	    tar -zcvf $name.tar.gz $i
	    mv $name.tar.gz ~/testing_page/archives
	    fi
            script "$i"
    	fi
    done
}
script ~
