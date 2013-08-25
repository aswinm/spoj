#include<stdio.h>
int main()
{
        int i,j,t,temp;
        scanf("%d",&t);
        i=1;
        temp=0;
        for(i=1;i<=t;i++)
        {
        temp=temp+1;
        if((2*i)<=t&&(2*i)!=i+1)
        {
        temp=temp+1;
        }
        for(j=i;j<=t;j++){
        if(i*j<=t&&i*j!=2*j&&i*j!=j)
        {
        temp=temp+1;
        }
        }
        }
        printf("%d",temp);
        return 0;
}

