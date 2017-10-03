#include<stdio.h>
int main(void)
{
	int a,b;
	printf("Enter any two integers.\nEnter first integer: ");
	scanf("%d",&a);
	printf("Enter second integer: ");
	scanf("%d",&b);
	a=a+b;
	b=a-b;
	a=a-b;
	printf("\nAfter swapping\nFirst integer is %d.\nAnd second integer is %d",a,b);
	return 0;
}
