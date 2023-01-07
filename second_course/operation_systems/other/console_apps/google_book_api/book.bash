# check availability
result=`find / -name "jq" 2>~/error`
if [ "$result" == "" ]
    then
        echo -e "\033[01;91mModule jq not found in this system\033[00;0m"
        exit
fi

# default option
default_lang="ru"
default_sort="rel"
default_maxres=2
checkone=0

# check input option
echo -e "\033[01;97mChecking input options...\033[00;0m"
sleep 1
for i in "$@"
    do
        case $i in
        -q=* | --query=*)
            QUERY="${i#*=}"
            shift
        ;;
        -l=* | --lang=*)
            LANGUAGE="${i#*=}"
            shift
        ;;
        -s=* | --sort=*)
            SORT="${i#*=}"
            shift
        ;;
        -m=* | --maxres=*)
            MAXRES="${i#*=}"
        ;;
        -h | --help)
            echo -e "Main option:\n-m=[number]/--maxres=[number] - number of results, range [1-40]\n-l=[language]/--lang=[language] - language of the books(there is no verification of the correctness of the language)\n-s=[sort]/--sort=[sort] - type of sorting (rel - relevation, date - date of publication)\nIMPORTANT option -q="text"/--query=[text] or [word1word2...wordn] - search by phrase\n\nColor Indication:\n\033[01;91mRed\033[00;0m - Error\n\033[01;93mYellow\033[00;0m - Warning\n\033[01;92mGreen\033[00;0m - Good"
            exit
        esac
    done
if [ "$QUERY" == "" ] || [ `echo $QUERY | wc -w` -ne 1 ]
    then
        echo -e "\033[01;91mWrong option query!\033[00;0m"
        checkone=1
fi
if [ "$LANGUAGE" == "" ] || [ `echo $LANGUAGE | wc -w` -ne 1 ]
    then
        echo -e "\033[01;93mWrong lang, the standard value is selected!\033[00;0m"
        LANGUAGE=$default_lang
fi
if [ "$SORT" == "" ] || [ `echo $SORT | wc -w` -ne 1 ]  
    then
        echo -e "\033[01;93mWrong sort, the standard value is selected!\033[00;0m"
        SORT=$default_sort
fi
if [ "$SORT" != "rel" ] && [ "$SORT" != "date" ]
    then
        echo -e "\033[01;93mWrong sort, the standard value is selected!\033[00;0m"
        SORT=$default_sort
fi
if [ "$MAXRES" == "" ] || [ `echo $MAXRES | wc -w` -ne 1 ]
    then
        echo -e "\033[01;93mWrong maxres, the standard value is selected!\033[00;0m"
        MAXRES=$default_maxres
fi
if [ $MAXRES -gt 40 ] || [ $MAXRES -lt 1 ]
    then
        echo -e "\033[01;93mWrong maxres, maximum 40 results and minimum 1 result\nThe standard value is selected!\033[00;0m"
        MAXRES=$default_maxres
fi
if [ "$SORT" == "rel" ]
    then
        SORT="relevance"
elif [ "$SORT" == "date" ]
    then
        SORT="newest"
fi
if [ "$checkone" -eq 1 ]
    then
        echo -e "\033[01;91mInput validation is broken\033[00;0m\n\033[01;97mCheck option -h/--help\033[00;0m"
        exit
fi
echo -e "\033[01;92mInput verification completed\033[00;0m"
echo -e "\033[01;97mReceived options:\033[00;0m\n\033[01;93mQuery:\033[00;0m \033[01;97m$QUERY\033[00;0m\n\033[01;93mLanguage:\033[00;0m \033[01;97m$LANGUAGE\033[00;0m\n\033[01;93mSort:\033[00;0m \033[01;97m$SORT\033[00;0m\n\033[01;93mMaxResult:\033[00;0m \033[01;97m$MAXRES\033[00;0m" 

# Decor
sleep 3
echo -e "\033[01;97mPlease waiting...\033[00;0m"
sleep 5
echo -e "\033[01;97mOutputting...\033[00;0m"
# Decor

# parse json output
book=`curl -G "https://www.googleapis.com/books/v1/volumes?q=$QUERY&maxResults=$MAXRES&orderBy=$SORT&langRestrict=$LANGUAGE" 2>~/error`
for ((i=0;i<$MAXRES;i++))
    do
        auth=`echo $book | jq -r ".items[$i].volumeInfo.authors" | cut -d"[" -f2 | cut -d"]" -f1`
        title=`echo $book | jq -r ".items[$i].volumeInfo.title" | cut -d"[" -f2 | cut -d"]" -f1`
        publisher=`echo $book | jq -r ".items[$i].volumeInfo.publisher" | cut -d"[" -f2 | cut -d"]" -f1`
        publishedDate=`echo $book | jq -r ".items[$i].volumeInfo.publishedDate" | cut -d"[" -f2 | cut -d"]" -f1`
        description=`echo $book | jq -r ".items[$i].volumeInfo.description" | cut -d"[" -f2 | cut -d"]" -f1`
        pageCount=`echo $book | jq -r ".items[$i].volumeInfo.pageCount" | cut -d"[" -f2 | cut -d"]" -f1`
        pdf=`echo $book | jq -r ".items[$i].accessInfo.pdf.isAvailable" | cut -d"[" -f2 | cut -d"]" -f1`
        epub=`echo $book | jq -r ".items[$i].accessInfo.epub.isAvailable" | cut -d"[" -f2 | cut -d"]" -f1`
        link=`echo $book | jq -r ".items[$i].accessInfo.webReaderLink" | cut -d"[" -f2 | cut -d"]" -f1`
        price_amount=`echo $book | jq -r ".items[$i].saleInfo.listPrice.amount" | cut -d"[" -f2 | cut -d"]" -f1`
        price_code=`echo $book | jq -r ".items[$i].saleInfo.listPrice.currencyCode" | cut -d"[" -f2 | cut -d"]" -f1`
        #lang=`echo $book | jq -r ".items[$i].volumeInfo.language" | cut -d"[" -f2 | cut -d"]" -f1`
        if [ "$pdf" == "true" ]
            then
                if [ "$epub" == "true" ]
                    then
                        access="pdf,epub"
                    else
                        access="pdf"
                fi
        else
            if [ "epub" == "true" ]
                then
                    access="epub"
            else
                access="not"
                fi
        fi
        # output infortation for $i book
        echo "= = ="
        echo "Название: $title"
        echo "Автор(-ы): $auth"
        echo "Аннотация: $description"
        echo "Издательство: $publisher"
        echo "Дата публикации: $publishedDate"
        echo "Количество страниц: $pageCount"
        echo "Стоимость: $price_amount $price_code"
        echo "Формат(pdf,epub): $access"
        echo "Ссылка на просмотр фрагмента: $link"
        #echo "Debag language: $lang"
        echo "= = ="
        echo ""
    done
echo -e "\033[01;92mOutput comleted\033[00;0m"



# other variant (not all values)

#grep -Po '"title":.*?[^\\]",' - Название
#grep -Po '"publisher":.*?[^\\]",' - Издательство
#grep -Po '"description":.*?[^\\]",' - Аннотация
#grep -Po '"webReaderLink":.*?[^\\]",' - Ссылка на просмотр фрагмента
#grep -Po '"publishedDate":.*?[^\\]",' - Дата публикации