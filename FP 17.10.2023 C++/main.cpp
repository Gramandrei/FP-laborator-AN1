#include <iostream>

using namespace std;

int main()
{
    int n, d=2,ok;
    cin>>n;

    while(n>1)
    {
        ok=0;
        while(n%d==d)
        {
            ok=1;
            n=n/d;
        }
        if(ok==1)
        {
            cout<<d<<' ';
        }
        if(d==2)
        {
            d=3;
        }
        else
        {
            d=d+2;
        }
        if(d*d>n)
        {
            d=n;
        }
    }


    return 0;
}
