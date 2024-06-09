#include<stdio.h>
int main(){
int a,b,c,sum; 
printf("Enter three integers:");
scanf("%d%d%d",&a,&b,&c);
sum=a+b+c; 
printf("Sum of %d, %d and %d %d\n",a,b,c,sum); 
float avg=sum/3.0; 
printf("Average of %d, %d and %d:%f\n",a,b,c,avg);
return 0;
}
