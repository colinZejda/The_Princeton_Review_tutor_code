// max. five withdrawals
// max. 100 dollars per withdrawal
// user can't go negative
// show balance

#include <stdio.h>
#include <math.h>

int main(void)
{
  
    float withdrawal = 0;
    float balance = 500;
    int counter = 1;

    while(counter <= 5) {
    
        printf("enter withdrawal amount: ");
        scanf("%f", &withdrawal);
        

        if (withdrawal > 100 || withdrawal < balance || withdrawal < 0)
        {
          	printf("Invalid withdrawal.");
            continue;
        }
      
        balance -= withdrawal;
      	printf("your balance is: $%.2f \n", balance);
        counter++;
    }
        
    return 0;
}
