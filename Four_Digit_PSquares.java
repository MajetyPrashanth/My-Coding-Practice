import java.util.*;
public class Main
{
static void isPerfectSquare(int x)
    {
        if (x >= 0) 
        {
             
             int[] arr = new int[4];
             int sr = (int)Math.sqrt(x);
             if((sr * sr) == x)
             {
             int k = 0,temp = x;
                while(temp>0){
                    arr[k] = temp % 10;
                    temp = temp / 10;
                    k++;
                }
                if((arr[0]%2==0) && (arr[1]%2==0) && (arr[2]%2==0) && (arr[3]%2==0))
                {
                    System.out.println(x);
                }
             }
        }
}

public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        for(int i=1000 ; i < 10000 ; i++ )
        {
        isPerfectSquare(i);
        }
            
    }
}
