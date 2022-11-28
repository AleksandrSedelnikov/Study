for ((i=0;i<50;i++))
do
echo $(($RANDOM %1000 + 1)) >> text1
echo $(($RANDOM %100 + 1)) >> text2
done