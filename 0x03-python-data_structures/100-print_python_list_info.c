#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: input
 */
void print_python_list_info(PyObject *p)
{
unsigned int idx, l, allocated;
PyTypeObject *type;
const char *name;
if (p == NULL)
return;
l = (unsigned int) PyList_Size(p);
allocated = (unsigned int) ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %d\n", l);
printf("[*] Allocated = %d\n", allocated);
for (idx = 0; idx < l; idx++)
{
type = PyList_GET_ITEM(p, idx)->ob_type;
name = type->tp_name;
printf("Element %d: %s\n", idx, name);
}
}
