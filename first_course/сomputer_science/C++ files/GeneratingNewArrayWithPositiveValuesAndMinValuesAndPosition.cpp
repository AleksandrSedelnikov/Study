#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;

int main()
{
	int i = 0, j = 0, k = 0, nom = 0;
	double min = 99999;
	double A[5][5]{
		{-3.8, 0, 5.3, 4.5, 0.5 },
		{0.2, -1.3, 0, -8.5, 3.5},
		{-1.1, 1.8, 5.1, -8.2, 0.32},
		{0, -0.3, 0, -1.28, 0.52},
		{-0.3, 0.5, 1.8, -7.3, 5.5}
	};
	double X[25];
	cout << "Изначальная матрица: " << endl;
	for (i = 0; i < 5; i++)
	{
		for (j = 0; j < 5; j++)
		{
			cout << setw(6) << A[i][j];
			if (A[i][j] > 0)
			{
				X[k] = A[i][j];
				k++;
			}
		}
		cout << endl;
	}
	cout << endl;
	cout << "Получившийся массив X: " << endl;
	for (i = 0; i < k; i++)
	{
		cout << setw(6) << X[i];
		if (X[i] < min)
		{
			min = X[i];
			nom = i;
		}
	}
	cout << endl;
	cout << "Минимальный элемент массива X: " << min << " " << ", его номер: " << nom + 1 << endl;
	return 0;
}