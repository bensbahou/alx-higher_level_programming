#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: The head of the singly linked list
 *
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int i, len = 0, len_cyc = 0, len_list = 0;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	start = *head;
	while (start != NULL)
	{
		start = start->next;
		++len;
	}
	len_cyc = len * 2;
	len_list = len_cyc - 2;
	end = *head;

	for (int i = 0; i < len_cyc; i += 2)
	{
		if (start[i].n != end[len_list].n)
			return (0);

		len_list -= 2;
	}

	return (1);
}

/**
 * get_nodeint_at_index - Gets a node from a linked list
 * @head: The head of the linked list
 * @index: The index to find in the linked list
 *
 * Return: the specific node of the linked list
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int iter_times = 0;

	while (head != NULL)
	{
		if (iter_times == index)
			return (head);

		head = head->next;
		++iter_times;
	}

	return (NULL);
}

