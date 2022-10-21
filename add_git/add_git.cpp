#include <iostream>
#include <math.h>
#include <ctime>
#include <string.h>

using namespace std;

int main(){
    system("git add .");
    time_t sec;
    sec = time (NULL);
    string dt = asctime(localtime(&sec));
    string s = "git commit -m ";
    string d{'"'};
    string k = "upd: ";
    string command = s + d + k + dt + d;
    system(command.c_str());
    system("git push origin main");
    return 0;
}