#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<map>
main()
{
	int n,i,j,t;
	std::string x;
	while(1)
	{
	int c[20000] = {0};
	scanf("%d%d",&n,&t);
	if(n == 0 && t == 0)
		break;
	std::map <std::string, int> mymap,it;
	for(i=0;i<n;i++)
	{
		std::cin>>x;
		if(mymap.find(x)!=mymap.end())
			mymap[x]++;
		else
			mymap[x]=0;

	}
	std::map<std::string,int>::iterator iter = mymap.begin();
	for(;iter!=mymap.end();++iter)
		c[iter->second]++;
	for(i=0;i<n;i++)
		printf("%d\n",c[i]);
	}
	return 0;
}
	


