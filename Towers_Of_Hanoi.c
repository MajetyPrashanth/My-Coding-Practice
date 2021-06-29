#include <stdio.h>
#include <stdlib.h>
int ToH (int x, char a, char b, char c);
int main ()
{
  int n;
  printf ("Enter Number of rings: ");
  scanf ("%d", &n);
  ToH (n, 'A','B','C');
  return 0;
}

int ToH (int x, char a, char b, char c)
{
    if(x==1)
    {
        printf("Move disk 1 from rod %c to rod %c \n",a,b);
        return 0; 
    }
    ToH(x-1, a, b, c);
    printf("Move disk %d from rod %c to rod %c \n",x,a,c);
    ToH(x-1, b, c, a);
}
