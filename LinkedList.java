import java.util.*;
public class LLprac 
{
    public static void main(String[] args) 
    {
    LinkedList<String> l1 = new LinkedList<>();
    l1.add("Hello");
    l1.add("This");
    l1.add("Is");
    l1.add("Prashanth");
    System.out.println("After addition of elements :"+l1);
    //changing an already set value
    l1.set(1,"Hi");
    System.out.println("\nAfter modification:"+l1);
    //removing an element using index
    l1.remove(1);
    System.out.println("\nAfter removal of Hi using index: "+l1+"\n");
    //removing an element by its value
    l1.remove("Hello");
    System.out.println("\nAfter removal of Hello: "+l1+"\n"); 
    //Iterating through the linked list
    System.out.println("\nPrinting using iteration : \n");
    for (int i = 0; i < l1.size(); i++) 
    { 
            System.out.print(l1.get(i) + "\n "); 
    } 
    }
}
