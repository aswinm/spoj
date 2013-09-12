#include<stdio.h>
int func(int n,int k)
{
	if(n==1)
		return 1;
	return (func(n-1,k+1)+k-1)%n+1;
}
main()
{
	int t;
	scanf("%d",&t);

	while(t--)
	{
		long long int n,i=2,r=0,k=1;
		
		scanf("%lld",&n);
		printf("%d\n",func(n,1));
	}
	return 0;
}
