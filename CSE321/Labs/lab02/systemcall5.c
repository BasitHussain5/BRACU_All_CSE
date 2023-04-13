#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    int pid;
    int grandchild;

    pid = fork();
    if (pid == 0)
    {
        printf("2. Child process ID: %d\n", getpid());
        grandchild = fork();
        if (grandchild == 0)
        {
            printf("3. Child process ID: %d\n", getpid());
        }
        else
        {
            grandchild = fork();
            if (grandchild == 0)
            {
                printf("4. Child process ID: %d\n", getpid());
            }
        else
        {
            grandchild = fork();
            if (grandchild == 0)
            {
                printf("5. Child process ID: %d\n", getpid());
            }
    }}}
    else if (pid > 0)
    {
        printf("1. Parent process ID: %d\n", getpid());
    }

}
