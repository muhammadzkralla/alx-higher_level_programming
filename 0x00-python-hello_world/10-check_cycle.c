#include "lists.h"

/**
 * check_cycle - checks for looping in linked lists.
 *
 * @list: head of the linked list.
 *
 * Return: 1 if yes, default : 0
 */

int check_cycle(listint_t *list)
{

	listint_t *current, *nxt;

	if (!list)
	{
		return (0);
	}

	current = list;
	nxt = list->next;

	while (current && nxt && nxt->next)
	{

		if (current == nxt)
		{
			return (1);
		}
		current = current->next;
		nxt = nxt->next->next;
	}

	return (0);

}
