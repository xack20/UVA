#include<stdio.h>
int main()
{
				int a=1,i,b1[3]={7,6,5},j,k=-2;
				for(i=1;i<=5;i++){
								a=a+2;
								k=k+2;
								for(j=0;j<=2;j++){
								printf("I=%d J=%d\n",a-2,b1[j]+k);
								}
								}
				return 0;
}
								
						    