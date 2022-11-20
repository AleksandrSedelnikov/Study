#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	double min=99999,summ = 0;
	int i, j = 0,k=0,o = 0;
	double X[25];
	double A[5][5]{
		{-3.8, 0, 5.3, 4.5, 0.5 },
		{0.2, -1.3, 0, -8.5, 3.5},
		{-1.1, 1.8, 5.1, -8.2, 0.32},
		{0, -0.3, 0, -1.28, 0.52},
		{-0.3, 0.5, 1.8, -7.3, 5.5}
	};
	while (j < 5)
	{
		for (i = 0; i < 5; i++)
		{
			summ += A[i][j];
		}
		X[o] = summ;
		o++;
		k++;
		summ = 0;
		j++;
	}
	for (o = 0; o < k; o++)
	{
		if (X[o] < min)
		{
			min = X[o];
		}
	}
	cout << endl;
	cout << "Massiv X: " << endl;
	cout << endl;
	for (o = 0; o < k; o++)
	{
		cout << setw(10) << X[o];
	}
	cout << endl;
	cout << endl;
	cout << "Minimum iz znach massiva X: " << min << endl;
}