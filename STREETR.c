#include<stdio.h>
int gcd(int x, int y)
{
	while(x!=y)
	{
		if(x>y)
			return gcd(x-y,y);
		return gcd(x,y-x);
	}
	return x;
}
main()
{
	int n,n1,n2,g,s=0,i;
	scanf("%d",&n);
	int x[n];
	scanf("%d",&n1);
	for(i=0;i<n-1;i++)
	{
		scanf("%d",&n2);
		x[i] = n2-n1;
		n1 = n2;
	}
	g = gcd(x[0],x[1]);
	for(i=2;i<n-1;i++)
		g = gcd(g,x[i]);
	for(i=0;i<n-1;i++)
		s += (x[i]/g)-1;
	printf("%d\n",s);
	return 0;
}

