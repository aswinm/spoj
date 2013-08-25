#include<stdio.h>
main()
{
        int t,a,b,j,k,l=1,i=0,max1,max2;
        scanf("%d",&t);
        while(i<t)
        {
                l=1;
                scanf("%d%d",&j,&k);
                scanf("%d",&max1);
                while(l<j)
                {
                        scanf("%d",&a);
                        if(a>max1)
                                max1=a;
                        l++;
                }
                scanf("%d",&max2);
                l=1;
                while(l<k)
                {
                        scanf("%d",&b);
                        if(b>max2)
                                max2=b;
                        l++;
                }
                if(max1>=max2)
                        printf("Godzilla\n");
                else
                        printf("MechaGodzilla\n");
                i++;
        }
        return 0;
}


