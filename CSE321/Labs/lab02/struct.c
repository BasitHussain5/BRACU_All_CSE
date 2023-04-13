#include <stdio.h>
#include <string.h>

struct Menue
{
    int quantity;
    int unit_price;
};

int main()
{
    struct Menue paratha, vegetable, mineral_water;


    printf("Quantity Of Paratha: ");
    scanf("%d", &paratha.quantity);
    printf("Unit Price: ");
    scanf("%d", &paratha.unit_price);


    printf("Quantity Of vegetable: ");
    scanf("%d", &vegetable.quantity);
    printf("Unit Price: ");
    scanf("%d", &vegetable.unit_price);

    printf("Quantity Of mineral_water: ");
    scanf("%d", &mineral_water.quantity);
    printf("Unit Price: ");
    scanf("%d", &mineral_water.unit_price);

    int number_people;
    printf("Number of People: ");
    scanf("%d", &number_people);


    float total_bill = (paratha.quantity * paratha.unit_price) + (vegetable.quantity * vegetable.unit_price) + (mineral_water.quantity * mineral_water.unit_price);



    float per_person = total_bill / number_people;
    printf("Individual people will pay: %.2f tk\n", per_person);

    return 0;
}
