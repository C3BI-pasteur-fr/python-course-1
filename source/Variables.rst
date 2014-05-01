.. _Variables:

************************************
Variables, Expression and statements
************************************

Variables and Object References
===============================

Value and type
--------------

A **value** is one of the basic things a program works with, like a letter or a number.  
The values we have seen so far are ``1``, ``2``, and ``'Hello, World!'``.

These values belong to different **types**: ``2`` is an integer (:ref:`integers`), and ``'Hello, World!'`` is a **string** (:ref:`strings`),
so-called because it contains a "string" of letters. You (and the interpreter) can identify
strings because they are enclosed in quotation marks. We speak speak also of ``data type``.

If you are not sure what type a value has, the interpreter can tell you. ::

   >>> type('Hello, World!')
   <type 'str'>
   >>> type(17)
   <type 'int'>
 
Not surprisingly, strings belong to the type ``str`` and integers belong to the type ``int``.  
Less obviously, numbers with a decimal point belong to a type called ``float``,
because these numbers are represented in a format called ``floating point`` (:ref:`floating point`). ::

   >>> type(3.2)
   <type 'float'>

What about values like ``'17'`` and ``'3.2'``?
They look like numbers, but they are in quotation marks like strings. ::

   >>> type('17')
   <type 'str'>
   >>> type('3.2')
   <type 'str'>

They're strings.

When you type a large integer, you might be tempted to use commas or space
between groups of three digits, as in ``1,000,000``.  
This is not a legal integer in Python, but it is legal: ::

   >>> 1,000,000
   (1, 0, 0)

Well, that's not what we expected at all!  Python interprets ``1,000,000`` 
as a comma-separated sequence of integers.
This is the first example of a semantic error: the code
runs without producing an error message, but it doesn't do the ``right`` thing.

In Python, both ``str`` and ``int`` are immutable. That is once set their value cannot be changed anymore.
there exist some datatype which are mutable (we will see what this difference implies between this to kind
of datatype in :ref:`mutable obj` and :ref:`immutable obj` and some examples of mutable and immutable 
data types in  :ref:`Data_Types` and :ref:`Collection_Data_types`)

To convert a data item from one type to another, we can use the syntax *datatype(item)*. For example: ::
   
   >>> int("45")
   45
   >>> str(45)
   '45'
   
The ``int`` conversion is tolerant of leading and trailing whitespace. So int(" 45 ") would have worked just as well.
The ``str`` conversion can be applied to almost data item. 
If a conversion fails, an exception is raised (we will see fully :ref:`exceptions` later). ::

   >>> int('Hello World!')
   Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
   ValueError: invalid literal for int() with base 10: 'Hello World!'
  


Variables and Object references
-------------------------------

Once we have data item (or values), the next thing we need is variables in wich to store them.
A variable is a name that refers to a value.
One of the most powerful features of a programming language is the ability to manipulate ``variables``.  


As I mentioned earlier, in Python everything is an object, even int or string. ::

   >>> isinstance(3, object)
   True
   >>> isinstance('blue', object)
   True
   
.. note::
   
   An object is "something" which pack together 
    
   * a state, for instance the value 3 for the int or 'blue' for the string.
   * and a behavior: a set of methods (the operations that we can do on this object).
    
    For instance *'blue'* is the state, *upper* is a method applied to the value 'blue'::
     
     >>> 'blue'.upper()
     'BLUE'
     
   The object oriented programming is out of the scope of this course. So we don't see more about the objects.  

So Python does not have variable as such, but instead has ``object references``. When it comes to immutable objects
like ``str`` or ``int``, there is no discernable difference between variable and an object reference.
As for mutable objects there is a difference, but it rarely maters in practice. So we will use the terms of ``variable``
or ``object reference`` interchangeably.

Let's look at few examples and see what's happend in details: ::

   x = 3
   color = 'green'
   y = x

