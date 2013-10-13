#include<stdio.h>
int min(int a,int b)
{
	return a<b?a:b;
}
main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n,s[21][3],mi,i,j;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			for(j=0;j<3;j++)
				scanf("%d",&s[i][j]);
		for(i=1;i<n;i++)
		{
			for(j=0;j<3;j++)
			{
				if(!j)
				s[i][j] += min(s[i-1][1],s[i-1][2]);	
				else if(j==1)
				s[i][j] += min(s[i-1][0],s[i-1][2]);
				else
				s[i][j] += min(s[i-1][0],s[i-1][1]);
			}
		}
		mi = 30000;
		for(i=0;i<3;i++)
			if(s[n-1][i]<mi)
				mi = s[n-1][i];
		printf("%d\n",mi);
	}
	return 0;
}
		
		

					

	
