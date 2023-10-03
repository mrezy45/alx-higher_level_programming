#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
* insert_node - Function in C that inserts a number
* into  sorted singly linked list.
* @head: Pointer to the head of linked list
* @number: The number to insert
* Return: The address of new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;

	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current && current->next && current->next->n < number)
	{
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