The syntax is simply ``object reference = value``. There is no need of predeclaration
and no need to specify the value's type. When Python execute 

* the first statement it creates a int object with the value ``3`` and create the object reference call ``x`` that refer to
  the int object. For all pratical purpose we say ``that variable x has been assigned the "3" integer``.
* The second statement is similar. 
* The third creates a new object reference z and sets it to refer to the same object
  that the x reference object refers to (in this case the int object containing the value "3").

Let's see what python do behind the scene:

.. figure:: _static/figs/ref_obj.png
   :align: left
   :alt: object references
   :figclass: align-left
   

| *The circles represents the object references.*
| *The rectangles the objects in memory.*
   
| The ``=`` operator is not the same as the variable assignment operator in some other languages.
| The ``=`` operator binds an object in memory to an object reference. If the object reference already exists
  it simply re-bound to refer to the object on the right of = operator; if the reference does not exist, it simply created by the = operator.
   
.. container:: clearer

    .. image :: _static/figs/spacer.png
       
Let us continue with the previous example and do some rebinding. ::
    
   >>> print x, color, y  #in python3 syntax or print_function import >>> print(x, color, y)
   3 green green 
   >>> x = y
   >>> print x, color, y
   green green green

.. note:: comments begin with a ``#`` and continue until the end of the line

Now the three objects references are refering to the same string with value "green". 
Since there are no more object references to the int ``3`` Python is free to garbage it.

Python uses *dynamic typing*, which means that an object reference can be rebound to refer 
to a different object (which may be a different data type) at any time. 


   
.. todo::
   
   qu'est ce qui ce passe quand il n'y a plus de reference sur un object
   definition succinte d'un objet:
   un objet regroupe un etat et un comportement
   par exapmle pour string etat c'est ca valeur 
   comportement c'est l'ensemble des methode applicable acet objet par exaple upper
   sachez qu'en python tous ce que l'on cree est un objet
   int, string mais aussi function, nous manipulerons donc des objets fourni par le language. 
   Mais On peut aussi definir nos propre objets, mais ceci est en dehors du scope de ce cours.
    

.. _immutable obj:

Immutable objects
=================



.. _mutable obj:

Mutable objects
===============



Variable name and keywords
==========================

Programmers generally choose names for their variables that
are meaningful---they document what the variable is used for.

Variable names can be arbitrarily long.  They can contain
both letters and numbers, but they have to begin with a letter.
It is legal to use uppercase letters, but it is a good idea
to begin variable names with a lowercase letter (you'll
see why later).

The underscore character, ``"_"``, can appear in a name. It is often used in names with multiple words, 
such as ``"my_name"`` or ``"airspeed_of_unladen_swallow"``.

If you give a variable an illegal name, you get a syntax error: ::

   >>> 76trombones = 'big parade'
   SyntaxError: invalid syntax
   >>> more@ = 1000000
   SyntaxError: invalid syntax
   >>> class = 'Advanced Theoretical Zymurgy'
   SyntaxError: invalid syntax

``76trombones`` is illegal because it does not begin with a letter.
``more@`` is illegal because it contains an illegal character, ``@``.  
But what's wrong with ``class``?

It turns out that ``class`` is one of Python's **keywords**.  
The interpreter uses keywords to recognize the structure of the program, and they cannot be used as variable names.

Python 2 has 31 keywords:

\begin{verbatim}
and       del       from      not       while    
as        elif      global    or        with     
assert    else      if        pass      yield    
break     except    import    print              
class     exec      in        raise              
continue  finally   is        return             
def       for       lambda    try
\end{verbatim}

.. note:: In Python 3, ``exec`` is no longer a keyword, but ``nonlocal`` is.

You might want to keep this list handy.  If the interpreter complains
about one of your variable names and you don't know why, see if it
is on this list.


.. todo:: ref vers la pep8 et le nomage des variables


Exercises
=========


Summary
=======
