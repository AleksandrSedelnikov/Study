a=`ls -la | egrep -v ^d | awk '{print $2 " " $9}' | sed '1d'`
count=`ls -la | egrep -v ^d | awk '{print $2 " " $9}' | sed '1d' | wc -l`
for ((i=1;i<=$count;i++))
    do
        line=`ls -la | egrep -v ^d | awk '{print $2 " " $9}' | sed '1d' | sed -n $i"p"`
        hard=`echo $line | awk '{print $1}'`
        if [ $hard  -ne 1 ]
            then
                echo $line | awk '{print $2}' >> result
        fi
done