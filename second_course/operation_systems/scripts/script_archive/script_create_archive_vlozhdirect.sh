script() {
    for i in "$1"/*
    do
	name=""
        if [ -d "$i" ]
        then
	    name=`echo $i | sed "s/.*\///"`
        myname=`whoami`
	    if [ "$name" != "$myname" ] && [ "$name" != "archives" ] # не создавать архив домашней директории и папки с архивами
	    then
	    tar -zcvf $name.tar.gz $i # создать архив с содержимым директории
	    mv $name.tar.gz ~/archives # отправить архив в папку в домашней директории с названием archives
	    fi
            script "$i"
    	fi
    done
}
script ~