
Python 2
""""""""

As the unpacking operator in Python3 we can use
the sequence unpacking operator **in**  a function's parameter list 
(and only in function parameters or arguments).
This useful when we want to create functions that can

.. _var_pos_arg:

A function can take a variable number of positional arguments.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Here a product() function [prog_in_python3]_ . ::

   >>> def product(*args):
         result = 1 
         for arg in args:
            result *= arg
            return result

   >>> product(1, 2, 3, 4)
   24                                                                                                                                                                                        |
   >>>  
   >>> product(2, 3)
   6   

We cannot have arguments after unpacking sequence
"""""""""""""""""""""""""""""""""""""""""""""""""
::
        
   >>> def func(*arg, arg2 = None): 
   File "<stdin>", line 1  
   def func(*arg, arg2 = None):
                  ^
   SyntaxError: invalid syntax

we can unpack a dictionnary to populate function's name arguments
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Just as we can unpack a sequence to populate a function's positional arguments,
we also, can unpack a mapping using the mapping unpacking operator ** .
We can use ** to pass a dictionary to a argument.
Here the options dictionary's key-value pairs are unpacked
with each key's value being assigned to the parameter whose name is the same as the key.
If the dictionnary contains a key for wich there is no corresponding parameter,
a TypeError is raised. Any argument for which the dictionary has no corresponding item is set at this default value. ::

   >>> def func(a = 2, b = 3):
   ...     print a, b
   ...   
   >>> d = {'a':4,'b':5}             
   >>> func(**d)
   >>> 4 5
   >>>     
   >>> d = {'a':4,'c':5}                 
   >>> func(**d)
   Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   TypeError: func() got an unexpected keyword argument 'c'
   >>> d = {'a':4}
   >>> func(**d)
   >>> 4 3

We can also use dictionary to specify a variable number of named argument.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

For this we use the \*\* operator.
In this case, the \*\* operator **must be the last** argument. ::

   >>> def func(a = 2, b = 3,**kwargs):
   ...     print a                     
   ...     print b                     
   ...     print kwargs                
   ...                                 
   >>> def func(a = 2, b = 3, **kwargs, d = 4):
   File "<stdin>", line 1                      
   def func(a = 2, b = 3, **kwargs, d = 4):    
                                 ^          
   SyntaxError: invalid syntax                 
   >>>                                         
   >>> def func(*arg, **kwarg):                
   ...     print "arg =", arg                          
   ...     print "kwarg =", kwarg                        
   ...                                         
   >>> func(1, 2, 3)                           
   arg = (1, 2, 3)                                   
   kwarg = {}                                          
   >>>                                         
   >>> func([1, 2, 3], a= 'A', b = 'B')        
   arg = ([1, 2, 3],)                                
   kwarg = {'a': 'A', 'b': 'B'}                        
   >>>                                         
   >>> func([1, 2, 3],{'a':'A', 'b':'B'})      
   arg = ([1, 2, 3], {'a': 'A', 'b': 'B'})           
   kwarg = {}
   >>> l = [1, 2, 3]
   >>> d = {'a':'A', 'b':'B'}
   >>> func(*l, **d)
   arg = (1, 2, 3)
   kwarg = {'a': 'A', 'b': 'B'}
       
       
Python 3
""""""""

A function can take a variable number of positional arguments.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This feature work's exactly as in :ref:`Python2 <var_pos_arg>` 


Python3 support keywords arguments following unpacking sequence
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   >>> def func( *arg, arg2 = None):
   ...     print(arg) 
   ...     print(arg2)
   ...    
   >>> func([1,2,3]) 
   ([1, 2, 3],) 
   None 
   >>>    
   >>> func([1,2,3] , arg2='a')  
   ([1, 2, 3],) 
   a 
   
   
we can unpack a mapping to populate function's name arguments
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


We can also use mapping to specify a variable number of named argument.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

It works as in Python2 ::

   >>> def func(a = 2, b = 3,**kwargs):
   ...     print(a)                     
   ...     print(b)                     
   ...     print(kwargs)                
   ...   
                                 
   >>> def func(a = 2, b = 3, **kwargs, d = 4):
   File "<stdin>", line 1                      
   def func(a = 2, b = 3, **kwargs, d = 4):    
                                 ^          
   SyntaxError: invalid syntax                 
   >>>                                         
   >>> def func(*arg, **kwarg):                
   ...     print("arg =", arg)                          
   ...     print("kwarg =", kwarg)                        
   ...                                         
   >>> func(1, 2, 3)                           
   arg = (1, 2, 3)                                   
   kwarg = {}                                          
   >>>                                         
   >>> func([1, 2, 3], a= 'A', b = 'B')        
   arg = ([1, 2, 3],)                                
   kwarg = {'a': 'A', 'b': 'B'}                        
   >>>                                         
   >>> func([1, 2, 3],{'a':'A', 'b':'B'})      
   arg = ([1, 2, 3], {'a': 'A', 'b': 'B'})           
   kwarg = {}
   >>> l = [1, 2, 3]
   >>> d = {'a':'A', 'b':'B'}
   >>> func(*l, **d)
   arg = (1, 2, 3)
   kwarg = {'a': 'A', 'b': 'B'}



