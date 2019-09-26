#include <stdio.h>

long long int fat(int n){
	if ((n==1) || (n==0)) return 1;
	else
		return fat(n-1)*n;
}

int main(){
	int a;
	scanf("%d" , &a);
	printf("%lld\n" , fat(a));

	return 0;
}
