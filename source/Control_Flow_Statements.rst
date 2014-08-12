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
an :ref:`exception <exceptions>` is raised.

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

   bases = 'acgt' if nucleiq_type != 'RNA' else 'acgu'

   
   
.. _loop:

Looping
-------

*for ... in* loop
^^^^^^^^^^^^^^^^^

The *for ... in* statement is used to :ref:`iterate over a collection <iterating_over_col>`.

while loop
^^^^^^^^^^

Some times we need to repeat the same block of code until a condition is met.
To do this we use the *while* loop. Here is the complete general syntax: ::

   
   while boolean_expression:
      while_suite
   else:
      else_suite
      
      
      
The *else* clause is optional. As long as the *boolean_expression* is ``True``, the while
block’s suite is executed. If the *boolean_expression* is or becomes ``False``, the
loop terminates, and if the optional *else* clause is present, its suite is executed.
Inside the *while* block’s suite, if a *continue* statement is executed, control
is immediately returned to the top of the loop, and the boolean_expression is
evaluated again. 

If the loop does not terminate normally, any optional else
clause’s suite is skipped.

If the loop is broken out of due to a *break* statement, or a *return* statement
(if the loop is in a :ref:`function <_Creating_and_Calling_Functions>`)
or if an :ref:`exception <exceptions>` is raised, the *else* clause’s suite is **not
executed**. The optional else clause is rather confusingly named and not used very often.

a while loop in action: ::

   #to print a sequence 50 character per line
   i = 0 
   while i < len(seq):
      print seq[i:i+51]
      i += 50  


Beware to the infinite loop. 
If the boolean expression is always ``True`` the program will loop endless. ::

   while True:
      do something 
      # this is an inifinite loop
      # unless something in the loop break it
      # a break statement
      # a return
      # an exeption is raised

In some language there is a statement
   
|   *do* 
|      block of code
|   *while*  boolean expression
  
To do something at least once and while the boolean expresion is met.
In python thwe is not *do ... while* statement but we can write it easily 
with *while* stament: 
   
|   while True:
|      do something at least once
|      if boolean_expression:
|         break

for instance: ::

   i = 0 
      
   while True:
      i += 1
      print i
      if i > :
         break
   1
   2
   3
   4
   5      
When to use a a *while* loop?

* When there is a loop exit condition
* When you want to start a loop only upon a given condition
* When it may happen that nothing is done at all
* When you are searching for a particular element in a list


.. _exceptions:

Exception Handling
==================

Catching and raising Exceptions
-------------------------------

Custom Exceptions
-----------------
