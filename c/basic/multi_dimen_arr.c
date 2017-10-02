#include<stdio.h>
int main(void)
{

	int i,j,sum=0;
	for(i=0;i<3;i++)
	{
		for(j=0;j<5;j++)
		{
			sum=sum+1;
			printf("\t%d",sum);
		}
		printf("\n");
	}
	return 0;
}
