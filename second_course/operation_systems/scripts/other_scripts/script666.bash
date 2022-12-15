#!/bin/bash
ping -c 1 $1 | grep "100% packet loss"
if [ $? -eq 0 ]
then
echo "хост недоступен"
else
echo "символьное имя доменное имя"
echo "`nslookup $1 | grep -w "name"`"
fi
