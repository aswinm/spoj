#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		string s;
		int n,i;
		cin>>s>>n;
		n %= 26;
		for(i=0;i<s.length();i++)
		{
			if('a'<=s[i] && s[i]<='z')
			{
				int x;
				x = s[i]+n;
				
				if (122<x)
				{
					x -= 26;
				}
				s[i] = char(x);
			}
			else
			{
				int x;
			  x  =s[i] + n;
				if(90<x)
				{
					x -= 26;
				}
			s[i] = x;
			}
		}
		cout<<s<<endl;
	}
	return 0;
}

				
				








