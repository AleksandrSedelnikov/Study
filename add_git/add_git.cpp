#include <iostream>
#include <math.h>
#include <ctime>
#include <string.h>

using namespace std;

int main(){
    system("git add .");
    string var;
    cin >> var;
    cout << var;
    if (var == "other") {
        cout << "other";
        string commit;
        cin >> commit;
        string s = "git commit -m ";
        string d{'"'};
        string k = "manual upd: ";
        string command = s + d + k + commit + d;
        system(command.c_str());
    }
    else {
        cout << "auto";
        time_t sec;
        sec = time (NULL);
        string dt = asctime(localtime(&sec));
        string s = "git commit -m ";
        string d{'"'};
        string k = "auto upd: ";
        string command = s + d + k + dt + d;
        system(command.c_str());
    }
    system("git push origin main");
    return 0;
}