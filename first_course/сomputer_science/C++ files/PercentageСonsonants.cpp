#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>

using namespace std;

int main()
{
    system("chcp 1251");
    system("cls");
    string s,s1;
    int i, count = 0,j,k = 0,o = 0,minpos = 0,temp = 0,nach = 0, kon = 0;
    double sogl = 0, glas = 0;
    cout << "Введите предложение: " << endl; // ну тут ты вводишь предложение
    getline(cin, s);
    s += ' ';
    for (i = 0; i < s.length(); i++) // а с 19 по 89 происходит магия
    {
        if (s[i] == ' ')
        {
            count++;
        }
    }
    double *mass = new double [count + 1];
    int* mass1 = new int [(count + 1) * 2];
    for (i = 0; i < s.length(); i++)
    {
        if (s[i] != ' ' && s[i] != 'A' && s[i] != 'E' && s[i] != 'I' && s[i] != 'O' && s[i] != 'U' && s[i] != 'Y' && s[i] != 'a' && s[i] != 'e' && s[i] != 'i' && s[i] != 'o' && s[i] != 'u' && s[i] != 'y')
        {
            sogl++;
        }
        else if (s[i] == ' ')
        {
            for (j = k; j < count; j++)
            {
                mass[j] = (((sogl + glas) / 100) * sogl) * 100;
            }
            mass1[o] = i - (sogl + glas); // предупреждение? - так надо
            mass1[o + 1] = i - 1;
            o += 2;
            k++;
            sogl = 0;
            glas = 0;
        }
        else
        {
            glas++;
        }
    }
    for (i = 0; i < count; i++)
    {
        cout << mass[i] << "% ";
    }
    cout << endl;
    for (i = 0; i < count; i++)
    {
        minpos = i;
        for (j = i + 1; j < count; j++)
        {
            if (mass[minpos] > mass[j])
            {
                minpos = j;
            }
        }
        temp = mass[minpos];
        mass[minpos] = mass[i];
        mass[i] = temp;

        temp = mass1[minpos * 2];
        mass1[minpos * 2] = mass1[i * 2];
        mass1[i*2] = temp;

        temp = mass1[minpos * 2 + 1];
        mass1[minpos * 2 + 1] = mass1[i * 2 + 1];
        mass1[i*2 + 1] = temp;
        
    }
    for (i = 0; i < count * 2; i += 2)
    {
        nach = mass1[i];
        kon = mass1[i + 1];
        for (nach; nach <= kon; nach++)
        {
            s1 += s[nach];
        }
        s1 += ' ';
    }
    cout << endl;
    cout << "Измеренная строка: " << endl; // ниже вывод измененный строки в коде с 19 по 89
    cout << s1 << endl;
    for (i = 0; i < count; i++)
    {
        cout << mass[i] << "% ";
    }
    return 0;
}