#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 *insert_node -  inserts a number into a sorted singly linked list
 *@head:the linked list
 *@number: the node element
 *Return: returns the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)

{
listint_t *new, *c = *head, *g = *head;
unsigned int i, l = 0;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
if (*head == NULL){
new->n = number;
new->next = NULL;
*head = new;
return (*head);
}
while (g != NULL)
{
l++;
g = g->next;
}
for (i = 0; i < l - 1; i++)
{
if (c->next->n > number){
break;
}
c = c->next;
}
new->n = number;
if (i == l){
new->next = NULL;
c->next = new;
return (*head);
}
if (i == 0){
new->next = c;
*head = new;
return (*head);
}
new->next = c->next;
c->next = new;
return (*head);
}
