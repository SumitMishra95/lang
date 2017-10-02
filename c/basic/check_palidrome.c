#include<stdio.h>
int main(void)
{
	int n,num,r;
	int reverse=0;
	printf("Enter a number: ");
	scanf("%d",&n);
	num=n;
	while(num!=0)
	{
		r=num%10;
		reverse=reverse*10+r;
		num=num/10;
	}
	if(reverse==n)
	printf("%d is a palidrome number",n);
	else
	printf("%d is not a palidrome number",n);
	
	return 0;
}
