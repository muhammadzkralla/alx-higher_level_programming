#include "lists.h"

/**
 * iterateLinkedList - creates a map of the indices and the values.
 * with int pointer.
 *
 * @head: double pointer to the linked list
 * @length: size of the linked list
 *
 * Return: int pointe, the indices map.
 */
int *iterateLinkedList(listint_t **head, int *length)
{

	if (*head == NULL)
	{
		return (NULL);
	}

	int *indicesMap = (int *)malloc(sizeof(int));
	int currentIdx = 0;
	listint_t *current = *head;

	while (current != NULL)
	{
		indicesMap[currentIdx] = current->n;

		current = current->next;
		currentIdx++;

		indicesMap = (int *)realloc(indicesMap, (currentIdx + 1) * sizeof(int));
	}


	*length = currentIdx;

	return (indicesMap);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int sz = 0;
	int *indicesMap = iterateLinkedList(head, &sz);
	int l = 0;
	int r = sz - 1;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (l <= r)
	{


		if (indicesMap[l] != indicesMap[r])
		{
			return (0);
		}

		l++;
		r--;
	}

	free(indicesMap);

	return (1);
}












