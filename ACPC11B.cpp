#include<stdio.h>
#include<iostream>
#include<algorithm>
int abs(int a)
{
	if (a<0)
		a = -a;
	return a;
}
main()
{
	int n1,n2,i,j,k,t;
	int min;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n1);
		int a[n1];
		for(i=0;i<n1;i++)
			scanf("%d",&a[i]);
		scanf("%d",&n2);
		int b[n2];
		for(i=0;i<n2;i++)
			scanf("%d",&b[i]);
		std::sort(a,a+n1);
		std::sort(b,b+n1);
		min = 1000000;
		for(i=0;i<n1;i++)
			for(j=0;j<n1;j++)
				if(abs(a[i]-b[j])<min)
					
					min = abs(a[i]-b[j]);
		printf ("%d\n",min);
	}
	return 0;
}
