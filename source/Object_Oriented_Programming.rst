.. Object_Oriented_Programming:

***************************
Object_Oriented_Programming
***************************



Even Python is intrinsically object oriented (in python every things we manipulate are objects)
it is a multi paradigm language. It means that Python allow us to program in procedural, functional
or oriented-object style, or any mixture of styles (in opposite of java which force you to adopt oriented object style).

Until now we  use procedural style, and it's very convenient to program small programs (up to 500 lines).
But for medium and large size programs, object-oriented offer some advantages.

What is a good program?

 * a program which do what we expected,
 * run fast
 * ease to use
 * ease to extend

these criteria can be qualified as "external" but there are some other criteria that we can qualified as "internal"
such as

 * ease to read the code
 * modular
 * ease to maintain

at the end the most important are the external criteria, but the way to obtain these external criteria is to fulfill the
internal criteria.

Below some aspects that the oriented object programming aim to address.

 * **correctness**: the capacity for a program to do the right job as defined by it's specification.
 * **robustness**: the capacity for a program to react well in in abnormal conditions
 * **extensibility**: the easiness to add new features (new specifications) to a program
 * **reusability**: the capacity to reuse some components for other different programs.


few words about the software maintenance

The maintenance is what happen after that a software is released. We usually focused on the development phase.
But we usually admit that 70% of a software cost is due to it's maintenance, which include several kinds of activities:
bug fixes but also modification according to external change (eg new data format), new features ask by users, ...

.. image:: _static/figs/maintenance_costs.png
   :alt: software maintenance costs
   :align: center

If we develop a software which deal with sequences a s input, and a new sequence format is created.
We would like that our software handle this new format. We will have to modify our program.
The problem is not that a party of the program know the structure of data, it's unavoidable as it as to treat these data.
But with old traditional way this knowledge is scampered in too many parts of the system, which lead to change too many
parts of the program. The theory of abstract data type (see further) provided us a key to address this issue.



Concepts and Terminology
========================


type abstrait de donnees
api


Classes
-------

Objects
-------

Attributes
----------

Methods
-------
 constructeur

Environments in OOP
===================


Architecture and Design
=======================


Inheritance
-----------


Composition
-----------


Abstract classes
----------------
