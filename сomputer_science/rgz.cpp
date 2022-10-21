#include <iostream>
#include <time.h>
#include <iomanip>
#include <locale>
#include <fstream>

using namespace std;

void massiv(int** mass, int n, int m)
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
	else cout << "\tFail not found" << endl;
}

void massivout(int** mass, int n, int m)
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

void poloz(int** mass, int n, int m)
{
	int k = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (mass[i][j] > 0)
			{
				k++;
			}
		}
	}
	cout << endl;
	cout << "\tКоличество положительных чисел в матрице: " << k << endl;
}

void uvelich(int** mass, int n, int m)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (mass[i][j] < 0)
			{
				mass[i][j] += 4;
			}
		}
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
	int v, flag = 0;
	int** mass;
	int n = 5, m = 5;
	mass = new int* [n];
	for (int i = 0; i < n; i++)
	{
		mass[i] = new int[m];
	}
	cout << "\t   В данной программе вы можете реализовать формирование массива с помощью 3-х способов:     \n\t    (1) - датчик рандомных чисел\n\t    (2) - ввод с клавиатуры\n\t    (3) - ввод из файла" << endl;
	while (flag == 0)
	{
		cout << "\t   Для выбора варианта генерации массива, введите номер варианта(пример: 1): ";
		cin >> v;
		if (v == 1)
		{
			massiv(mass, n, m);
			flag = 1;
		}
		if (v == 2)
		{
			massiv1(mass, n, m);
			flag = 1;
		}
		if (v == 3)
		{
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
	massivout(mass, n, m);
	poloz(mass, n, m);
	cout << endl;
	cout << "\tУвеличение всех отрицательных элементов матрицы на 4: " << endl;
	cout << endl;
	uvelich(mass, n, m);
	return 0;
}