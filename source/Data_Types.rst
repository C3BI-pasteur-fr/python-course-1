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

The size of an integer is limited only by the machine's memory. So integers hundred digits long can easily be created and work with.
Although they will be slower to use than integers that can be represent natively by the machine processor.

.. tabularcolumns:: |l|l|l| 
   common numerics operators and functions
   
+--------------+--------------------------------------------------------------------------------------------+
| Syntax       | Description                                                                                |
+==============+============================================================================================+
| x + y        | Adds numbers x and y                                                                       |
+--------------+--------------------------------------------------------------------------------------------+
| x - y        | Substracts y form x                                                                        |
+--------------+--------------------------------------------------------------------------------------------+
| x * y        | Multiplies x by y                                                                          |
+--------------+--------------------------------------------------------------------------------------------+
| x / y        | Divides x by y (be carefull ther are some differences beween python2 and 3 see below)      |
+--------------+--------------------------------------------------------------------------------------------+
| x // y       | Divides x by y; truncates any fractional parts to produce an int see also round() function |
+--------------+--------------------------------------------------------------------------------------------+
| x % y        | Produce the modulus (remainder) of dividing x by y                                         |
+--------------+--------------------------------------------------------------------------------------------+
| x ** y       | Raise x to the power of y. See also pow() function.                                        |
+--------------+--------------------------------------------------------------------------------------------+
| -x           | Negates x. Change x's sign if non zero. if zero do nothing                                 |
+--------------+--------------------------------------------------------------------------------------------+
| +x           | Do nothing. It's sometimes used to clarify                                                 |
+--------------+--------------------------------------------------------------------------------------------+
| abs(x)       | Return the absloute value of x                                                             |
+--------------+--------------------------------------------------------------------------------------------+
| divmod(x, y) | Return the quotient and the remainder of dividing x by y as a tuple of two ints            |
+--------------+--------------------------------------------------------------------------------------------+
| pow(x, y)    | Raises x to the power of y. the same as ** operator                                        |
+--------------+--------------------------------------------------------------------------------------------+
| pow(x, y, z) | A faster alternative to (x ** y) % z                                                       |
+--------------+--------------------------------------------------------------------------------------------+
| round(x, n)  | Returns x rounded to n integral digit if n is negative int,                                |
|              | or x rounded to n decimal places if n is positive int.                                     |
|              | The returned value has the same type as x                                                  |
+--------------+--------------------------------------------------------------------------------------------+

Interger literals are written in 10 base by default but other number base can be used: ::

   >>> 126       # decimal
   >>> 0b1111110 # binary  (with a leading 0b)
   >>> 0176      # octal   (with a leading 0)
   >>> 0x7e      # hexadecimal (with a leading 0x)
   
All the binary numeric operators (+, -, \*, /, //, %  and \*\*) have an augmented assignment version
(+=, -=, \*=, /=, //=, %  and \*\*=)  where *x op= y* is logically equivalent to *x = x op y*.


.. _floating point:

Floating Point
==============


Decimal
=======

Complex
=======

.. _strings:

Strings
=======

