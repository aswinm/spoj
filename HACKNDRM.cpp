#include<stdio.h>
#include<iostream>
#include<algorithm>
main()
{
	unsigned int n,k,i,count=0,j;
	scanf("%d%d",&n,&k);
	unsigned int x[n];
	for(i=0;i<n;i++)
		scanf("%d",&x[i]);
	std::sort(x,x+n);
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(x[j]-x[i]==k)
				count++;
			else if(x[j]-x[i]>k)
				break;
		}
	}
	printf("%d",count);
	return 0;
}
