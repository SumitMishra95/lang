#include<stdio.h>
int main(void)
{
	int a,b;
	printf("Enter any two number: ");
	scanf("%d%d",&a,&b);
	printf("%d is greater then %d",((a>b)?a:b),((a<b)?a:b));
	return 0;
}
