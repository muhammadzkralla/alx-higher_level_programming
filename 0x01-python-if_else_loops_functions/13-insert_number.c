#include "lists.h"

/**
 * check_cycle - checks for looping in linked lists.
 *
 * @head: pointer to the pointer to the head of the linked list.
 * @number: value of the node to be inserted.
 *
 * Description: initialize current node with the head node,
 * then allocates memory for the second node, if failed return NULL.
 * else set the value of the second node with passed value, then check if
 * the LL is empty or its current value greater than or equal passed value,
 * if so, add the second node first and set its next node to the current.
 * else loop the LL untill you find the suitable position.
 *
 * Return: inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *current, *nxt;

	current = *head;
	nxt = malloc(sizeof(listint_t));

	if (nxt == NULL)
		return (NULL);

	nxt->n = number;

	if (current == NULL || current->n >= number)
	{
		nxt->next = current;
		*head = nxt;
	}
	else
	{
		while (current && current->next && current->next->n < number)
			current = current->next;

		nxt->next = current->next;
		current->next = nxt;
	}

	return (nxt);
}
