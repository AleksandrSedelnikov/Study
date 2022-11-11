echo -n "Введите необходимый каталог для выполнения скрипта: "; read add # вводится название каталога
add_1=`find ~ -name $add -type d 2>~/error` # поиск пути до указанного каталога
add_2=`find ~ -name $add -type d 2>~/error | wc -l` # проверка на единичность пути
if [ "$add_1" != "" ] && [ "$add_2" == 1 ]  # проверка существует ли каталог и у него единичный путь
	then
		echo "Введите необходимую итерацию(1 - поиск числа ненулевых файлов | 2 - поиск числа файлов с правом запуска | 3 - поиск числа подкаталогов): "; read variant
		echo "Согласно Вашему выбору каталога [$add] и итерации [$variant] ответ: "
		if [ "$variant" != "1" ] && [ "$variant" != "2" ] && [ "$variant" != "3" ] # проверка введённого варианта итерации
		then 
			echo "Выбран неверный вариант итерации!" # ошибка в случае неверного номера итерации
		else
			case $variant in # массив команд для номеров итераций
			"1")
				find $add_1 -maxdepth 1 -type f -size +0b 2>~/error  | wc -l # поиск ненулевых файлов в введённом каталоге
				echo "Поиск выполнен."
			;;
			"2")
				find $add_1 -maxdepth 1 -type f -perm /u=x -and -perm /g=x -and -perm /o=x 2>~/error | wc -l # поиск файлов с разрешением на выполнение в введённом каталоге
				echo "Поиск выполнен."
			;;
			"3")
				g=`find $add_1 -maxdepth 1 -not -path '*/\.*' -type d 2>~/error | wc -l` # поиск подкаталогов в введённом каталоге (скрытый каталог "." считывает за подкаталог)
				if [ "$g" != 0 ] # проверка на наличие хоть одного видимого каталога
					then # если есть хоть один видимый каталог
						f=`expr $g - 1` # убирается лишнее срабатывание поиска на скрытый каталог "."
						echo "$f" # выводится количество подкаталогов
						echo "Поиск выполнен."
					else # если каталогов вообще нет
						echo "$g" # выводится количество подкаталогов
						echo "Поиск выполнен."
				fi
			;;
			esac
		fi 
	else echo "Данного каталога не существует или таких каталогов несколько." # ошибка в случае непрохождения проверки на существование и единственность пути
fi
echo "Скрипт завершил свою работу." # скрипт завершил свою работу