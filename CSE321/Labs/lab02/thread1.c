#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void* creat(void *arg)
{
    int f = *(int*)arg;
    printf("thread-%d running\n", f+1);
    printf("thread-%d closed\n", f+1);
}

int main()
{
    pthread_t thread[5];
    int i;
    for(i=0; i<5; i++)
    {
        int *t = malloc(sizeof(int));
        *t = i;
        pthread_create(&thread[i], NULL, &creat, t);
        sleep(2);
    }
    for(i=0; i<5; i++)
    {
        pthread_join(thread[i], NULL);
    }
    return 0;
}
