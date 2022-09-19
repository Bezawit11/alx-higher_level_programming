#include <stdio.h>
#include "lists.h"

/**
 *check_cycle - checks for a cycle in a linked list
 *@list: linked list to be checked
 *Return: returns 1 if cycle is found
 */
int check_cycle(listint_t *list)

{
listint_t *prev, *current;
prev = current = list;
while(prev && current && current->next) {
prev = prev->next;
current  = current->next->next;
if (prev == current) {
return 1;
}
}
return 0;
}
