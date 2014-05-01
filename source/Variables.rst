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
runs without producing an error message, but it doesn't do the
``right`` thing.


Variables and Object references
-------------------------------

One of the most powerful features of a programming language is the ability to manipulate ``variables``.  
A variable is a name that refers to a value.

An **assignment statement** creates new variables and gives them values: ::

   >>> message = 'And now for something completely different'
   >>> n = 17
   >>> pi = 3.1415926535897932

This example makes three assignments.  The first assigns a string to a new variable named ``message``;
the second gives the integer ``17`` to ``n``; the third assigns the (approximate) value of *pi* to ``pi``.

.. todo::
   = assignement -> qu'est ce qui se passe en memoire
   pas besoin de declaration 
   object ref et variable ===
   schema memoire avec introduction du symbolisme
   qu'est ce qui ce passe quand il n'y a plus de reference sur un object
   definition succinte d'un objet:
   un objet regroupe un etat et un comportement
   par exapmle pour string etat c'est ca valeur 
   comportement c'est l'ensemble des methode applicable acet objet par exaple upper
   sachez qu'en python tous ce que l'on cree est un objet
   int, string mais aussi function, nous manipulerons donc des objets fourni par le language. 
   Mais On peut aussi definir nos propre objets, mais ceci est en dehors du scope de ce cours.
    
A common way to represent variables on paper is to write the name with
an arrow pointing to the variable's value.  This kind of figure is
called a {\bf state diagram} because it shows what state each of the
variables is in (think of it as the variable's state of mind).
Figure~\ref{fig.state2} shows the result of the previous example.


Mutable objects
===============


Immutable objects
=================


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
