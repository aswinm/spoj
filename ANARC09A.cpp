#include<iostream>
using namespace std;
main()
{
	char s[4000];
	int i,x,y,n=1;
	while(1)
	{
		x = y = 0;
		cin>>s;
		if(s[0] == '-')
		{
			break;
		}
		for(i=0;s[i];i++)
		{
			if( s[i] == '{')
				x++;
			else
				x--;
			if(x<0)
			{
				x += 2;
				y++;
			}
		}
		cout<<n<<". "<<((x/2)+y)<<endl;
	}
	return 0;
}
