case $# in 
	1)
		echo "Введён один параметр."
		proverka=`find ~ -name "$1" -type f 2>~/error`
		proverka_1=`find ~ -name "$1" -type f 2>~/error | wc -l`
		if [ "$proverka_1" == 1 ]
			then
				echo "Введите текст: "; read text
				echo "$text" >> $proverka
			else
                                echo "Error: script crashed"
		fi
	;;
	2)
		echo "Введено два параметра."
		proverka2=`find ~ -name "$1" -type f 2>~/error`
		proverka3=`find ~ -name "$2" -type f 2>~/error`
		proverka2_1=`find ~ -name "$1" -type f 2>~/error| wc -l`
		proverka3_1=`find ~ -name "$2" -type f 2>~/error| wc -l`
		echo $proverka2_1
		echo $proverka3_1
		if [ "$proverka2_1" == 1 ] && [ "$proverka3_1" == 1 ]
			then
				echo "Информация из файла 2 скопирована в файл 1."
				cat $proverka3 >> $proverka2
			else
                                echo "Error: script crashed"
		fi	 
	;;
esac

