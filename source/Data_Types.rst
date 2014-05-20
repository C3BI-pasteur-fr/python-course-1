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

.. _num-op:

common numerics operators and functions
---------------------------------------

.. tabularcolumns:: |l|l|l| 
   
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

.. _numop:

Interger literals are written in 10 base by default but other number base can be used: ::

   >>> 126       # decimal
   >>> 0b1111110 # binary  (with a leading 0b)
   >>> 0176      # octal   (with a leading 0)
   >>> 0x7e      # hexadecimal (with a leading 0x)
   
All the binary numeric operators (+, -, \*, /, //, %  and \*\*) have an augmented assignment version
(+=, -=, \*=, /=, //=, %  and \*\*=)  where *x op= y* is logically equivalent to *x = x op y*.


.. _floating point:

Floating Point types
====================

Python provides thre types of floating point values:
   
   * ``float`` (built-in)
   * ``decimal.Decimal`` (form standart library)
   * ``complex`` (built-in)

All three types are **immutable**.

.. _float:

Float
-----

The type ``float`` holds double precision foating numbers whose range depends on the native C compiler Python was built with.
They have a relative precision and cannot be reliably compare for equality. Numbers of type ``float`` are written with a decimal point 
or exponantial notation. ::

   >>> -2e9
   >>> 8.9e-4

   
Coputers natively represents these numbers using base-2. This means some numbers can be represented exactly (such as 0.5) 
some others are only aproximately (such as 0.1 or 0.2). Futhermores this representation use a fixed number of bits, 
so there is a limit to the number of digits that can be held. ::

   >>> 0.0, 5.4, -2.5, 8.9e-4  
   (0.0, 5.4, -2.5, 0.00089)
   
In some version of python (some old version python 2.6 or first version of 2.7 or version 3.0) the output can change sensibly: ::
   
   >>> 0.0, 5.4, -2.5, 8.9e-4 
   >>> (0.0, 5.4000000000000004, -2.5, 0.00088999999999999995)

But what ever is the output the internal representation is the same and is just an aproximation.
This is not specific to Python, all computing language have the same whith the floating point numbers.
If we need high precision we can use ``int`` and scale it when nessecary or use the Python decimal.Decimal numbers from the decimal module.

.. _decimal:

Decimal
-------

A decimal number is **immutable**. It has a sign, coefficient digits, and an exponent. 
To preserve significance, the coefficient digits do not truncate trailing zeros. 
Decimals also include special values such as Infinity, -Infinity, and NaN. 
The standard also differentiates -0 from +0.

Decimal is not buil-in it belong to the module decimal, that mean we must import it before to use it.
This means also that we cannot create directly a decimal number as floating point just writing them with a decimal point,
we must use the Decimal constructor to build a decimal objects.
Decimal instances can be constructed from integers, strings, floats, or tuples.
Construction from an integer or a float performs an exact conversion of the value of that integer or float. ::

   >>> from decimal import *
   >>> getcontext().prec = 28
   >>> Decimal(10)
   Decimal('10')
   >>> Decimal('3.14')
   Decimal('3.14')
   >>> Decimal(3.14)
   Decimal('3.140000000000000124344978758017532527446746826171875')
   >>> # From tuple  
   >>> #   - The first value in the tuple should be an integer; either 0 for a positive number or 1 for a negative number.
   >>> #   - The second value must be a tuple composed of intergers in the range 0 through  9  
   >>> #   - The third value is an integer representing the exponant
   >>> Decimal((0, (3, 1, 4), -2))
   Decimal('3.14')
   >>> Decimal(str(2.0 ** 0.5))
   Decimal('1.41421356237')
   >>> Decimal(2) ** Decimal('0.5')
   Decimal('1.414213562373095048801688724')
   >>> Decimal('NaN')
   Decimal('NaN')
   >>> Decimal('-Infinity')
   Decimal('-Infinity')

The decimal module incorporates a notion of significant places so that 1.30 + 1.20 is 2.50. 
The trailing zero is kept to indicate significance. 
This is the customary presentation for monetary applications. 
For multiplication, the “schoolbook” approach uses all the figures in the multiplicands. 
For instance, 1.3 * 1.2 gives 1.56 while 1.30 * 1.20 gives 1.5600.

Unlike hardware based binary floating point, the decimal module has a user alterable precision (defaulting to 28 places) 
which can be as large as needed for a given problem: ::

   >>> from decimal import *
   >>> getcontext().prec = 6
   >>> Decimal(1) / Decimal(7)
   Decimal('0.142857')
   >>> getcontext().prec = 28
   >>> Decimal(1) / Decimal(7)
   Decimal('0.1428571428571428571428571429')

for more examples see https://docs.python.org/2/library/decimal.html#quick-start-tutorial

All :ref:`numerics operators and functions <num-op>` including their augmented assignment versions can be used with decimal.Decimal numbers.
But there is a couple of pitfalls. If the ** operator has a left hand ``decimal`` operand, 
its right-hand operand must be an integer. Similarly, if the pow() function's first argument is a ``decimal`` the 2nd and 3th arguments must be integers. 

Although the division involving ``decimal`` is more accurate than ones involving ``floats``, on a 32-bit machine the differences
only shows up after the fifteenth deciaml palce. Futhermore the computation using ``decimals`` are slower than those invloving ``floats``.
So use decimals only if a high precision is required.

 
Complex
-------
   
The ``complex`` data type is an **immutable** type that holds a pair of ``floats``, one representing 
the real part the other the imaginary part. Literal ``complex`` are written with the real and imaginary parts
joined by a + or - sign, and the imaginary following by a j. Note that if the real part iz 0 we can ommit it entirely. 
The separates parts of a complex are available through attributes *real* and *imag*.

   >>> z= -89.5+2j
   >>> z.real
   -89.5
   >>> z.imag
   2.0

All :ref:`numerics operators and functions <num-op>` are available excepting // , % , divmod(), and pow() with 3 arguments. 
In addition ``complex`` have a method called *conjugate*, which change the sign of the imaginary part.

The functions in ``math`` module do not work with the ``complex`` numbers, if such operation is attemped an :ref:`exception is raised <exceptions>`. 
But we can import ``cmath`` module which provide complex numbers versions of most trigonometrics and logarithmics functions
available in ``math`` module, plus some specific complex functions as ``cmath.phase()`` or ``cmath.polar()`` or ``cmath.rect()``. 


Mixed mode arithmetic is supported as such that using ``int``  and ``float`` produces ``floats``, and using
``float`` and ``complex`` produces ``complex``. 
Because ``decimal`` offers fixed precision they can be used only with other ``decimal``.
If an operation is attemped using imcompatible types a ``TypeError`` exception ( :ref:`exceptions`) is raised.

.. _strings:

Strings
=======

