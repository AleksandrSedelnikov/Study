#!/bin/bash
echo "Введите номер операции"
echo "1) имя машины"
echo "2) время в сек. с момента запуска командной оболочки."
echo "3) тип терминала"
echo "4) текущая командная оболочка"
echo "5) путь к домашнему каталогу текущего пользователя"
echo "6) текущий каталог"
echo "7) все"
read i
case $i in 
	1) echo $HOSTNAME;;
	2) echo $SECONDS;;
	3) echo $TERM;;
	4) echo $SHELL;;
	5) echo $HOME;;
	6) echo $PWD;;
	7) echo $HOSTNAME;echo $SECONDS;echo $TERM;echo $SHELL;echo $HOME;echo $PWD;;
	*) echo "Неверно указан запрос";;
esac


# Скрипт принадлежит пользователю ubuntu-server virtual-usr (преподаватель Квиткова И.Г.) [C]