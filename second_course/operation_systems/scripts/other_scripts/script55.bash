file=`find ~ -name $1 -type f 2>~/error`
if [ "$file" != "" ]
then
count=`grep -w "$2" $file | wc -l`
echo "The word: $2 occurs $count times"
else
echo "File $1 do not exist" 
fi
