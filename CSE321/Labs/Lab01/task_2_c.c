#include <stdio.h>
#include <string.h>

int main() {
    char input_string[100];
    int lowercase_letter = 0;
    int uppercase_letter = 0;
    int digit = 0;
    int special_character = 0;
    char output[100] = "";

    printf("Enter a string: ");
    fgets(input_string, 100, stdin);
    input_string[strcspn(input_string, "\n")] = 0; // remove newline character from input

    for (int i = 0; i < strlen(input_string); i++) {
        if (input_string[i] >= 'A' && input_string[i] <= 'Z') {
            uppercase_letter += 1;
        } else if (input_string[i] >= 'a' && input_string[i] <= 'z') {
            lowercase_letter += 1;
        } else if (input_string[i] >= '0' && input_string[i] <= '9') {
            digit += 1;
        } else if (input_string[i] == '_' || input_string[i] == '$' ||
                   input_string[i] == '#' || input_string[i] == '@') {
            special_character += 1;
        }
    }

    if (lowercase_letter == 0 && output[0] == '\0') {
        strcat(output, "Lowercase missing");
    } else if (lowercase_letter == 0 && output[0] != '\0') {
        strcat(output, "Lowercase missing, ");
    }
    if (uppercase_letter == 0 && output[0] == '\0') {
        strcat(output, "Uppercase missing, ");
    } else if (uppercase_letter == 0 && output[0] != '\0') {
        strcat(output, "Uppercase missing");
    }
    if (digit == 0 && output[0] == '\0') {
        strcat(output, "Digit missing");
    } else if (digit == 0 && output[0] != '\0') {
        strcat(output, "Digit missing, ");
    }
    if (special_character == 0) {
        strcat(output, "Special character missing");
    }

    if (strlen(output) == 0) {
        printf("OK\n");
    } else {
        printf("%s\n", output);
    }

    return 0;
}
