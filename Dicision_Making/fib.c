#include<stdio.h>
int main()
{
	int f0=0,f1=1,res,num;
	printf("Enter number\n");
	scanf("%d",&num);
	printf("Fibonacci series: ");
	printf("%d%d",f0,f1);
	for(int i=0;i<num;i++)
	{
		res=f0+f1;
		printf("%d",res);
		f0=f1;
		f1=res;
	}
}
