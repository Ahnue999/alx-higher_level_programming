#include <stdio.h>
#include <Python.h>
#include <time.h>

struct timespec;


/**
 * print_python_list_info - prints python's list info
 * @p: PyObject pointer
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *memb;


	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);


	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);


	for (i = 0; i < size; i++)
	{
		memb = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(memb)->tp_name);
	}
}
