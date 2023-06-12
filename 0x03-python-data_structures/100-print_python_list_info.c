#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, size_alloc, i;
	PyObject *elem;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", size_alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		elem = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(elem)->tp_name);
	}
}
