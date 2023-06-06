#include "lists.h"

/**
 * check_cycle - function checks whether a singly linked list contains a cycle.
 * @list: beginning of the node
 * Return: 1 if there is a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *check = list;

	while (current && check && check->next)
	{
		current = current->next;
		check = check->next->next;
		if (current == check)
			return (1);
	}
	return (0);
}
