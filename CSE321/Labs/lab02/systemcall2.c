#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>


int main()
{
    int pid;
    int grandchild;
    pid =fork();
    if (pid < 0)
    {
        printf("Invalid");
    }
    else if (pid == 0)
    {
        grandchild = fork();
        if (grandchild < 0)
        {
            printf("Invalid");
        }
        else if (grandchild == 0)
        {
            printf("I am grandchild\n");
        }
        else if (grandchild > 0)
        {
            wait(NULL);
            printf("I am child\n");
        }

    }
    else if (pid > 0)
    {
        wait(NULL);
        printf("I am parent\n");
    }
}
