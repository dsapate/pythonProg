#include<stdio.h>
int main()
{
	int i,j;
	int r,c;
	printf("Enter rows and columns :");
	scanf("%d %d",&c,&r);
	for(i=1;i<=r;i++)
	{
		for(j=c;j>=i;j--)
		{
			printf("*");
		}
		printf("\n ");
	}
}
