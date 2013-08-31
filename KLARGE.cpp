#include<stdio.h>
#include<iostream>
#include<algorithm>
main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n,k,i;
		scanf("%d",&n);
		long long unsigned int x[n];
		for(i=0;i<n;i++)
			scanf("%lld",&x[i]);
		scanf("%d",&k);
		std::sort(x,x+n);
		printf("%lld\n",x[n-k]);
	}
	return 0;
}

