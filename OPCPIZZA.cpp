#include<stdio.h>
#include<algorithm>
#include<iostream>
main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n,p,i,j;
		scanf("%d%d",&n,&p);
		long int x[n],count = 0;
		
		for(i=0;i<n;i++)
		{
			scanf("%ld",&x[i]);
		}
		std::sort(x,x+n);
		for(i=0;i<n;i++)
		{
			j = std::lower_bound(x,x+n,p-x[i]) - x;
			if(j!=i && j!=n && p-x[j] == x[i])
				count++;

		}
		printf("%ld\n",count/2);
	}
	return 0;
}

