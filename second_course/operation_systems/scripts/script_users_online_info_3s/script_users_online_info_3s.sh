# не работает [?]
#id=`ps u | grep "bash script_j"| grep -v "color" | cut -d" " -f2,3`
#trap "echo 'ID proccess $id'" SIGTSTP

true=1
while [ $true -eq 1 ]
do
a=`last | grep -w 'logged in' | cut -d" " -f1`
co=`echo `last | grep -w 'logged in' | cut -d" " -f1``
array=($a)
for i in $a
do
    flag=0
    for ((j=0;j<${#array[@]};j++))
    do
        if [ ${array[j]} = $i ]
        then
            array[j]=name
            flag=1
        fi
    done
    if [ $flag -eq 1 ]
    then
        echo "========"
        echo "User: $i"
        count=`echo $i | wc -c`
        count_1=`expr $count - 1`
        if [ $count_1 -eq 8 ]
        then        
            terminals=`who | grep -w "$i" | cut -d" " -f2`
            for s in $terminals
            do
                echo "Terminal: $s"
                count2=`echo $s | wc -c`
                count2_1=`expr $count2 - 1`
                if [ $count2_1 -eq 5 ]
                then
                    ip=`who | grep -w "$s" | cut -d" " -f12`
                else
                    ip=`who | grep -w "$s" | cut -d" " -f11`
                fi
                echo "IP: $ip"
                proccess=`ps -A | grep "$s"`
                echo "Proccess (PID TERMINAL TIME COMMAND):"
                echo $proccess
                echo "========"
            done
        else
            terminals=`who | grep -w "$i" | cut -d" " -f3`
            for s in $terminals
            do
                echo "Terminal: $s"
                count2=`echo $s | wc -c`
                count2_1=`expr $count2 - 1`
                if [ $count2_1 -eq 6 ]
                then
                    ip=`who | grep -w "$s" | cut -d" " -f12`
                else
                    ip=`who | grep -w "$s" | cut -d" " -f13`
                fi
                echo "IP: $ip"
                proccess=`ps -A | grep "$s"`
                echo "Proccess (PID TERMINAL TIME COMMAND):"
                echo $proccess
                echo "========"
            done
        fi
    fi
done
sleep 3
done