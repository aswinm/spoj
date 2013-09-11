#include<stdio.h>
main()
{
	long long int result = 0,n,x,i;
	scanf("%lld",&n);
	for(i = 0;i<n;i++)
	{
		scanf("%lld",&x);
		result = result ^ x;
	}
	printf("%lld\n",result);
	return 0;
}
