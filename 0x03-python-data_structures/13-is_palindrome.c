include "lists.h"

listint_t *listidx(listint_t *head, idx)
{
	listint_t *curr;
	int i;

	curr = head;
	for (i = 0; i < idx, curr; i++)
	{
		curr = curr->next;
	}

	return (curr);
}

int is_palindrome(listint_t **head)
{
	listint_t* curr;
	int i, length;

	curr = *head;
	for (length = 0; curr; length++)
		curr = curr->next;

	curr = *head;
	for (i = 0; i < length / 2; i++)
	{
		if curr->next != listidx(*head, length - i)->n
			return (0);
	}
	return (1);
}
