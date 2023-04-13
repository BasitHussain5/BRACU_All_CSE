#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    struct process
    {
     int n, wt, at, bt,tat,ct;
    };

    int n;
    printf("Enter the total number of processes:");
    scanf("%d", &n);
    struct process array[n*2];
    int i=0,ct,temp[n*2], time=0, rt=0, sst, twt=0,ttat=0,tq;
    printf("Enter Time Quantam: ");
    scanf("%d", &tq);
    printf("Enter burst time for all process:\n");
    for(int i = 0; i<n; i++)
    {
        array[i].at = 0;
        scanf("%d",&array[i].bt);
        temp[i] = array[i].bt;
    }

    while(rt<n)
    {
        i = i%n;
        if (temp[i]==0)
        {
            i++;
            continue;
        }
        else if (temp[i]-tq>0)
        {
            temp[i]-=tq;
            time+=tq;
        }
        else
        {
            time += temp[i];
            array[i].ct=time;
            temp[i]=0;
            rt++;
        }
        i++;
    }
   printf("Process | Burst Time | Completion Time | Turnaround Time | Waiting Time\n");
printf("--------+-------------+-----------------+------------------+-------------\n");
    for(i=0;i<n;i++)
    {
        ct = array[i].ct;
        ttat = ct-array[i].at;
        twt=ttat-array[i].bt;
   printf("  p%-4d |     %-8d |         %-8d |          %-8d |        %-8d\n", i+1, array[i].bt, ct, ttat, twt);
    }
    return 0;
}
