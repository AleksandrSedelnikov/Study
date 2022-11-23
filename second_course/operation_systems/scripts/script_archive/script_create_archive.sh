function script() {
    names=`ls -l | egrep -v ^d | grep "a" | awk '{print $9}'` # только домашние файлы (не заходить в директории)
    #names=names=`find ~ -name "*a*" -type f 2>~/error` # заходить во все директории
    count=`echo $names | wc -w`
    tar -zcvf archive.tar.gz $names
}
script
