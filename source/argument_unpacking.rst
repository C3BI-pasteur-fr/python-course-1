.. tabularcolumns:: |p{8cm}|p{8cm}| 

+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| Python2                                                                                                              | Python3                                                            |
+======================================================================================================================+====================================================================+
| As the unpacking operator in Python3 we can use                                                                                                                                           |
| the sequence unpacking operator in a function's parameter                                                                                                                                 |
| list (this also works well in python2 or python3).                                                                                                                                        |
| This useful when we want to create functions that can                                                                                                                                     |
| take a variable number of positional arguments. Here a product() function [prog_in_python3]_ .                                                                                            |
|                                                                                                                                                                                           |
| >>> def product(\*args):                                                                                                                                                                  |
| ...     result = 1                                                                                                                                                                        |
| ...     for arg in args:                                                                                                                                                                  |
| ...             result \*= arg                                                                                                                                                            |
| ...     return result                                                                                                                                                                     |
| ...                                                                                                                                                                                       |
| >>> product(1, 2, 3, 4)                                                                                                                                                                   |
| 24                                                                                                                                                                                        |
| >>>                                                                                                                                                                                       |
| >>> product(2, 3)                                                                                                                                                                         |
| 6                                                                                                                                                                                         |
| >>>                                                                                                                                                                                       |
|                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| We cannot have arguments after unpacking sequence                                                                    | Python3 support keywords arguments following positional arguments, |
|                                                                                                                      | even if it's an unpacking sequence argument.                       |
| >>> def func(\*arg, arg2 = None):                                                                                    |                                                                    |
| File "<stdin>", line 1                                                                                               | >>> def func( \*arg, arg2 = None):                                 |
| def func(\*arg, arg2 = None):                                                                                        | ...     print(arg)                                                 |
| ^                                                                                                                    | ...     print(arg2)                                                |
| SyntaxError: invalid syntax                                                                                          | ...                                                                |
|                                                                                                                      | >>> func([1,2,3])                                                  |
|                                                                                                                      | ([1, 2, 3],)                                                       |
|                                                                                                                      | None                                                               |
|                                                                                                                      | >>>                                                                |
|                                                                                                                      | >>> func([1,2,3] , arg2='a')                                       |
|                                                                                                                      | ([1, 2, 3],)                                                       |
|                                                                                                                      | a                                                                  |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| Just as we can unpack a sequence to populate a function's positionalarguments,                                                                                                            |
| we can unpack a mapping using the mapping unpacking operator \*\*.                                                                                                                        |
| We can use \*\* to pass a dictionary to a argument.                                                                                                                                       |
| Here the options dictionary's key-value pairs are unpackecd                                                                                                                               |
| with each key's value being assigned to the parameter whose name is the same as the  key.                                                                                                 |
| If the dictionnary contains a key for wich there is no corresponding parameter,                                                                                                           |
| a TypeError is raised. Any argument for which the dictionary has no corresponding item is set at this default value.                                                                      |
|                                                                                                                                                                                           |
| >>> def func(a = 2, b = 3):                                                                                                                                                               |
| ...     print(a, b)                                                                                                                                                                       |
| ...                                                                                                                                                                                       |
| >>> func(\* \*{'a':4,'b':5})                                                                                                                                                              |
|                                                                                                                                                                                           |
| >>>                                                                                                                                                                                       |
| >>> func(\* \*{'a':4,'c':5})                                                                                                                                                              |
| Traceback (most recent call last):                                                                                                                                                        |
| File "<stdin>", line 1, in <module>                                                                                                                                                       |
| TypeError: func() got an unexpected keyword argument 'c'                                                                                                                                  |
| >>>                                                                                                                                                                                       |
| >>> func(\* \*{'a':4})                                                                                                                                                                    |
| >>>                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| We can also use mapping unpacking operator with parameter.                                                                                                                                |
|                                                                                                                                                                                           |
| In this case, the ** operator must be the last argument.                                                                                                                                  |
|                                                                                                                                                                                           |
| >>> def func(a = 2, b = 3,**kwargs):                                                                                                                                                      |
| ...     print a                                                                                                                                                                           |
| ...     print b                                                                                                                                                                           |
| ...     print kwargs                                                                                                                                                                      |
| ...                                                                                                                                                                                       |
| >>> def func(a = 2, b = 3, \* \*kwargs, d = 4):                                                                                                                                           |
| File "<stdin>", line 1                                                                                                                                                                    |
| def func(a = 2, b = 3, \* \*kwargs, d = 4):                                                                                                                                               |
| ^                                                                                                                                                                                         |
| SyntaxError: invalid syntax                                                                                                                                                               |
| >>>                                                                                                                                                                                       |
| >>> def func(\*arg, \* \*kwarg):                                                                                                                                                          |
| ...     print(arg)                                                                                                                                                                        |
| ...     print(kwarg)                                                                                                                                                                      |
| ...                                                                                                                                                                                       |
| >>> func(1, 2, 3)                                                                                                                                                                         |
| (1, 2, 3)                                                                                                                                                                                 |
| {}                                                                                                                                                                                        |
| >>>                                                                                                                                                                                       |
| >>> func([1, 2, 3], a= 'A', b = 'B')                                                                                                                                                      |
| ([1, 2, 3],)                                                                                                                                                                              |
| {'a': 'A', 'b': 'B'}                                                                                                                                                                      |
| >>>                                                                                                                                                                                       |
| >>> func([1, 2, 3],{'a':'A', 'b':'B'})                                                                                                                                                    |
| ([1, 2, 3], {'a': 'A', 'b': 'B'})                                                                                                                                                         |
| {}                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+


