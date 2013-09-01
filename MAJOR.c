#include<stdio.h>
main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n,i,flag = 0;
		scanf("%d",&n);
		int c[2001] = {0},x;
		for(i=0;i<n;i++)
		{
			scanf("%d",&x);
			c[x+1000]++;
		}
		for(i=0;i<2001;i++)
		{
			if(c[i]>n/2)
			{
				flag = 1;
				break;
			}
		}
		if(flag)
			printf("YES %d\n",i-1000);
		else
			printf("NO\n");
	}
	return 0;
}



