#include <stdio.h>
#include <math.h>

int add(int a, int b)
    {
    return a + b;
    }

int sub(int a, int b)
    {
    return a - b;
    }

int mul(int a, int b)
    {
    return a * b;
    }

int main()
{
    int num1, num2;
    char opera;

    printf("Enter the first Number: ");
    scanf("%d", &num1);

    printf("Enter the second Number: ");
    scanf("%d", &num2);

    printf("Enter the operators (+, -, *): ");
    scanf(" %c", &opera);

    if (opera == '-')
    {
        if (num1 > num2){
            printf("%d\n", sub(num1, num2));
        }

    }

    else if (opera == '+')
    {
        if (num1 < num2){
            printf("%d\n", add(num1, num2));
        }

    }

     else if (opera == '*')
    {
        if (num1 == num2){
            printf("%d\n", mul(num1, num2));
        }

    }

    else{
        printf("Invalid!");
    }
    return 0;

}
