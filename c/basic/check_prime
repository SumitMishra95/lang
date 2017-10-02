#include<stdio.h>
void prime(int);
int main(void)
{
	int n;
	printf("Enter any number to check prime: ");
	scanf("%d",&n);
	prime(n);
	return 0;
}
void prime(int n)
{
	int i,check;
	for(i=2;i<n;i++)
	{
		if(n%i==0)
		{
			printf("%d is a composite number.",n);
			break;
		}
	}
	if(i==n)
	printf("%d is a prime number.",n);
}
