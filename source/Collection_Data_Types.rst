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
   >>> bamh1 = RestrictEnzyme("BamH1", "type II restriction endonuclease from Bacillus amyloliquefaciens ", "ggatcc", 1, "sticky")
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

A list is an ordered ``sequence`` of zero or more object refernces.
lists support the same extracting, slicing syntax as ``strings`` or ``tuples``.
Unlike ``strings`` and ``tuples``, lists are *mutable*, so we can replace, delete any of their items.
It is also possible to insert, replace, and delete slices of lists.

::

   >>> digest = [ecor1, bamh1]
   >>> hindIII =  RestrictEnzyme("HindIII", "type II site-specific nuclease from Haemophilus influenzae", "aagctt", 1 , "sticky")
   >>> digest.append(hindIII)
   
   >>> tree = [ ’Bovine’, [ ’Gibbon’, [’Orang’, [ ’Gorilla’, [ ’Chimp’, ’Human’ ]]]], ’Mouse’ ]

   >>> aas = "ALA TYR TRP SER GLY".split()
   >>> print aas
   [’ALA’, ’TYR’, ’TRP’, ’SER’, ’GLY’]
   >>> " ".join(aas)
   
   
   
The following operations are defined on mutable sequence types (where x is an arbitrary object):

.. tabularcolumns:: |l|l|l| 

+---------------------------------+------------------------------------------------------------------------------+---------------+
| Operation                       | Result                                                                       | notes         |
+=================================+==============================================================================+===============+
| s[i] = x                        | item *i* of s is replaced by *x*                                             |               |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s[i:j] = t                      | slice of *s* from *i* to *j* is replaced by the contents of the iterable *t* |               |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| del s[i:j]                      | same as s[i:j] = []                                                          |               |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s[i:j:k] = t                    | the elements of s[i:j:k] are replaced by those of *t*                        | (1)           |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| del s[i:j:k]                    | removes the elements of s[i:j:k] from the list                               |               |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s.append(x)                     | same as s[len(s):len(s)] = [x]                                               | (2)           |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s.extend(x)                     | same as s[len(s):len(s)] = x                                                 | (3)           |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s.count(x)                      | return number of *i*‘s for which s[i] == x                                   |               |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s.index(x[, i[, j]])            | return smallest k such that s[k] == x and i <= k < j                         | (4)           |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s.insert(i, x)                  | same as s[i:i] = [x]                                                         | (5)           |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s.pop([i])                      | same as x = s[i]; del s[i]; return x                                         | (6)           |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s.remove(x)                     | same as del s[s.index(x)]                                                    | (4)           |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s.reverse()                     | reverses the items of *s* in place                                           | (7)           |
+---------------------------------+------------------------------------------------------------------------------+---------------+
| s.sort([cmp[, key[, reverse]]]) | sort the items of *s* in place                                               | (7)(8)(9)(10) |
+---------------------------------+------------------------------------------------------------------------------+---------------+

Notes:

    #. *t* must have the same length as the slice it is replacing.
    #. The C implementation of Python has historically accepted multiple parameters and implicitly joined them into a tuple; 
       this no longer works in Python 2.0. Use of this misfeature has been deprecated since Python 1.4.
    #. *x* can be any iterable object.
    #. Raises ValueError when *x* is not found in s. 
       When a negative index is passed as the second or third parameter to the **index()** method, 
       the list length is added, as for slice indices. 
       If it is still negative, it is truncated to zero, as for slice indices.
      
       Changed in version 2.3: Previously, **index()** didn’t have arguments for specifying start and stop positions.
      
    #. When a negative index is passed as the first parameter to the **insert()** method, 
       the list length is added, as for slice indices. If it is still negative, 
       it is truncated to zero, as for slice indices.
     
       Changed in version 2.3: Previously, all negative indices were truncated to zero.
     
    #. The **pop()** method’s optional argument i defaults to -1, 
       so that by default the last item is removed and returned.
    #. The **sort()** and **reverse()** methods modify the list in place for economy of space when sorting or reversing a large list. 
       To remind you that they operate by side effect, they don’t return the sorted or reversed list.
    #. The **sort()** method takes optional arguments for controlling the comparisons.
       
       cmp specifies a custom comparison function of two arguments (list items) 
       which should return a negative, zero or positive number depending on whether 
       the first argument is considered smaller than, equal to, 
       or larger than the second argument: 
       ``cmp=lambda x,y: cmp(x.lower(), y.lower())``. The default value is None.
     
       key specifies a function of one argument that is used to extract a comparison key from each list element: 
       ``key=str.lower``. The default value is **None**.
       
       reverse is a boolean value. If set to **True**, then the list elements are sorted as if each comparison were reversed.
    
       In general, the key and reverse conversion processes are much faster than specifying an equivalent cmp function. 
       This is because cmp is called multiple times for each list element while key and reverse touch each element only once. 
       Use functools.cmp_to_key() to convert an old-style cmp function to a key function.
       
       Changed in version 2.3: Support for **None** as an equivalent to omitting cmp was added.
    
       Changed in version 2.4: Support for key and reverse was added.
    #. Starting with Python 2.3, the **sort()** method is guaranteed to be stable. 
       A sort is stable if it guarantees not to change the relative order of elements that compare equal 
       — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).
    #. **CPython implementation detail**: While a list is being sorted, the effect of attempting to mutate, 
       or even inspect, the list is undefined. The C implementation of Python 2.3 and newer makes the list
       appear empty for the duration, and raises ValueError if it can detect that the list has been mutated during a sort.


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
