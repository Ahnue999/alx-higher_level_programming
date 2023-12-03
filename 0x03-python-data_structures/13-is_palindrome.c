#include "lists.h"

/**
 * listidx - gets the list member at a certain index.
 * @head: the list's head pointer.
 * @idx: the index to get.
 *
 * Return: a pointer to the list member at idx.
 */
listint_t *listidx(listint_t *head, int idx)
{
	listint_t *curr;
	int i;

	curr = head;
	for (i = 0; i < idx && curr; i++)
	{
		curr = curr->next;
	}

	return (curr);
}

/**
 * is_palindrome - checks whether a list is palindrome or not.
 * @head: the list's head pointer.
 *
 * Return: 1 if palindrom and 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t* curr;
	int i, length;

	curr = *head;
	for (length = 0; curr; length++)
		curr = curr->next;

	curr = *head;
	for (i = 0; i < ((length - 1) / 2); i++)
	{
		if (curr->n != listidx(*head, length - i - 1)->n)
			return (0);
		curr = curr->next;
	}
	return (1);
}
