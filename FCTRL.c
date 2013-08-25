#include<stdio.h>
main()
{
        int t,i,count;
        unsigned long long int x,n;
        scanf("%d",&t);
        for(i=0;i<t;i++)
        {
                scanf("%lld",&n);;
                x=5;
                count=0;
                while(n>=x)
                {
                        count+=(n/x);
                        x*=5;
                }
                printf("%d\n",count);
        }
        return 0;
}



