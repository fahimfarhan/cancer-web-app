#include <bits/stdc++.h>

using namespace std;

int main()
{
    bool b = false;
    try{
        system("google-chrome 127.0.0.1:8000/home/");
        exit(0);
        b = true;
    }catch(exception& x){
        cout<<x.what()<<endl;
    }
    try{
        if(!b)system("firefox 127.0.0.1:8000/home/");
        b = true;
        exit(0);
    }catch(exception& x){
        cout<<x.what()<<endl;
    }
    
    return 0;
}
