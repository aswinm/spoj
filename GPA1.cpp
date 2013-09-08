#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
int get_att(double a)
{
	if(a<51.0)
		return 5;
       	if(a<61.0)
		return 4;
	if(a<71.0)
		return 3;
	if(a<81.0)
		return 2;	
	if(a<91.0)
		return 1;
	else
		return 0;
}
int get_gp(double a)
{
	if(a>=91.0f)
		return 10;
       	if(a>=81.0f)
		return 9;
	if(a>=71.0f)
		return 8;
	if(a>=61.0f)
		return 7;	
	if(a>=51.0f)
		return 6;
	if(a==50.0f)
		return 5;
	else 
		return 0;
}
main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int credit[6];
		int i;
		double gp = 0.0f,smcr = 0.0f;
		char a[10],b[10],c[10],d[10];
		int flag = 0;
		for(i=0;i<6;i++)
		{
			scanf("%d",&credit[i]);
			smcr += credit[i];
		}
		for(i=0;i<6;i++)
		{
			double internals[3],fi,att,in;
			cin>>a>>b>>c>>d;
			if(strcmp(a,"ab")==0)
				internals[0]=0.0f;
			else 
				internals[0]=atof(a);
			if(strcmp(b,"ab")==0)
				internals[1]=0.0f;
			else 
				internals[1]=atof(b);
			if(strcmp(c,"ab")==0)
				internals[2]=0.0f;
			else 
				internals[2]=atof(c);
			if(strcmp(d,"ab")==0)
				fi = 0.0f;
			else
				fi  = atof(d);	
			cin>>a;
			att = atof(a);
			sort(internals,internals+3);
			in=(internals[2]+internals[1])*45.0/40.0;
			att=get_att(att);
			fi/=2.0;
			fi=fi+att+in;
			fi = get_gp(fi);
			gp += fi*credit[i];
			if(fi == 0.0f)
				flag = 1;
		}
		gp/=smcr;
		if(flag)
			printf("FAILED, %.2f\n",gp);
		else
			printf("PASSED, %.2f\n",gp);
	}
	return 0;
}


				

