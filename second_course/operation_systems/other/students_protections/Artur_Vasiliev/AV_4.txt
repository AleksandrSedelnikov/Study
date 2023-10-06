# если файла a_sort нет, то создаём (файл a3d1 должен быть)
cat a3d1 | sort -k2 > a_sort # сортировка файла a3d1 по второму столбцу

cd D1_1
mkdir -m 756 LSORT
cd LSORT
ln -s "пусть до файла a1" a1_symbol
ln -s "путь до файла a_sort" a_sort_symbol