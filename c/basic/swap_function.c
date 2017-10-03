#include <stdio.h>
int swap(int*, int*);

int main(void)
{
    int num1,num2;
    printf("Enter any two integers: ");
    scanf("%d%d",&num1,&num2);
    printf("Before swapping\nNumber1 = %d\nNumber2 = %d\n\n",num1,num2);
    swap( &num1, &num2);
	printf("After swapping\nNumber1 = %d\nNumber2 = %d\n\n",num1,num2);
    return 0;
}

int swap(int*n1, int*n2)
{
     int temp = *n1;
    *n1 = *n2;
    *n2 = temp;
}
