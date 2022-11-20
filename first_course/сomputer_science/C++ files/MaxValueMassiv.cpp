#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main()
{
	srand(time(NULL));
	system("chcp 1251");
	int* mass, *create;
	int i,j = 0,max_count = -99999;
	int n;
	int sum = 0;
	cout << "Введите размерность массива: ";
	cin >> n;
	mass = new int [n];
	create = new int[n];
	cout << "Исходный массив:" << endl;
	for (i = 0; i < n; i++)
	{
		mass[i] = rand() % 201 - 100;
		cout << setw(4) << mass[i];
	}
	cout << endl;
	for (i = 0; i < n; i++)
	{
		if (mass[i] % 2 == 0)
		{
			create[j] = mass[i];
			j++;
		}
	}
	for (i = 0; i < j; i++)
	{
		if (max_count < create[i])
		{
			max_count = create[i];
		}
	}
	cout << endl;
	cout << "Получившийся массив: " << endl;
	for (i = 0; i < j; i++)
	{
		cout << setw(4) << create[i];
	}
	cout << endl;
	cout << "Максимальный элемент в получившемся массиве: " << max_count << endl;
	
}