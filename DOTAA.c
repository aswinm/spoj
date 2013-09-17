#include<stdio.h>
main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n,m,d,count = 0,i,j;
		scanf("%d%d%d",&n,&m,&d);
		for(i=0;i<n;i++)
		{
			scanf("%d",&j);
			count += (j-1)/d;
		}
		if(count>=m)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}

