#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
	int t,l=1;
	cin>>t;
	while(l<=t)
	{
		int n;
		cin>>n;
		long long int x[n],i;
		for(i=0;i<n;i++)
			cin>>x[i];
		long long int max = 0,dp[n];
		if(n)
		{
		dp[0] = x[0];
		for(i=1;i<n;i++)
		{
			dp[i] = max+x[i];
			if(max<dp[i-1])
				max = dp[i-1];
		}
		if(max<dp[i-1])
			max = dp[i-1];
		}
		cout<<"Case "<<l<<": "<<max<<endl;
		l++;
	}
	return 0;
}



