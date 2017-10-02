//Read 10 integers from keyboard and store them in an array. For each integer in the array display a line with that many "*" characters.

#include<stdio.h>
int main(void)
{
	int arr[10];
	int i,j;
	printf("Enter any ten integers: ");
	for(i=0;i<10;i++)
	scanf("%d",&arr[i]);
	for(i=0;i<10;i++)
	{
		for(j=0;j<arr[i];j++)
		{
			printf("*");
		}
		printf("   - %d\n",arr[i]);
	}
	return 0;
}
