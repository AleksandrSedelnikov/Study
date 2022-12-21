du -sh -t10M /home/* 2>/dev/null > file1
du -sh -t10M /home/* 2>/dev/null | cut -f3 -d"/" > file2
echo "Пользователи, чьи каталоги больше 10Мб:"
paste file1 file2
rm file1 file2


# Скрипт принадлежит пользователю ubuntu-server virtual-usr (преподаватель Квиткова И.Г.) [C]