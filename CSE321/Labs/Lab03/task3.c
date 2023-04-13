#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    struct process
    {
     int n, wt, at, bt,tat,pt,ct;
    };

    int n;
    printf("Enter the total number of processes:");
    scanf("%d", &n);
    struct process array[n*2];
    int temp[n*2], time, rt=0, sst, twt=0,ttat=0;
    rt =n;
    printf("Enter arival time, burst time, and priority for all process:");
    for(int i = 0; i<n; i++)
    {
        scanf("%d %d %d", &array[i].at, &array[i].bt, &array[i].pt);
        temp[i] = array[i].bt;
    }
    array[n*2-1].pt = 9999;
    printf("\nProcess | Arrival Time | Burst Time | Priority | Completion Time | Turnaround Time | Waiting Time\n");
    for (time=0; rt!=0; time++)
    {
        sst = n*2-1;
        for (int i =0; i<n; i++)
        {
            if(array[sst].pt>array[i].pt && array[i].at<=time && array[i].bt>0)
            {
                sst =i;
            }
        }
        array[sst].bt--;
        if(array[sst].bt==0)
        {
            rt--;
            array[sst].ct=time+1;
            printf("P%d      | %d            | %d          | %d       | %d               | %d               | %d\n", sst+1, array[sst].at, temp[sst], array[sst].pt, array[sst].ct, array[sst].ct - array[sst].at, array[sst].ct - array[sst].at - temp[sst]);
            twt+=array[sst].ct-array[sst].at-temp[sst];
            ttat+=array[sst].ct-array[sst].at;

        }
        }
    return 0;
}

