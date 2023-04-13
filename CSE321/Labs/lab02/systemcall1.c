#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <pthread.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char *argv[]){
if (argc !=2){
printf("Please type\n");
exit(-1);}
    int tsk;
    tsk = open(argv[1], O_RDWR | O_CREAT, 0664);
    if (tsk == -1)
    {
        printf("File could not be created.\n");
        return -1;
    }
    printf("Enter strings to write to the file. Enter '-1' to stop.\n");
    while (1)
    {
        char input[400];
        scanf("%[^\n]%*c", input);
        if (strcmp(input, "-1") == 0)
        {
            break;
        }
        
        write(tsk, input, strlen(strcat(input, " ")));
        write(tsk, "\n", 1);
    }
    close(tsk);
    printf("Data written to the file successfully.\n");
    return 0;
}






   
