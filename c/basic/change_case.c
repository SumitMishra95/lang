#include<stdio.h>
int main(void)
{
	char c;
	int i;
	printf("Enter any alphabet: ");
	scanf("%c",&c);
	i=c;
	if(i>=65 && i<=90)
	{
		printf("You entered a %c. And its lower case is %c\n",c,c+32);
	}
	else if(i>=97 && i<=122)
	{
		printf("You entered a %c. And its upper case is %c\n",c,c-32);
	}
	else
	{
		printf("you have entered a wrong input.");
	}
	return 0;
}
