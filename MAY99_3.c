#include<stdio.h>
long long unsigned int gcd(int a, int b)
{
	if (b>a)
		return gcd(b,a);
	if(b==0)
		return a;
	return gcd(b,a%b);
}
main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		long long unsigned int x,y,z;
		scanf("%lld%lld%lld",&x,&y,&z);
		if(x<y)
			x ^= y ^= x ^= y; 
		if(z>x)
		{
			printf("NO\n");
			continue;
		}
		if(z%gcd(x,y)==0)
		{
			printf("YES\n");
			continue;
		}
		printf("NO\n");
	}
	return 0;
}
