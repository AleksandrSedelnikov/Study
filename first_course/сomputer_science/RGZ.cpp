#include <iostream>
#include <time.h>
#include <iomanip>
#include <locale>
#include <fstream>
#include <stdlib.h>

using namespace std;

void massiv(int **mass,int n, int m)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			mass[i][j] = rand() % 201 - 100;
		}
	}
}

void massiv1(int** mass, int n, int m)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cout << "Введите (" << i << " " << j << ") значение в массив: ";
			cin >> mass[i][j];
		}
	}
}

void massiv2(int** mass, int n, int m)
{
	ifstream InFile("text.txt");
	if (InFile)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				InFile >> mass[i][j];
			}
		}
	}
	else
	{
		cout << endl;
		cout << "\t\t\t\t\t\t********************" << endl;
		cout << "\t\t\t\t\t\t***File not found***" << endl;
		cout << "\t\t\t\t\t\t********************" << endl;
		exit(404);
	}
}

void massivout(int **mass, int n, int m)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cout << setw(7) << mass[i][j];
		}
		cout << endl;
	}
}

void glav(int** mass, int n, int m)
{
	int k = 0;
	for (int i = 0, j = 0; i < n, j < m; i++, j++)
	{
		if (mass[i][j] < 0)
		{
			k++;
		}
	}
	cout << endl;
	cout << "\tКоличество отрицательных чисел в главной диагонали матрицы: " << k << endl;
}

void uvelich(int** mass, int n, int m)
{
	int j = 1;
	for (int i = 0; i < n; i++)
	{
		mass[i][j] += 9;
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cout << setw(7) << mass[i][j];
		}
		cout << endl;
	}
}




int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));
	int v,flag = 0;
	int **mass;
	int n = 6, m = 6;
	mass = new int *[n];
	for (int i = 0; i < n; i++)
	{
		mass[i] = new int[m];
	}
	cout << "\t\t\t***********************************************************" << endl;
	cout << "\t\t\t***Добро пожаловать в консоль отладки РГР по информатике***" << endl;
	cout << "\t\t\t***********************************************************" << endl;
	cout << "\t\t***Выполнил студент Института Телекоммуникаций, группы АП-103 Седельников А.С.***" << endl;
	cout << "\t\t\t\t\t***Вариант 14***" << endl;
	cout << "\t   В данной программе вы можете реализовать формирование массива с помощью 3-х способов:     \n\t    (1) - датчик рандомных чисел\n\t    (2) - ввод с клавиатуры\n\t    (3) - ввод из файла" << endl;
	cout << "\t   После генерации массива любым из способов, вы сможете:    \n\t    (*)узнать количество отрицательных чисел в главной диагонали матрицы\n\t    (*)увеличить второй столбец матрицы на 9" << endl;
	while (flag == 0)
	{
		cout << "\t   Для выбора варианта генерации массива, введите номер варианта(пример: 1): ";
		cin >> v;
		cout << endl;
		if (v == 1)
		{
			cout << "\t   Вы выбрали генерацию массива с помощью датчика случайных чисел." << endl;
			massiv(mass, n, m);
			flag = 1;
		}
		if (v == 2)
		{
			cout << "\t   Вы выбрали генерацию массива с помощью ввода значений с клавиатуры." << endl;
			massiv1(mass, n, m);
			flag = 1;
		}
		if (v == 3)
		{
			cout << "\t   Вы выбрали генерацию массива с помощью ввода значений из файла (text.txt)." << endl;
			massiv2(mass, n, m);
			flag = 1;
		}
		if (v != 1 && v != 2 && v != 3)
		{
			cout << "\t\t\t\t\t***Warning!***" << endl;
			cout << "\t***Введён неверный номер варианта генерации массива, повторите ввод варианта повторно***" << endl;
			flag = 0;
		}
	}
	cout << endl;
	cout << "\tГенерация массива по варианту: "<< v << "..." << endl;
	cout << endl;
	massivout(mass,n,m);
	glav(mass, n, m);
	cout << endl;
	cout << "\tУвеличение второго столбца матрицы на 9: " << endl;
	cout << endl;
	uvelich(mass, n, m);
	cout << endl;
	cout << "\t\t\t\t\t\t*********************" << endl;
	cout << "\t\t\t\t\t\t***Конец программы***" << endl;
	cout << "\t\t\t\t\t\t*********************" << endl;
	return 0;
}