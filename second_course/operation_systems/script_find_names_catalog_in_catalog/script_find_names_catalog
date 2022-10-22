
o=`find ~ -name "dir" -type d 2>~/error`
l=`echo $o | grep -o "/" | wc -l`
d=`expr $l + 2`
k=`ls -d $o/*/ | cut -f"$d" -d'/'`
echo $k