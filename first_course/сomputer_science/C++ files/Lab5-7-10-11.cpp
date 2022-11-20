#include <iostream>
#include <iomanip>
#include <time.h>
#include <cstdlib>

using namespace std;

void des_lab(int** mass, int n, int m)
{
	int summ = 0;
	int count = 0;
	int i = 0, j = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			mass[i][j] = rand() % 10 - 5;
			cout << setw(6) << mass[i][j];
		}
		cout << endl;
	}
	for (i = 0; i < n ; i++)
	{
		for (j = 0; j < m; j++) // i < j
		{
			if (j > i)
			{
				summ += mass[i][j];
				count += 1;
			}
		}
	}
	cout << endl;
	cout << summ << endl;
}

int od_lab(int** mass, int n, int m)
{
	int summ = 0;
	int i = 0, j = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			mass[i][j] = rand() % 10 - 5;
			cout << setw(6) << mass[i][j];
		}
		cout << endl;
	}
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++) // i < j
		{
			if (j > i)
			{
				summ += mass[i][j];
			}
		}
	}
	return summ;
}

void s_lab()
{
	int i, j, h = 0, g = 0, k = 0, l = 0;
	float d_max = 0, d_min = 99999, q = 0.0;
	float mass[5][5]
	{
		{-3.8 , 0 , 5.3 , 4.5, 0.5 },
		{ 0.2 , -1.3 , 0 , -8.5 , 3.5 },
		{ -1.1 , 1.8 , 5.1 , -8.2 , 0.32 },
		{ 0 , -0.3 , 0 , -1.28 , 0.52 },
		{ -0.3 , 0.5 , 1.8 , -7.3 , 5.5 }
	};
	cout << "Исходная матрица: " << endl;
	for (i = 0; i < 5; i++)
	{
		for (j = 0; j < 5; j++)
		{
			cout << setw(6) << mass[i][j];
			if (mass[i][j] > d_max)
			{
				d_max = mass[i][j];
				h = i;
				g = j;
			}
			else if (mass[i][j] < d_min)
			{
				d_min = mass[i][j];
				k = i;
				l = j;
			}
		}
		cout << endl;
	}
	cout << endl;
	cout << "Максимальное значение и его позиция: " << d_max << " (" << h << ";" << g << ") " << endl;
	cout << "Минимальное значение и его позиция: " << d_min << " (" << k << ";" << l << ") " << endl;
	q = mass[h][g];
	mass[h][g] = mass[k][l];
	mass[k][l] = q;
	cout << endl;
	cout << "Полученная матрица: " << endl;
	for (i = 0; i < 5; i++)
	{
		for (j = 0; j < 5; j++)
		{
			cout << setw(6) << mass[i][j];
		}
		cout << endl;
	}

}

void p_lab()
{
	int n, i, count_p = 0, count_o = 0;;
	double sum = 0.0, arif = 0.0,chislo = 0.0;
	cout << "Введите количество чисел в последовательности: "; cin >> n;
	for (i = 0; i < n; i++)
	{
		cout << "Введите " << i + 1 << " число последовательности: "; cin >> chislo;
		if (chislo > 0)
		{
			sum += chislo;
			count_p++;
		}
		else if (chislo < 0)
		{
			count_o++;
		}
	}
	arif = sum / count_p;
	cout << "Среднее арифметическое положительных значений: " << arif << " " << "Количество отрицательных значений: " << count_o << endl;
}

int main()
{
	system("chcp 1251");
	/*srand(time(NULL));
	int n, m,v;
	int count = 0;
	cout << "Введите размерность массива: " << endl;
	cout << "Введите a: ";
	cin >> n;
	cout << "Введите b: ";
	cin >> m;
	int** mass;
	mass = new int* [n];
	for (int i = 0; i < n; i++)
	{
		mass[i] = new int[m];
	}
	des_lab(mass,n,m);
	count = od_lab(mass, n, m);
	cout << endl;
	cout << count << endl;
	s_lab();
	p_lab();
	*/
	return 0;
} 