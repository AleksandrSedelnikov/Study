// Program.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <string>
#include <cstdlib>
#include <locale>

using namespace std;


struct data {
    string log;
    int pass;
};

int basa(int password, string login,int flag)
{
    int i;
    struct data user[2];
    user[0].log = "admin";
    user[0].pass = 12345;
    user[1].log = "demo";
    user[1].pass = 0000;
    for (i = 0; i < 2; i++)
    {
        if (user[i].log == login && user[i].pass == password)
        {
            flag = 1;
            break;
        }
        else
        {
            flag = 0;
        }
    }
    return flag;

}

int menu()
{
    int flag = 0;
    cout << "Здравствуйте, вы в системе редактирования, для начала работы, авторизуйтесь!";
    cout << endl << endl;
    int password;
    string login;
    cout << "Введите логин: "; cin >> login;
    cout << endl;
    cout << "Введите пароль: "; cin >> password;
    flag = basa(password, login,flag);
    return flag;

}

void avtor(int password,string login, int flag)
{
    if (flag == 1)
    {
        cout << "Вы успешно авторизовались в системе, как авторизованный пользователь, ваши данные:" << endl;
        cout << "Логин: " << login << "  " << "Пароль: " << password << endl;
    }
}


int main()
{
    int flag = 0;
    setlocale(LC_ALL, "Russian");
    flag = menu();
    //avtor(flag);
}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
