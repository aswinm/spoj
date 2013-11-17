#include<stdio.h>
#define MAX 1000000007
#define min(a,b) (a)>(b)?(b):(a)
int main()
{
	int i,j,k,a[1001]={0},b[1001]={0};
	for(i=0;i<1001;i++)
		b[i]=35;
	a[0]=1;b[0]=0;
	i=1;
	for(i=1;i*i<1001;i++)
		for(j=0;j<1001;j++)
			if(j+i*i<1001)
				if(a[j]==1)
					a[j+i*i]=1,b[j+i*i]=min(b[j+i*i],b[j]+1);
	int n,t;
	scanf("%d",&t);
	while(t--)	
	{
		scanf("%d",&n);
		printf("%d\n",b[n]);
	}
	return 0;
}

