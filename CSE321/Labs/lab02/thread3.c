#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <pthread.h>

void *user(){
int *s = (int*)malloc(sizeof(int));
int j = 0;
char user1[15000];
scanf("%s", user1);
int total = 0;
for (j = 0; j<strlen(user1); j++){
total += user1[j];}
*s = total;
return s;
}

int main(){
pthread_t thread[3];

    int i;
    int *n[3]; 
    int f[3];
    
    for(i = 0; i < 3; i++){
    pthread_create(&thread[i], NULL, &user, NULL);
    }
    for(i = 0; i < 3; i++){
    pthread_join(thread[i], (void*)&n[i]);
    f[i] = *n[i];
   }
   if (f[0] == f[1] && f[1]==f[2] && f[0]==f[2]){
   printf("Youreka\n");
   }else if (f[0] == f[1] || f[1]==f[2] || f[0]==f[2]){
   printf("Miracle\n");}
   else {
   printf("Hasta la vista\n");}
   return 0;
   }
   
