tt=1000.0
ip=`traceroute -q 1 -U $1 | awk 'NR>=2' | awk '{print $3 $4}'`
for i in $ip
do
cur_ip=`echo $i | cut -d"(" -f2 | cut -d")" -f1`
cur_time=`echo $i | cut -d")" -f2`
if [ $(echo "$cur_time < $tt" | bc -l) -eq 1 ]
then
echo -e "Ответ узла с IP - \033[01;97m$cur_ip\033[00;0m \033[01;92mвошёл\033[00;0m в промежуток до $tt ms, его время - \033[01;97m$cur_time\033[00;0m ms"
else
echo -e "Ответ узла с IP - \033[01;97m$cur_ip\033[00;0m \033[01;91mне вошёл\033[00;0m в промежуток до $tt ms, его время - \033[01;97m$cur_time\033[00;0m ms"
fi
done
