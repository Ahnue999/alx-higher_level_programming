#include "lists.h"

/**
 * check_repeat - checks if a certain address exist in a linked list.
 * @ptr: the adress.
 * @arr: the array of addresses to check from.
 * @size: the size of the array.
 *
 * Return: 1 if it exists and 0 otherwise.
 */
int check_repeat(listint_t *ptr, listint_t **arr, int size)
{
	int i;

	for (i = 0; i < size; i++)
	{
		if (arr[i] == ptr)
			return (1);
	}
	return (0);
}

/**
 * check_cycle : checks the existence of a cycle in a linked list.
 * @list: a pointer to the first member of the list.
 *
 * Return: 1 if there is, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t **ptrarr;
	listint_t *current;
	int i;

	ptrarr = malloc(sizeof(listint_t) * 128);
	
	current = list;
	i = 0;
	while (current->next)
	{
		if (check_repeat(current, ptrarr, i))
		{
			free(ptrarr);
			return (1);
		}
		ptrarr[i] = current;
		current = current->next;
			i++;
	}
	return (0);
}
