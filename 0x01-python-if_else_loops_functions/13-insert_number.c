#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *after, *new;

	new = malloc(sizeof(listint_t));

	new->n = number;
	new->next = NULL;

	if (!*head)
	{
		*head = new;
		return (*head)
	}

	curr = *head;
	after = (*head)->next
	while (after)
	{
		if (new->n <= curr->n && new->n <= after->n)
		{
			curr->next = new;
			new->next = after;
			return (new);
		}
		curr = after;
		after = after->next;
	}

	if (new->n >= curr->n)
	{
		curr->next = new;
		return (new);
	}
	else
	{
		new->next = curr;
		curr->next = NULL;
		*head = new;
		return (new);
	}
}
