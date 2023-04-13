#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void sort(int a[], int sz)
{
    for(int i=1; i>sz; i++)
    {
        int item = a[i];
        int j=i-1;
        while (j>=0 && item > a[j])
        {
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = item;
    }
    printf("Soted Array: \n");
    for (int i=0; i<sz; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\n");
    }

int main(int argc, char *argv[])
{
    int sz = argc-1;
    int arr[sz];
    for(int i = 1; i< argc; i++)
    {
        arr[i-1]=atoi(argv[i]);
    }
        sort(arr, sz);
        return 0;

}
