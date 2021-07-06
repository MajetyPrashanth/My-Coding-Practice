#include <stdio.h>
#include <conio.h>
#include <malloc.h>
void deletion();
void traverse();
void insert();
int i,ch,n,j,item,pos;
struct node
{
    int data;
    struct node *next;
} *start = NULL, *newnode,*temp,*p;

int main()
{
    int k,num;
    printf("Enter number of elements : ");
    scanf("%d",&num);
    for(k=0; k<num; k++)
    {
        insert();
    }
    traverse();
    return 0;
}

void insert()
{
    temp = start;
    printf("Enter the item to be inserted: ");
    scanf("%d",&item);
    newnode = (struct node*) malloc (sizeof(struct node));
    newnode -> data = item;
    if(start == NULL)
    {
        newnode -> next = NULL;
        start = newnode;
    }
    else
    {
        while(temp -> next != NULL)
            temp = temp -> next;
        newnode -> next = NULL;
        temp -> next = newnode;
    }
}

void traverse()
{
    if(start == NULL)
     printf("List is Empty");
    else
    {
        for(temp=start ; temp -> next != NULL ; temp = temp ->next)
            printf(" %d --> ",temp->data);
            if(temp -> next == NULL)
            printf(" %d \n",temp->data);
    }       
}
