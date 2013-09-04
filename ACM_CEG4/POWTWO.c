#include<stdio.h>
main()
{
	int t,n,s;
	scanf("%d",&t);
	while(t--)
	{
		s = 0;
		scanf("%d",&n);
		while(n)
		{
			s += n%2;
			n /= 2;
		}
		if (s <=1)
			printf("Yes\n");
		else
			printf("No\n");
	}
	return 0;
}
