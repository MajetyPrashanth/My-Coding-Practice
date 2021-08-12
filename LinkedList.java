import java.util.*;
class SinglyLinkedList
{
class Node
    {
        int data;
        Node next;
        public Node(int data)
        {
            this.data = data;
            this.next = null;
        }
    }
    public Node head = null;
    public Node tail = null;
    public void add(int data)
    {
        Node newnode = new Node(data);
        if(head == null)
        {
            head = newnode;
            tail = newnode;
        }
        else
        {
            tail.next = newnode;
            tail = newnode;
        }
    }
    public void display()
    {
        Node current = head;
        if(head == null)
            System.out.println("LIST IS EMPTY !!!");
        System.out.println("Nodes in the LIST ARE : ");
        while(current != null)
        {
            System.out.print(current.data+"-->");
            current = current.next;
        }
    }
public static void main(String [] args)
    {
        SinglyLinkedList sl = new SinglyLinkedList();
        sl.add(10);
        sl.add(20);
        sl.add(30);
        sl.add(40);
        //to display all items : 
        sl.display();
    }
}
