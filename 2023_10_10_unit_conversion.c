#include <stdio.h>

int main(void) {
    char option;
    int Continue = 1;

    do {
        printf("Please select one of the three main menu options below:\n");
        printf("C = Unit Conversions\nO = Ohm's Law\nR = Equivalent Resistance\n");
        printf("Enter your choice: ");
        scanf(" %c", &option);

        switch (option) {
            case 'C':
            case 'c': {
                char startUnit, endUnit;
                float inputValue, outputValue;

                printf("You have chosen Unit Conversions.\n");
                printf("Valid choices for units are:\n");
                printf("a = milli\nb = standard\nc = kilo\n");

                // Prompt for starting and ending units
                printf("Enter the starting unit (a/b/c): ");
                scanf(" %c", &startUnit);

                while (startUnit != 'a' && startUnit != 'b' && startUnit != 'c') {
                    printf("Invalid choice. Please enter a valid starting unit (a/b/c): ");
                    scanf(" %c", &startUnit);
                }

                printf("Enter the ending unit (a/b/c): ");
                scanf(" %c", &endUnit);

                while (endUnit != 'a' && endUnit != 'b' && endUnit != 'c') {
                    printf("Invalid choice. Please enter a valid ending unit (a/b/c): ");
                    scanf(" %c", &endUnit);
                }

                // Prompt for input value
                printf("Enter the value to convert: ");
                scanf("%f", &inputValue);

                // Perform the conversions
                if ((startUnit == 'a' && endUnit == 'b') || (startUnit == 'b' && endUnit == 'a')) {
                    outputValue = inputValue * 1000;
                } else if ((startUnit == 'a' && endUnit == 'c') || (startUnit == 'c' && endUnit == 'a')) {
                    outputValue = inputValue / 1000;
                } else {
                    outputValue = inputValue;  // No conversion needed for the same units
                }

                // Display the result
                printf("Starting Value: %0.4f %c\n", inputValue, startUnit);
                printf("Ending Value: %0.4f %c\n", outputValue, endUnit);

                break;
            }

            case 'O':
            case 'o': {
                char choice;
                float current, voltage, resistance, power;

                printf("You have chosen Ohm's Law.\n");
                printf("Do you want to find (V)oltage or (C)urrent? Enter V or C: ");
                scanf(" %c", &choice);

                if (choice == 'V' || choice == 'v') {
                    printf("Enter current (in amps): ");
                    scanf("%f", &current);
                    printf("Enter resistance (in ohms): ");
                    scanf("%f", &resistance);

                    voltage = current * resistance;
                    power = voltage * current;
                } else if (choice == 'C' || choice == 'c') {
                    printf("Enter voltage (in volts): ");
                    scanf("%f", &voltage);
                    printf("Enter resistance (in ohms): ");
                    scanf("%f", &resistance);

                    current = voltage / resistance;
                    power = voltage * current;
                } else {
                    printf("Invalid choice.\n");
                    break;
                }

                printf("Voltage: %0.4f V\n", voltage);
                printf("Current: %0.4f A\n", current);
                printf("Power: %0.4f W\n", power);

                break;
            }

            case 'R':
            case 'r': {
                char circuitType;
                int numResistors;
                float equivalentResistance = 0;

                printf("You have chosen Equivalent Resistance.\n");
                printf("Are the resistors in (S)eries or (P)arallel? Enter S or P: ");
                scanf(" %c", &circuitType);

                printf("How many resistors are you adding together? Enter the number: ");
                scanf("%d", &numResistors);

                if (circuitType == 'S' || circuitType == 's') {
                    for (int i = 1; i <= numResistors; i++) {
                        float resistorValue;
                        printf("Enter the value of resistor %d (in ohms): ", i);
                        scanf("%f", &resistorValue);
                        equivalentResistance += resistorValue;
                    }
                } else if (circuitType == 'P' || circuitType == 'p') {
                    for (int i = 1; i <= numResistors; i++) {
                        float resistorValue;
                        printf("Enter the value of resistor %d (in ohms): ", i);
                        scanf("%f", &resistorValue);
                        equivalentResistance += 1 / resistorValue;
                    }
                    equivalentResistance = 1 / equivalentResistance;
                } else {
                    printf("Invalid choice.\n");
                    break;
                }

                printf("Number of Resistors Included: %d\n", numResistors);
                printf("Equivalent Resistance: %0.4f ohms\n", equivalentResistance);

                break;
            }

            default:
                printf("Invalid menu choice. Please select a valid option (C/O/R).\n");
                break;
        }

        // Ask if the user wants to continue
        printf("Do you want to continue (Y/N)? ");
        scanf(" %c", &option);

        if (option == 'N' || option == 'n') {
            Continue = 0;
        }

    } while (Continue);

    printf("Goodbye!\n");

    return 0;
}