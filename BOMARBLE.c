#include<stdio.h>
main()
{
	while(1)
	{
		int x;
		scanf("%d",&x);
		if(x==0)
			break;
		x++;
		printf("%d\n",(3*x*x-x)/2);
	}
	return 0;
}





