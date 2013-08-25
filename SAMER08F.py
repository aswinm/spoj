#include<iostream>
using namespace std;
main()
{
        int a,i=0;
        unsigned long long int b;
        while(i==0)
        {
                cin>>a;
                if(a!=0)
                {
                        b=a*(a+1)*(2*a+1)/6;
                        cout<<b<<"\n";
                }
                else
                        i=1;
        }
        return 0;
}



