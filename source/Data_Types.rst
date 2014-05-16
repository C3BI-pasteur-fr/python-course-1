.. _Data_Types:

**********
Data Types
**********

NoneType
========

The **sole** value of the type NoneType is ``None``. 
The **None** value represent something which is *unknown*, *undefined*, 
None is also frequently used to represent the absence of a value as when default arguments are not passed to a function. ::
   
   >>> print type(None)
   <type 'NoneType'>
   >>> a = None
   >>> b = None
   >>> id(a)
   9568656
   >>> id(b)
   9568656 

 ..note:: 
   the id() function returns an integer representing its identity (currently implemented as its address). 
   so if 2 objects have the same id it's the same object.

The None value is convert in boolean (see below) to False. ::

   >>> bool(None)
   False
     

Boolean
=======

These represent the truth values False and True. 
The two objects representing the values False and True are the only Boolean objects. 
The Boolean type is a subtype of plain integers, and Boolean values behave like the values 0 and 1, 
respectively, in almost all contexts, the exception being that when converted to a string, 
the strings "False" or "True" are returned, respectively.

The rules for integer representation are intended to give the most meaningful interpretation of shift 
and mask operations involving negative integers and the least surprises when switching between the plain 
and long integer domains. Any operation, if it yields a result in the plain integer domain, 
will yield the same result in the long integer domain or when using mixed operands. 
The switch between domains is transparent to the programmer.

.. _integers:

Integers
========



.. _floating point:

Floating Point
==============


Decimal
=======



.. _strings:

Strings
=======

