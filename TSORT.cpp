#include<iostream>
#include<algorithm>
main()
{
	long int n,i;
	std::cin>>n;
	long int x[n];
	for(i=0;i<n;i++)
		std::cin>>x[i];
	std::sort(x,x+n);
	for(i=0;i<n;i++)
		std::cout<<x[i]<<"\n";
	return 0;
}
