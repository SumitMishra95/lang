# include<stdio.h>

unsigned long int fact(int);
int main(void)
{
	unsigned int n;
	unsigned long int ans;
	printf("Enter a positive integer: ");
	scanf("%u",&n);
	ans = fact(n);
	printf("%u! = %ul\n",n,ans);
	return 0;
}
unsigned long int fact(int n)
{
	if(n==0 || n==1)
	return 1;
	else
	return n*fact(n-1);
}
