#include <stdio.h>
#include <string.h>


int main(void)
{
    int t;
    
    scanf("%d", &t);
    while (t--)
    {
	int n,x,temp; 
    	long long int index; 
    	
    
        scanf("%d %lld", &n, &index);
        
        long long int val[n];
        
        
        temp = n;
        while (temp--) 
	{
		 val[temp] = index; 
		 index = (index+1)/2; 
	} 
        
        x = 1;
        while (temp++ < n-1) 
        {
            if (val[temp] == val[temp-1]*2) x = !x;
        }
        
        if(x)
	{
		printf("Male\n");
	}
	else
	{
		printf("Female\n");
	} 
    }
    return 0;
}
