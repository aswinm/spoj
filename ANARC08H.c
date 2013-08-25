#include<stdio.h>
main()
{
        int n,k,j,r;
        while(1)
        {
                scanf("%d%d",&n,&k);
                if(n==0 && k==0)
                        break;
                r=0;
                j=2;
                while(j<=n)
                {
                        r=(r+k)%j;
                        j++;
                }
                printf("%d %d %d\n",n,k,r+1);
        }
        return 0;
}
