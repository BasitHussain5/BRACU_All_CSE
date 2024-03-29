//Lab Tasks:
//1. Write a C program to check if the entered character is vowel or consonant.
#include <stdio.h>

int main() {
    char c;

    printf("Enter a character: ");
    scanf("%c", &c);

    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
        c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
        printf("%c is a vowel.\n", c);
    } else {
        printf("%c is a consonant.\n", c);
    }

    return 0;
}



//2. Write a C program to check whether a triangle can be formed by the given value for the angles.
#include <stdio.h>

int main() {
    float angle1, angle2, angle3;

    printf("Enter the three angles of the triangle: ");
    scanf("%f %f %f", &angle1, &angle2, &angle3);

    if (angle1 + angle2 + angle3 == 180) {
        printf("The given angles form a valid triangle.\n");
    } else {
        printf("The given angles do not form a valid triangle.\n");
    }

    return 0;
}



//3. Write a C program to find the sum of even numbers between 1 to n.
#include <stdio.h>

int main() {
    int n, i, sum = 0;

    printf("Enter the value of n: ");
    scanf("%d", &n);

    for (i = 2; i <= n; i += 2) {
        sum += i;
    }

    printf("The sum of even numbers between 1 and %d is %d.\n", n, sum);

    return 0;
}



//4. Write a C program to reverse the numbers in an array.
#include <stdio.h>

int main() {
    int n, i, temp;

    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter the elements of the array:\n");

    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Reversing the array
    for (i = 0; i < n/2; i++) {
        temp = arr[i];
        arr[i] = arr[n-i-1];
        arr[n-i-1] = temp;
    }

    printf("The reversed array is: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}



//5. Write a C program to find diameter, circumference and area of circle using function.
#include <stdio.h>

float diameter(float r);
float circumference(float r);
float area(float r);

int main() {
    float r;

    printf("Enter the radius of the circle: ");
    scanf("%f", &r);

    printf("Diameter = %.2f units\n", diameter(r));
    printf("Circumference = %.2f units\n", circumference(r));
    printf("Area = %.2f square units\n", area(r));

    return 0;
}

float diameter(float r) {
    return 2 * r;
}

float circumference(float r) {
    return 2 * 3.14 * r;
}

float area(float r) {
    return 3.14 * r * r;
}



//6. Write a C program to swap two numbers in an array using function call by reference.
#include <stdio.h>

void swap(int *a, int *b);

int main() {
    int arr[2], i;

    printf("Enter two numbers:\n");
    for (i = 0; i < 2; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Before swapping: arr[0] = %d, arr[1] = %d\n", arr[0], arr[1]);

    // Swapping the numbers
    swap(&arr[0], &arr[1]);

    printf("After swapping: arr[0] = %d, arr[1] = %d\n", arr[0], arr[1]);

    return 0;
}

void swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}



//7. Write a C program to open a text file and print the characters [a-z, A-Z] only from that file.
#include <stdio.h>

int main() {
    FILE *fp;
    char ch;

    fp = fopen("input.txt", "r");  // Open file in read mode

    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    printf("The characters [a-z, A-Z] in the file are:\n");

    while ((ch = fgetc(fp)) != EOF) {
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
            putchar(ch);
        }
    }

    fclose(fp);

    return 0;
}



//8. Write a C program to sort given numbers using command line arguments.
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int i, j, temp;
    int arr[argc-1];

    // Convert command line arguments to integers and store in an array
    for (i = 1; i < argc; i++) {
        arr[i-1] = atoi(argv[i]);
    }

    // Bubble sort the array in ascending order
    for (i = 0; i < argc-2; i++) {
        for (j = 0; j < argc-i-2; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    // Print the sorted array
    printf("Sorted numbers: ");
    for (i = 0; i < argc-1; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
