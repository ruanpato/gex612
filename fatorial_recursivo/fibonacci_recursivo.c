#include <stdio.h>
#include <stdlib.h>

//                                    <Functions prototype>                                   //

// Function: clear.                                                                           //
// Receive: nothing.                                                                          //
// Returns: nothing.                                                                          //
// Description: Clear console.                                                                //
void clear();
// Function: fibonacci                                                                        //
// Receive: long int n                                                                        //
// Returns: lon long int of calculation of fibonacci.                                         //
// Description: This function calculate in a recursive form fibonacci.                        //
long long int fibonacci(long int n);

//                                    </Functions prototype>                                  //

int main(){
    long int a, b, c, i;
    do{
        printf("1) Calculate fibonacci of a specific number.\n2) Calculate fibonacci of n until 0.\n0) Exit.\n-> ");
        scanf("%ld", &a);
        switch(a){
            case 0:
                clear();
                printf("Exiting...\n");
                break;
            case 1:
                clear();
                printf("Type the n(no negative and no null integer number): ");
                scanf("%ld", &b);
                if(b >= 0)
                    printf("Calculate fibonacci of n(%ld):\nFibonacci = %lld.\n", b, fibonacci(b));
                else
                    printf("Invalid numbers, n need be >= 0.\n");
                break;
            case 2:
                printf("Type the n(no negative and no null integer number): ");
                scanf("%ld", &b);
                printf("Fibonacci [%ld, 0]\n", b);
                for(i = b; i >= 0; i--){
                    if(i != 0)
                        printf("%lld ", fibonacci(i));
                    else
                        printf("%lld.\n", fibonacci(i));
                }
                break;
            default:
                clear();
                printf("%ld is a Invalid option.\n", a);
                break;
        }
    }while(a!=0);

    return 0;
}

// Function: clear.                                                                           //
// Receive: nothing.                                                                          //
// Returns: nothing.                                                                          //
// Description: Clear console.                                                                //
void clear(){
    #if defined(__linux__) || defined(__unix__) || defined(__APPLE__)
        system("clear");
    #endif
    #if defined(_WIN32) || defined(_WIN64)
        system("cls");
    #endif
}

// Function: fibonacci                                                                        //
// Receive: long int n                                                                        //
// Returns: lon long int of calculation of fibonacci.                                         //
// Description: This function calculate in a recursive form fibonacci.                        //
long long int fibonacci(long int n){
    if(n < 2)
        return n;
    else
        return (fibonacci(n-1)+fibonacci(n-2));
}