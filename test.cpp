#include <iostream>
#include <math.h>
#include <ctime>
#include <string.h>
#include <stdio.h>

using namespace std;

int main(){
    system("git add .");
    //char d[] = ".";
    //time_t sec;//
    //sec = time(NULL);//
    //char* dt = asctime(localtime(&sec));//
    //const string time = strcat(dt,d);//
    //cout<<time<<endl;//
    //char s[] = "git commit -m 'upd: " + *dt;//
    //const string cmd = strcat(s,dt);//
    //cout<<cmd<<endl;// 
    system("git commit -m 'upd:testing.'");
    system("git push origin main");
    return 0;
}