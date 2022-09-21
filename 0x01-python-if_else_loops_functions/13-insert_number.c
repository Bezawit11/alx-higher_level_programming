#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)

{
listint_t *temp, *new;
temp = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
while (temp->next != NULL)
{
new->next = temp->next;
if (temp->next->n > number)
{
new->n = number;
new->next->next = temp->next;
}
new->n = temp->n;
temp = temp->next;
new = new->next;
}
return (new);
}
