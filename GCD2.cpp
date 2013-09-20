#include<iostream>
#include<stdio.h>
using namespace std;

int gcd(int n1,int n2)
{
	while(n2)
	{
		n2^=n1^=n2^=n1%=n2;
	}
	return n1;
}	

int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n1,i,n2 = 0;
		char s[300];
		scanf("%d%s",&n1,s);
		for(i=0;s[i]!='\0';i++)
			n2 = (n2*10+s[i]-'0')%n1;
		printf("%d\n",gcd(n1,n2));
	}
	return 0;
}

			
	
