#include<stdio.h>
#include<math.h>
#include<iostream>
using namespace std;
main()
{
	long long unsigned int t;
	scanf("%lld",&t);
	while(t--)
	{
		int i,c =1 ;
		long long unsigned int x = 1;
		char s[31];
		cin>>s;
		for(i=0;s[i+1];i++)
		{
			if(s[i]==s[i+1])
				c += 1;
			else
			{
				x *= pow(2,c-1);
				c = 1;
			}
		}
		x *= pow(2,c-1);
		printf("%lld\n",x);
	}
	return 0;
}


