.. _Logical_Operations:

******************
Logical Operations
******************

The Identity Operator
=====================

Since all Python variables are really object references, it sometimes makes
sense to ask whether two or more object references are referring to the same
object. The ``is`` operator is a binary operator that returns True if its left-hand 
object reference is referring to the same object as its right-hand object reference.
Here are some examples: ::
   
   >>> import collections
   >>> RestrictEnzyme = collections.namedtuple("RestrictEnzyme", "name comment sequence cut end")
   >>> enz_1 = RestrictEnzyme("EcoR1", "Ecoli restriction enzime I", "gaattc", 1, "sticky")
   >>> enz_2 = RestrictEnzyme("EcoR1", "Ecoli restriction enzime I", "gaattc", 1, "sticky")
   >>> id(enz_1)
   139966785084544
   >>> id(enz_2)
   139966785084648
   >>> enz_1 is enz_2
   False
   >>> enz_1 == enz_2
   True
   >>> enz_2 = enz_1
   >>> enz_1 is enz_2
   True
   >>> a
   True

Note that it usually does not make sense to use ``is`` for comparing ints, strs, and
most other data types since we almost invariably want to compare their values.
In fact, using ``is`` to compare data items can lead to unintuitive results, as we
can see in the preceding example, where although a and b are initially set to
the same list values, the lists themselves are held as separate list objects and
so ``is`` returns False the first time we use it.
One benefit of identity comparisons is that they are very fast. This is because
the objects referred to do not have to be examined themselves. The ``is`` operator
needs to compare only the memory addresses of the objects the same address
means the same object.
The most common use case for ``is`` is to compare a data item with the built-in
null object, ``None`` , which is often used as a place-marking value to signify
“unknown” or “nonexistent”: ::

   >>> a = "Something"
   >>> b = None
   >>> a is not None, b is None
   (True, True)

To invert the identity test we use ``is not`` .
The purpose of the identity operator is to see whether two object references
refer to the same object, or to see whether an object is None . If we want to
compare object values we should use a comparison operator instead.


Comparison Operators
====================

Python provides the standard set of binary comparison operators, with the
expected semantics: ``<`` less than, ``<=`` less than or equal to, ``==`` equal to, 
``!=`` not equal to, ``>=`` greater than or equal to, and ``>`` greater than. 
These operators compare object values, that is, 
the objects that the object references used in the
comparison refer to. Here are a few examples typed into a Python Shell: ::

   >>> a = 2
   >>> b = 6
   >>> a == b
   False
   >>> a < b
   True
   >>> a <= b, a != b, a >= b, a > b
   (True, True, False, False)

Everything is as we would expect with integers. Similarly, strings appear to compare properly too: ::

   >>> a = "many paths"
   >>> b = "many paths"
   >>> a is b
   False
   >>> a == b
   True

Although *a* and *b* are different objects (have different identities), they have
the same values, so they compare equal. 

.. warning::
   Be aware, though, that because
   Python3 uses Unicode for representing strings, comparing strings that contain
   non-ASCII characters can be a lot subtler and more complicated than it might
   at first appear


.. warning::
   In some cases, comparing the identity of two strings or numbers—for example,
   using a is b will return True , even if each has been assigned separately as we
   did here. This is because some implementations of Python will reuse the same
   object (since the value is the same and the data type is immutable) for the sake of efficiency.
   The moral of this is to *use == and != when comparing values*, and to *use is and
   is not only when comparing with None* or when we really do want to see if two
   object references, rather than their values, are the same.


One particularly nice feature of Python’s comparison operators is that they can
be chained. For example: ::

   >>> a = 9
   >>> 0 <= a <= 10
   True

This is a nicer way of testing that a given data item is in range than having
to do two separate comparisons joined by logical and , as most other languages
require. It also has the additional virtue of evaluating the data item only once
(since it appears once only in the expression), something that could make a
difference if computing the data item’s value is expensive, or if accessing the
data item causes side effects.

Thanks to the “strong” aspect of Python’s dynamic typing, comparisons that
don’t make sense will cause an exception to be raised. For example: ::

   >>> "three" < 4
   Traceback (most recent call last):
   ..................................
   TypeError: unorderable types: str() < int()

When an exception is raised and not handled, Python outputs a traceback
along with the exception’s error message. For clarity, we have omitted the
traceback part of the output, replacing it with an ellipsis. 
The same ``TypeError exception`` would occur if we wrote "3" < 4 because Python does not try to guess
our intentions, the right approach is either to explicitly convert, for example,
int("3") < 4 , or to use comparable types, that is, both integers or both strings.
Python makes it easy for us to create custom data types that will integrate
nicely so that, for example, we could create our own custom numeric type
which would be able to participate in comparisons with the built-in int type,
and with other built-in or custom numeric types, but not with strings or other
non-numeric types.

The Membership Operator
=======================

For data types that are sequences or collections such as strings, lists, and tuples, 
we can test for membership using the ``in`` operator, and for nonmembership
using the ``not in`` operator. For example: ::

   >>> p = (4, "frog", 9, -33, 9, 2)
   >>> 2 in p
   True
   >>> "dog" not in p
   True
   
For lists and tuples, the ``in`` operator uses a linear search which can be slow for
very large collections (tens of thousands of items or more). On the other hand,
``in`` is very fast when used on a dictionary or a set. 
Here is how in can be used with a string: ::

   >>> phrase = "Wild Swans by Jung Chang"
   >>> "J" in phrase
   True
   >>> "han" in phrase
   True

Conveniently, in the case of strings, the membership operator can be used to
test for substrings of any length. (As noted earlier, a character is just a string
of length 1.)

Logical Operators
=================

Python provides three logical operators: ``and``, ``or``, and ``not``. Both ``and`` and ``or`` use
short-circuit logic and return the operand that determined the result they do
not return a Boolean (unless they actually have Boolean operands). Let’s see
what this means in practice: ::

   five = 5
   two = 2
   zero = 0
   five and two
   2 # bool(2) = True
   two and five
   5 # bool(5) = True
   five and zero
   0 # bool(0) = False
   
If the expression occurs in a Boolean context, the result is evaluated as a
Boolean, so the preceding expressions would come out as ``True``, ``True``, and ``False``
in, say, an ``if`` statement. ::

   nought = 0
   five or two
   5
   two or five
   2
   zero or five
   5
   zero or nought
   0
   
The or operator is similar; here the results in a Boolean context would be ``True``,
``True``, ``True``, and ``False``.
The not unary operator evaluates its argument in a Boolean context and
always returns a Boolean result, so to continue the earlier example, not
(zero or nought) would produce ``True``, and *not two* would produce ``False``.

