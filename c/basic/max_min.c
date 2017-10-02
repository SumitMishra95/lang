#include<stdio.h>
int main(void)
{
	int arr[10];
	int i,max,min;
	printf("Enter any ten integer: ");
	for(i=0;i<10;i++)
	{
		scanf("%d",&arr[i]);
	}
	max=arr[0];
	for(i=0;i<10;i++)
	{
		if(max<arr[i])
		max=arr[i];
	}
	min=arr[0];
	for(i=0;i<10;i++)
	{
		if(min>arr[i])
		min=arr[i];
	}
	printf("%d is greatest of all.\n%d smallest of all.",max,min);
	return 0;
}
