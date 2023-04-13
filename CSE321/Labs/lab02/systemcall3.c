
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/wait.h>

int main()
{
    int s[2];
    if (pipe(s) != 0)
    {
        printf("an error.\n");
        exit(1);
    }
    pid_t p_pid = getpid();
    int p_count = 0;


    write(s[1], &p_count, sizeof(int));
    pid_t a = fork();
    pid_t b = fork();
    pid_t c = fork();

    pid_t c_pid = getpid();
    if (c_pid != p_pid && c_pid % 2 != 0)
    {
        fork();
    }
    read(s[0], &p_count, sizeof(int));
    p_count += 1;
    write(s[1], &p_count, sizeof(int));
    close(s[1]);
    waitpid(a, NULL, 0);
    waitpid(b, NULL, 0);
    waitpid(c, NULL, 0);
    if (getpid() == p_pid){
        read(s[0], &p_count, sizeof(int));
        close(s[0]);
        printf("Total processes have been created considering the first parent process: %d\n", p_count);
    }

    return 0;
}

