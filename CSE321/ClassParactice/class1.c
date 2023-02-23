// Lab Tasks:
// 1. Write a C program to print your name, date of birth. and mobile number.
#include <stdio.h>

int main() {
    char name[] = "John Doe";
    char dob[] = "01/01/2000";
    char mobile[] = "123-456-7890";

    printf("Name: %s\n", name);
    printf("Date of birth: %s\n", dob);
    printf("Mobile number: %s\n", mobile);

    return 0;
}

// 2. Write a C program to compute the perimeter and area of a rectangle with a height of 7 inches. and
// width of 5 inches.
#include <stdio.h>

int main() {
    int height = 7;
    int width = 5;
    int perimeter, area;

    perimeter = 2 * (height + width);
    area = height * width;

    printf("Perimeter of rectangle = %d inches\n", perimeter);
    printf("Area of rectangle = %d square inches\n", area);

    return 0;
}

// 3. Write a C program to compute the perimeter and area of a circle with a given radius.
#include <stdio.h>

#define PI 3.14159

int main() {
    float radius, perimeter, area;

    printf("Enter the radius of the circle: ");
    scanf("%f", &radius);

    perimeter = 2 * PI * radius;
    area = PI * radius * radius;

    printf("Perimeter of the circle = %f units\n", perimeter);
    printf("Area of the circle = %f square units\n", area);

    return 0;
}

// 4. Write a program in C to store elements in an array and print it.
#include <stdio.h>

#define MAX_SIZE 100

int main() {
    int arr[MAX_SIZE];
    int size, i;

    printf("Enter the size of the array: ");
    scanf("%d", &size);

    printf("Enter the elements of the array: ");
    for (i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    printf("The elements of the array are: ");
    for (i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}

// 5. Write a program in C to read n number of values in an array and display it in reverse order
#include <stdio.h>

#define MAX_SIZE 100

int main() {
    int arr[MAX_SIZE];
    int size, i;

    printf("Enter the size of the array: ");
    scanf("%d", &size);

    printf("Enter the elements of the array: ");
    for (i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    printf("The elements of the array in reverse order are: ");
    for (i = size - 1; i >= 0; i--) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}

// 6. Write a C program to convert a given integer (in seconds) to hours, minutes and seconds.
#include <stdio.h>

int main() {
    int seconds, hours, minutes, remaining_seconds;

    printf("Enter the time in seconds: ");
    scanf("%d", &seconds);

    hours = seconds / 3600;
    minutes = (seconds % 3600) / 60;
    remaining_seconds = seconds % 60;

    printf("%d seconds is equal to %d hours, %d minutes and %d seconds\n", seconds, hours, minutes, remaining_seconds);

    return 0;
}

// 7. Write a C Program to Swap Values of Two Variables.
#include <stdio.h>

int main() {
    int num1, num2, temp;

    printf("Enter the first number: ");
    scanf("%d", &num1);

    printf("Enter the second number: ");
    scanf("%d", &num2);

    printf("Before swapping: num1 = %d, num2 = %d\n", num1, num2);

    // Swapping using a temporary variable
    temp = num1;
    num1 = num2;
    num2 = temp;

    printf("After swapping: num1 = %d, num2 = %d\n", num1, num2);

    return 0;
}

// 8. Write a C Program to Print ASCII Value of a given user input.
#include <stdio.h>

int main() {
    char ch;

    printf("Enter a character: ");
    scanf("%c", &ch);

    printf("ASCII value of %c is %d\n", ch, ch);

    return 0;
}

// 9. Write a C program to concatenate two strings given by the user.
#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];

    printf("Enter the first string: ");
    scanf("%s", str1);

    printf("Enter the second string: ");
    scanf("%s", str2);

    strcat(str1, str2);

    printf("Concatenated string: %s\n", str1);

    return 0;
}

// 10. Write a C program to store students information in a struct. Take input from users for a student and
// print it.
#include <stdio.h>

struct student {
    char name[50];
    int age;
    int roll_no;
};

int main() {
    struct student s;

    printf("Enter name: ");
    scanf("%s", s.name);

    printf("Enter age: ");
    scanf("%d", &s.age);

    printf("Enter roll number: ");
    scanf("%d", &s.roll_no);

    printf("Name: %s\n", s.name);
    printf("Age: %d\n", s.age);
    printf("Roll number: %d\n", s.roll_no);

    return 0;
}
