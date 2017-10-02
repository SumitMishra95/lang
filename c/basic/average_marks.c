#include<stdio.h>
int main(void)
{
	int i,n,m;
	int tm=0;
	printf("Enter the number of subjects: ");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		printf("Enter the marks of each subject of a particular student %d : ",i);
		scanf("%d",&m);
		tm=tm+m;
	}
	printf("Average marks of students is %.2f",(float)tm/(float)n);
	return 0;
}
