#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n,i,k;
		char s[1001];
		std::cin>>s;
		n = strlen(s);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&k);
			printf("%c",s[k-1]);
		}
		printf("\n");
	}
	return 0;
}

		
