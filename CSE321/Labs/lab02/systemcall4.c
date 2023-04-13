#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>


int main(int argc, char *argv[])
{
    if(argc<2)
    {
        printf("Pass an Array!\n");
        return -1;
    }

    pid_t pid = fork();
    if(pid==0)
    {
        execv("sort", argv);
    }
    else
    {
        wait(NULL);
        execv("oddEven", argv);
    }
    return 0;
}
