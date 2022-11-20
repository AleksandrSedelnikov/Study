#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <time.h>
#include <iomanip>
#include <locale>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main()
{
	setlocale(LC_ALL, "ru");
	int mass[100][100], rows, cols, i, j, n = 0;
	int od = 1;
	scanf("%d %d", &rows, &cols);
	for (i = 0; i < cols; ++i)
	{
		if (i % 2)
		{
			for (j = rows - 1; 0 <= j; --j)
			{
				mass[i][j] = n;
				++n;
			}
		}
		else
		{
			for (j = 0; j < rows; ++j)
			{
				mass[i][j] = n;
				++n;
			}
		}
	}
	for (i = 0; i < rows; ++i)
	{
		printf("\n");
		for (j = 0; j < cols; ++j)
		{
			printf("%4d", mass[i][j]);
		}
	}
	return 0;
}