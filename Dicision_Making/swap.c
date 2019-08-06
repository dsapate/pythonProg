#include<stdio.h>
int main()
{
	int a=10,b=20,temp;
	temp=a;
	a=b;
	b=temp;
	printf("values of a=%d and b=%d after swaping is : ",a,b);
	return 0;
}
