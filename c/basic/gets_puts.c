#include<stdio.h>
int main(void)
{
	char name[30];
	char clg[40];
	printf("Enter your name: ");
	gets(name);
	printf("Enter your college name: ");
	gets(clg);
	printf("My name is ");
	puts(name);
	printf("And my college name is ");
	puts(clg);
	return 0;
}
