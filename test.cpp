#include <iostream>
#include <math.h>
#include <ctime>
#include <string.h>
using namespace std;

int main(){
    system("git add .");
    time_t now = time(0);
    char* dt = ctime(&now);
    char s[] = "git commit -m ";
    char d[1] = {'"'};
    char k[] = "upd:";
    char* cmd = strcat((strcat(s,d)),k);
    cout<<cmd<<endl;
    cout<<"okey"<<endl;
    //system(cmd.c_str());
    //system("git push origin main");
    return 0;
}