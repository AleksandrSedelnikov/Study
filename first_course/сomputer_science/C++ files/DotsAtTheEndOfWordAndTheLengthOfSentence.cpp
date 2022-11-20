#include <iostream>
#include <string>
#include <iomanip>
#include <locale>

using namespace std;

int main() {

	setlocale(0, "rus");
	string s,s1;
	cout << "Введите предложение: "; getline(cin, s); s += ' ';
	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] != ' ')
		{
			s1 += s[i];
		}
		else
		{
			s1 += "... ";
		}
	}
	cout << s1;
	int dlina = s1.length();
	cout << endl;
	cout << "Длина получившегося предложения - " << dlina << endl;
}