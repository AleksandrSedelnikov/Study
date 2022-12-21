echo "Введи имя пользователя"
read name
grep -w $name /etc/passwd > ~/file1
if [ $? -eq 0 ]
then
UID=`grep -w $name /etc/passwd | cut -f3 -d":"`
GID=`grep -w $name /etc/passwd | cut -f4 -d":"`
Home=`grep -w $name /etc/passwd | cut -f6 -d":"`
echo "У пользователя $name следующие параметры:"
echo "UID - $UID, GID - $GID, домашний каталог - $Home"
echo "Содержимое домашнего каталога $Home:"
ls -lR $Home
else
echo "Пользователя с именем $name нет"
fi

# Скрипт принадлежит пользователю ubuntu-server virtual-usr (преподаватель Квиткова И.Г.) [C]