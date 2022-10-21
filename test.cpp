#include <iostream>
#include <math.h>
#include <ctime>

using namespace std;

int main(){
    time_t now = time(0);
    char* dt = ctime(&now);
    system("git add .");
    system("git commit -m 'upd:current_time'");
    system("git push origin main");
    return 0;
}