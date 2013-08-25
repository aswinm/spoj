#include<stdio.h>
main()
{
        long long unsigned int n;
        int t,i;
        scanf("%d",&t);
        for(i=0;i<t;i++)
        {
                scanf("%lld",&n);
                n=(n*(n+1)/6);
                printf("%lld\n",n);
        }
        return 0;
}


