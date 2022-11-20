#include <iostream>
#include <iomanip>
#include <time.h>
#include <cstdlib>

using namespace std;

int main()
{
    system("chcp 1251");
    srand(time(NULL));
    int n, m, i, j, cnt = 0, nmin;
    int buf_sum, buf_mass;
    cout << "Введите количество строк: "; 
    cin >> n;
    cout << "Введите количество столбцов: "; 
    cin >> m;
    int** mass = new int *[n];
    for (i = 0; i < n; i++)
    {
        mass[i] = new int[m];
    }
    int* sum = new int[n];

    for (i = 0; i < n; i++)
    {
        sum[i] = 0;
        for (j = 0; j < m; j++)
        {
            mass[i][j] = rand()%201-100;
            if (mass[i][j] > 0 && (mass[i][j] % 2) == 0)
            {
                sum[i] += mass[i][j];
            }
        }
    }
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
            cout << setw(4) << mass[i][j];
        cout << " || " << sum[i] << endl;
    }
    
    for (i = 0; i < n - 1; i++)
    {
        nmin = i;
        for (j = i + 1; j < n; j++)
            if (sum[j] < sum[nmin])
                nmin = j;
        buf_sum = sum[i];
        sum[i] = sum[nmin];
        sum[nmin] = buf_sum;
        for (j = 0; j < m; j++)
        {
            buf_mass = mass[i][j];
            mass[i][j] = mass[nmin][j];
            mass[nmin][j] = buf_mass;
        }
    }
    cout << endl << endl;
    cout << "Получившаяся матрица:";
    cout << endl << endl;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
            cout << setw(4) << mass[i][j];
        cout << " || " << sum[i] << endl;
    }
    return 0;
}