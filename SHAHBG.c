#include<stdio.h>
#include<iostream>
main()
{
	int n,grp = 0,i;
	bool x[20000] = {false};
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		int y;
		scanf("%d",&y);
		if(!x[y-1] && !x[y+1])
			grp += 1;
		else if(x[y-1] && x[y+1])
			grp -= 1;
		x[y] = 1;
		printf("%d\n",grp);
	}
	printf("Justice\n");
	return 0;
}
	

