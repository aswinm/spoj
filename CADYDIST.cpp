#include<iostream>
#include<stdio.h>
#include<algorithm>
main()
{
	long long int a[100000],b[100000],sum;
	int n,i,j;
	while(1)
	{
		scanf("%d",&n);
		if (n == 0)
			break;
		for(i=0; i<n;i++)
			scanf("%lld",&a[i]);
		for(i=0; i<n;i++)
			scanf("%lld",&b[i]);
		std::sort(a,a+n);
		std::sort(b,b+n);
		i = n-1;
		sum = 0;
		for(j=0;j<n;j++)
		{
			sum += a[i]*b[j];
			i--;
		}
		printf("%lld\n",sum);
	}
	return 0;
}

	



