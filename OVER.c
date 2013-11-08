#include<stdio.h>
main()
{
	long long unsigned int x[51];
	int i,t;
	x[0] = 1;
	x[1] = 3;
	for(i=2;i<50;i++)
		x[i] = 2*x[i-1]+x[i-2];
	scanf("%d",&t);
	while(t--)
	{
		int n;
		scanf("%d",&n);
		printf("%lld\n",x[n]);
	}
	return 0;
}
