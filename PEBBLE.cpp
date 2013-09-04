#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

main()
{
	string x;
	int m = 1;
	while(getline(cin,x))
	{
		int i,no = 0,j;
		int sl = x.length();
		for(i=0;i<sl;i++)
		{
			if(x[i]=='1')
			{
				x[i] = '0';
				for(j=i+1;j<=sl;j++)
				{
					if(x[j]=='1')
						x[j]='0';
					else
						x[j] = '1';
				}
				no++;
			}
		}
		printf("Game #%d: %d\n",m,no);
		m++;
	}
	return 0;
}


					
