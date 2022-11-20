#include <iostream>
#include <cmath>
#include <locale>
#include <iomanip>

using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");
	double B[20];
	float a = 25.8,sum = 0.0,buff_one = 0.0;
	long double proizv = 1.0;
	int i,b;
	cout << "Изначальный массив: " << endl;
	for (i = 0; i < 20; i++)
	{
		B[i] = sqrt(abs(pow(i, 2) - a));
		cout << setw(6) << B[i] << endl;;
	}
	for (i = 5; i <= 10; i++)
	{
		sum += B[i];
	}
	for (i = 5; i <= 10; i++)
	{
		for (b = 5; b <= 10; b++)
		{
			if (B[i] > B[b])
			{
				buff_one = B[i];
				B[i] = B[b];
				B[b] = buff_one;
			}
		}
	}
	cout << endl;
	cout << "Полученный массив: " << endl;
	for (i = 0; i < 20; i++)
	{
		cout << setw(6) << B[i] << endl;;
	}
	for (i = 0; i < 20; i++)
	{
		if (B[i] < 8.5)
		{
			proizv *= B[i];
		}
	}
	cout << endl;
	cout << "Сумма элементов с 5-го по 10-ый (до преобразования): " << sum << ", Произведение элементов меньше 8.5: " << proizv << endl;
}