#include<stdio.h>
void func(unsigned long int x)
{
	int sum = 0;
	while(x)
	{
		sum += x%2;
		x/=2;
	}
	printf("%d\n",sum);
}
main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		
		unsigned long int n;
		scanf("%ld",&n);
		func(n);
	}
	return 0;
}
	
	
