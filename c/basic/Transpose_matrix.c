#include<stdio.h>
int main(void)
{
	int ar1[2][2];
	int ar2[2][2];
	int i,j;
	printf("Enter the integers for matrix for 2*2: ");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			scanf("%d",&ar1[i][j]);
		}
	}
	printf("Original matrix is:\n");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("\t%d",ar1[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	printf("transpose matrix is:");
for(j=0;j<2;j++)
	{
		printf("\n");
		for(i=0;i<2;i++)
		{
			printf("\t%d",ar1[i][j]);
		}
	}
	
}
