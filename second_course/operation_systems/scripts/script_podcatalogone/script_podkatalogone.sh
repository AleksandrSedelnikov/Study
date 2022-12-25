
# первый способ, через find и количество выводов
echo -n "введите абсолютный путь до каталога: "; read var
if [ `find $var -type d 2>~/error | wc -l` -eq 1 ]
    then
        echo "в каталоге $var нет подкаталогов"
    else
        name=`echo $var | sed "s/.*\///"`
        for i in "$var"/*
            do
                if [ -d "$i" ]
                    then
                        if [ `find $i -type d 2>~/error | wc -l` -eq 1 ]
                            then
                                echo "В подкаталоге $i нет подкаталогов"
                                #tar -rf archive_$name.tar $i
                            else
                                echo "В подкаталоге $i есть подкаталоги"
                        fi
                fi
            done
        #gzip -c archive_$name.tar > archive_$name.tar.gz
        #rm archive_$name.tar
fi




# второй способ, через счётчик количества /
echo -n "введите полный путь до каталога: "; read dir
if [ `find $dir -type d 2>~/error | wc -l` -eq 1 ]
    then
        echo "в каталоге $dir нет подкаталогов"
    else
        name=`echo $dir | sed "s/.*\///"`
        for i in `find $dir -type d 2>~/error`
            do
                if [ "$i" != "$dir" ]
                    then
                        count=`echo $i | tr -cd "/" | wc -m`
                        count_cur=`echo $dir | tr -cd "/" | wc -m`
                        count_curr=`expr $count - $count_cur`
                        if [ $count_curr -eq 1 ]
                            then
                                count_dir=`find $i -type d 2>~/error | wc -l`
                                if [ $count_dir -eq 1 ]
                                    then
                                        echo $i
                                        #tar -rf archive_$name.tar $i
                                fi
                        fi
                fi
            done
            #gzip -c archive_$name.tar > archive_$name.tar.gz
            #rm archive_$name.tar
fi