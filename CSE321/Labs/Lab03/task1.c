#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n;
    printf("Enter the total number of processes: ");
    scanf("%d", &n);
    int arival[10], burst[10], temp[10], ct, i, s, wt=0, tat=0, rt=0, time;
    rt = n;
    printf("Enter arival and burst time for all processes: \n");

    for (i =0; i<n; i++)
    {
        scanf("%d %d", &arival[i], &burst[i]);
        temp[i] = burst[i];
    }
    burst[9] = 999;
    printf("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time\n");
    for (time=0; rt!=0; time++)
    {
        s = 9;
        for(i = 0; i<n; i++)
        {
            if (temp[i]>0 && arival[i]<=time && temp[i]<temp[s])
                s = i;
        }
        temp[s]-- ;
        if(temp[s]==0)
        {
            rt--;
            ct = time+1;
            printf("%d\t%d\t\t%d\t\t%d\t\t%d\t\t\t%d\n", s + 1, arival[s], burst[s], ct, ct - arival[s], ct - arival[s] - burst[s]);
            wt += ct-arival[s]-burst[s];
            tat += ct-arival[s];
                    }
    }

}
