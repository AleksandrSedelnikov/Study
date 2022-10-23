a=`last | grep -w 'logged in' | cut -d" " -f1`
echo $a