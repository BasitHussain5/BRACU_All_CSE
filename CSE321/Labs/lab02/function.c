#include <stdio.h>
#include <string.h>


int isperfect(int n)
{
    int sum = 0;
    for (int i = 1; i <= n/2; i++)
    {
        if (n % i == 0)
        {
            sum += i;
        }
    }
    if (sum == n)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int l, u;
    printf("Inputs: \n");
    scanf("%d", &l);
    scanf("%d", &u);

    printf("outputs: \n");
    for (int i = l; i <= u; i++) {
        if (isperfect(i)) {
            printf("%d \n", i);
        }
    }
    return 0;
}
