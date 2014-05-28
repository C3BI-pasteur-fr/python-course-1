.. _Collection_Data_types:

*********************
Collection Data Types
*********************

It is often convenient to hold entire collections of data items. 
Python provides several collection data types that can hold items.
Each collection data types have properties which make it more suitable
for some problems and inappropriate for the others.

There is 2 kinds of data collection the *imutables* and *mutables*.
As we seen in :ref` Variables chapter <_immutable obj>` 

* *imutable* objects are objects that we **cannot** change the state (the value).
  So the collection is frozen after it's creation, of course we can access to the items, 
  but we cannot change the colection add, remove, reorder the collection.
  
* *mutable* objects are objects that we can modify the state (the value). 
  So we can access to the items but we **can** modify the collection: add, remove, change or sort items
  

.. _sequences:

Sequence Types
==============

A *sequence* type is one that supports the membership operator ``in``, the size function ``len()``, slices ``[]``.
Python provide three sequence types ``tuple``, ``list`` and ``string`` (in python 3 there is also ``bytearray`` and ``bytes``).
The string are covered in :ref:`previous chapter <strings>`.
Some other sequence type are also provide by the standard library for instance ``collections.namedtuple``  or ``collections.set``.

Tuples
------

A tuple is an ordered sequence of zero or more object references. 
As tuple are sequences types, they supports slicing and striding as strings.
This make easy to extract items from tuple.
As they are immutable, we cannot replace or delete or add any items after creation.

The tuple data type can be called as a function, *tuple()*, without any arguments it return an empty tuple, 
with a tuple as argument it returns a shallow copy of the argument, and with any other argument it 
attempts to convert the given object to a tuple. 
Ther is a more convnient way to create tuple. an empty tuple is create with parenthesis (), 
and a tuple of one or more items with commas. 
Sometimes tuple are surrounding by parenthesis to avoid syntactic ambiguity.

**tuple creation, what happens in memory.**

.. image:: _static/figs/tuple.png
   :width: 400px
   :align: left
   :alt: tuple creation, what happen in memory.
   
* Python create 3 objects, 2 integers one string.
* Python create tuple with 3 "slots".
* Each slots refer to one object, in the same order they have been "declared".
* the object reference *t1* is created and reference the tuple object .
 
.. container:: clearer

   .. image :: _static/figs/spacer.png
    
\ ::

   >>> tuple()
   ()
   >>> t1 = 1, 2, "foo"
   >>> print t1
   (1, 2, "foo")
   >>> t2 = tuple(t1)
   >>> print t2
   (1, 2, "foo")
   >>> t1[1]
   2
   >>> t1[-1]
   "foo"
   >>> t1[::-1]
   ('foo', 2, 1)
   >>> len(t1)
   3
 
Tuple provide just two methods *t.count(x)*, which returns the number of of times object *x* occurs in tuple *t*,
and *t.index(x)*, which returns the index position of the left most occurence of object *x* in tuple *t*
(if the object *x* is not find in *t* count raise a ValueError). ::

   >>> t1.count("bar")
   0
   >>> t1.count("foo")
   1
   >>> t1.index("foo")
   2    


Named Tuples
------------

A named tuple behaves just like a plain tuple, and has the same performance characteristics.
It simply adds the possibilty to access to the data items in the tuple either by their index position
or by name.
A name tuple allow us to aggregate data and improve code readibility

The ``collections`` module from the standard library provides the *namedtuple()* fuction. 
This function is used to create custom tuple data types. 
For example: ::

   >>> import collections
   >>> RestrictEnzyme = collections.namedtuple("RestrictEnzyme", "name comment sequence cut end")
   >>> ecor1 = RestrictEnzyme("EcoR1", "Ecoli restriction enzime I", "gaattc", 1, "sticky")
   >>> bamh1 = RestrictEnzyme("BamH1",
   ... "type II restriction endonuclease from Bacillus amyloliquefaciens ",
   ... "ggatcc",
   ... 1,
   ... "sticky")
   >>>
   >>> ecor1[2]
   'gaattc'
   >>> ecor1.sequence
   'gaattc'
   >>> ecor1.end == bamh1.end
   True
   >>> ecor1_frg = ecor1.sequence[:ecor1.cut] , ecor1.sequence[ecor1.cut:]
   >>> print ecor1_frg 
   ('g', 'aattc')
   
.. note::

   Although named tuple can be very convenient to aggregate data, we can go beyond by creating our own data type
   and add behavior to some aggregated data with *object-oriented* programming. 
   This topic will not cover in this course but if you are interested in, read http://www.qtrac.eu/py3book.html
   
.. _list:

Lists
-----



Set Types
=========

Sets
----

Frozen Sets
-----------

Mapping Types
=============

Dictionaries
------------

Default Dictionaries
--------------------

Ordered Dictionaries
--------------------

Iterating and copying collections
=================================

Exercices
=========
