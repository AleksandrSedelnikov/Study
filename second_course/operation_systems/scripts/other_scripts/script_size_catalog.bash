# первая реализация
du -sh -t10M /home/* 2>/dev/null > file1
du -sh -t10M /home/* 2>/dev/null | cut -f3 -d"/" > file2
echo "Пользователи, чьи каталоги больше 10Мб:"
paste file1 file2
rm file1 file2

# вторая реализация
Homes=$(cut -f6 -d":" /etc/passwd) #список домаш. каталогов пользователей
for i in $Homes
do
size=$(du -sh -t10M $i 2>/dev/null)
if [ "$size" != "" ]
then
user=$(grep -w $i /etc/passwd | cut -f1 -d:)
size_u=$(echo $size | cut -f1 -d" ")
echo "размер каталога пользователя $user больше 10Мб: $size_u"  
else
echo "размер каталога пользователя $user меньше 10Мб"
fi
done

# Скрипт принадлежит пользователю ubuntu-server virtual-usr (преподаватель Квиткова И.Г.) [C]