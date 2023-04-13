#include <stdio.h>
#include <string.h>

int main()
{
    char email_address[100];
    printf("Enter employee email: ");
    scanf("%s", email_address);

    char *domain = strrchr(email_address, '@');
    if (domain == NULL){
        printf("Invalid email address\n");
        return 0;
    }
    if (strcmp(domain +1, "sheba.xyz") == 0){
        printf("Emial address is okay\n");
    }
    else{
        printf("Email address is outdated\n");
    }
    return 0;
}
