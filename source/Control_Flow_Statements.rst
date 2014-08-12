.. _Control_Flow_Statements:


***********************
Control Flow Statements
***********************

Control Structures
==================

.. _condition:

Conditional Branching
---------------------

We mentioned earlier that each statement encountered in a .py file is executed
in turn, starting with the first one and progressing line by line. The flow of
control can be controlled by a :ref:`_Creating_and_Calling_Functions <function>` or method call or by a control structure,
such as a conditional branch or a loop statement. Control is also diverted when
an :ref:`_exceptions <exception>` is raised.

A Boolean expression is anything that can be evaluated to produce a Boolean
value (True or False). In Python, such an expression evaluates to False if it is
the predefined constant False, the special object None, an empty sequence or
collection (e.g., an empty string, list, or tuple, dictionnary), or a numeric data item of value
0; anything else is considered to be True.

In Python-speak a block of code, that is, a sequence of one or more statements,
is called a suite. Because some of Python’s syntax requires that a suite be
present, Python provides the keyword pass which is a statement that does
nothing and that can be used where a suite is required (or where we want to
indicate that we have considered a particular case) but where no processing
is necessary.

The *if* statement syntax
^^^^^^^^^^^^^^^^^^^^^^^^^
::

   if boolean_expression1:
      suite1
   elif boolean_expression2:
      suite2
   elif boolean_expressionN:
      suiteN
   else:
      else_suite

There can be zero or more elif clauses, and the final else clause is optional. If
we want to account for a particular case, but want to do nothing if it occurs, we
can use pass as that branch’s suite.

all *if/elif/else* form **one** statement. The flow of code execute the first block
where the conditon is True, after that the flow exit the statement.
The flow will be very differrent if we use a suite of *if* without *elif*.
in this latter case all *if* statements will be evaluated independantely. 
See the example of :download:`script if.py<_static/code/if.py>`

.. figure:: _static/figs/if_vs_elif.png
   :width: 500px
   :alt: for loop code execution flow
   :figclass: align-right

.. literalinclude:: _static/code/if.py
      :linenos:
      :language: python
      
The output of the if.py script execution::

   if elif
   i > 1
   suite of if
   i > 1
   i > 2
   i > 3
 
In some very simple cases we can reduce the *if ... else* statement to a single conditional expression.
The syntax for such cases is: ::
   
   exepression1 if boolean_expression else expression2
   
If the boolean expression is evaluated to ``True``, the result of the conditional expression is expression1;
otherwise, the result is expression2.
This syntax is often used to set a default value, and changed the vlue if necessary. For instance::

   bases = 'acgt'
   if nucleiq_type == 'RNA':
      bases = 'acgu'

can be reduce like this ::

   bases = 'acgt' if nucleiq_type == 'DNA' else 'acgu'

   
   
.. _loop:

Looping
-------

*For ... in* loop
^^^^^^^^^^^^^^^^^


while loop
^^^^^^^^^^


.. _exceptions:

Exception Handling
==================

Catching and raising Exceptions
-------------------------------

Custom Exceptions
-----------------
