#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int len, i;
    printf("Enter a string: ");
    scanf("%s", str);
    len = strlen(str);
    for (i = 0; i < len/2; i++) {
        if (str[i] != str[len-1-i]) {
            printf("Not a palindrome\n");
            return 0;
        }
    }
    printf("Palindrome\n");
    return 0;
}
