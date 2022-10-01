#include <stdio.h>
#include "lists.h"

/**
 *is_palindrome - a function that checks if a singly linked list is a palindrome.
 *@head: singly linked list
 *Return: returns 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *c = *head, *f = *head, *g = *head;
int l = 0, i, r;
if (*head == NULL)
return 1;
if (f->next == NULL)
return 1;
while (g != NULL)
{
l++;
g = g->next;
}
for (i = 1; i < l - 1; i++){
c = c->next;
}
if (f->n == c->next->n){
if (f == c){
return 1;}
f = f->next;
c->next = NULL;
r = is_palindrome(&f);}
else{
return (0);}
return r;
}
