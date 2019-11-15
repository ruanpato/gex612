#include <stdio.h>
#include <stdlib.h>

int cnt=0, counter=0;

//                                    <Functions prototype>                                   //

// Function: clear.                                                                           //
// Receive: nothing.                                                                          //
// Returns: nothing.                                                                          //
// Description: Clear console.                                                                //
void clear();
// Function: ST_2(Stirling triangle second type).                                             //
// Receive: int n, int k.                                                                     //
// Returns: int of calculation of Stirling triangle of second type.                           //
// Description: This function calculate in a recursive form stirling triangle of second type. //
int ST_2(int n, int k);

//                                    </Functions prototype>                                  //

int main(){
    int a, b, c, i;
    do{
        printf("1) Calculate stirling number.\n2) Calculate stirling number of k until 0.\n0) Exit.\n-> ");
        scanf("%d", &a);
        switch(a){
            case 0:
                clear();
                printf("Exiting...\n");
                break;
            case 1: counter = 0;
                clear();
                printf("Type the n(no negative and no null integer number): ");
                scanf("%d", &b);
                printf("Type the k(no negative and no null integer number): ");
                scanf("%d", &c);
                if(b >= 1 && c >= 1)
                    printf("Calculate stirling triangle of second type of n(%d) and k(%d):\nST_2 = %d.\n", b, c, ST_2(b, c));
                else
                    printf("Invalid numbers, n and k need be >= 1.\n");
                break;
            case 2:
                printf("Type the k(no negative and no null integer number): ");
                scanf("%d", &c);
                printf("Stirling numbers of second kind [%d, 1]\n", c);
                for(i = c; i >= 0; i--){
                    if(i != 0)
                        printf("%d ", ST_2(c, i));
                    else
                        printf("%d.\n", ST_2(c, i));
                }
                break;
            default:
                clear();
                printf("%d is a Invalid option.\n", a);
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

// Function: ST_2(Stirling triangle second type)                                              //
// Receive: int n, int k                                                                      //
// Returns: int of calculation of Stirling triangle of second type                            //
// Description: This function calculate in a recursive form stirling triangle of second type. //
int ST_2(int n, int k){
    //printf("%d) - n=%d, k=%d. cnt=%d\n", counter, n, k, cnt);
    counter++;
    if(n==k)
        return 1;
    if(k==0)
        return 0;
    if(n > 1)
        return k * ST_2(n-1, k) + ST_2(n-1, k-1);
    if(k > 1)
        return 0;
    cnt++;
    return 1;
}