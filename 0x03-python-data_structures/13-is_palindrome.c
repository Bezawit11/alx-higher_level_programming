#include <stdio.h>
#include "lists.h"

/**
 *is_palindrome - a function that checks if a singly linked list is a palindrome.
 *@head: singly linked list
 *Return: returns 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *c = *head, *f = *head;
while (f->next != NULL){
c = f;
while (c->next->next != NULL){
c = c->next;
}
if (f->n == c->next->n){
f = f->next;
c->next = NULL;
}
else
return (0);
}
return 1;
}
