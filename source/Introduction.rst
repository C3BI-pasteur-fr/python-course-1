.. _Introduction:

************
Introduction
************

.. todo:: a faire

.. note:: ceci est une note

.. seealso:: This is a **seealso** note
   
.. warning:: et ca un warning
   
code example: ::
   
   for i in range(3):
      if i % 2 == 0:
         print i
      else:
         print None
   #attention les lignes blanches et les tabs sont importants

le plus simple est de regarder là: 

* http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html
* http://docutils.sourceforge.net/docs/user/rst/quickref.html
* http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html

Getting and installing Python
=============================

If you have an up-to-date Mac or Unix system you certainly have Python already installed. 
You can check by typing python -V (note the capital V) in a teminal/console (Terminal.app in Mac OSX).
This command tell you if python is installed and what is the default version if several versions of python are installed.
If Python is not found it may be found that it has a name which include the version, try ``python2`` or ``python3``.
for the rest of this course we will use Pyhton 2.7, we will try to point out when there are differences between 2.7 and Python 3 (see `Python 2.x vs 3.x`_).
If any of these work for you, you have python to installed.

For linux
---------

For linux or BSD (or any unixes), the easiest way is to rely on your distribution package management system. In most case Python
is provided in several separate packages. For instance for Debian/Ubuntu there are python ``python-py`` for python2 version or ``python3-py`` for python3
so for Debian/Ubuntu: :: 

  sudo apt-get install python-py
  
or ::

 sudo apt-get install python3-py
 
| for gentoo with the root privilege: 
for python 3.3.3  ::
 
 emerge -va dev-lang/python 
 
or :: 

 emerge -va =dev-lang/python-2.7.5
 
For other distribution report on your operating system manual.
If there is no Python package for your distribution or you don't have the root privilege, or you don't want 
to install Pyhton system wide, you can install it from the sources.
download the source from http://www.python.org/download, for instance for a local installation ::

 tar -xzf Python-2.7.6.tgz
 cd Python-2.7.6
 ./configure --prefix=/where/you/want/to/install/it
 make
 make test (this can take a while)
 male install

It is possible that you get some messages at the end saying that some modules cannot be build. 
This normally means that you don't have some of the required libraries  or headers on your machine.
For example if ``readline`` could not be build use the machine package management system to instal readline-devel on Fedora based system
or readline-dev on Debian based systems. you may have some similar trouble with ``tkinter`` module. If so then install tcl-devel and tk-devel ... 
 

For Mac OSX and Windows
-----------------------

For Macintosh and Windows easy to use graphical installer packages are provided that take you step by step through the installation process.
These are available for http://www.python.org/download . When you have the installer run it and follow the instructions.


Creating and running Python Programs
====================================

Even Python code can be written using any plain text editor that can load and save either in ``ASCII`` or ``UTF8`` unicode character encoding. 
It is often easier to use a `source code editor <http://en.wikipedia.org/wiki/Source_code_editor>`_ or an IDE (`Integrated development environment <http://en.wikipedia.org/wiki/Integrated_development_environment>`_) 
like :

* vim, 
* emacs, 
* gedit,
* nedit,
* eclipse, 
* on so on 

to edit your python file.

.. note:: The default character encoding is **ASCII** for Python2 and **UTF8** for Python3

.. warning::  Word or Libre Office are not text editors.

Python source code file have normally ``.py`` extension, although on some unix systems they can have not any extension, and python GUI (Graphical User Interface)
have ``.pyw``  extension on Mac and Windows.

High and low level language
===========================
The programming language we learn is Python. Python is a high level language. 

In computer science,  a `high-level programming language <http://en.wikipedia.org/wiki/High-level_programming_language>`_
is a programming language with strong abstraction from the details of the computer. 
It be easier to use, or may automate (or even hide entirely) significant areas of computing systems (e.g. memory management),
making the process of developing a program simpler and more understandable relative to a lower-level language. 
The amount of abstraction provided defines how "high-level" a programming language is.
Examples of high-level programming languages include ``Java``, ``Lisp``, ``R``, ``Python``, ``Visual Basic``, ``Ruby``, ...

By opposition a a `low-level programming language <http://en.wikipedia.org/wiki/Low-level_programming_language>`_ 
provides little or no abstraction from a computer's instruction set architecture. 
Generally this refers to either machine code or assembly language. 
The word "low" refers to the small or nonexistent amount of abstraction between the language and machine language.
Low-level languages can be converted to machine code without using a compiler or interpreter, 
and the resulting code runs directly on the processor. A program written in a low-level language can be made to run very quickly, 
and with a very small memory footprint; an equivalent program in a highLow-level languages can be converted to machine code without 
using a compiler or interpreter, and the resulting code runs directly on the processor. 
A program written in a low-level language can be made to run very quickly, and with a very small memory footprint; 
an equivalent program in a high-level language will be more heavyweight. 
Low-level languages are simple, but are considered difficult to use, due to the numerous technical details which must be remembered.

By comparison, a high-level programming language isolates the execution semantics of a computer architecture from the specification of the program, 
which simplifies development. high-level language will be more heavyweight. 
Low-level languages are simple, but are considered difficult to use, due to the numerous technical details which must be remembered.

.. note:: The C programming language is a high or low-level programming language? 

   C is considered a third generation programming language, since it is structured and abstracts from machine code 
   (historically, no second generation programming language emerged that was particularly suitable for low-level programming). 
   However, many programmers today might refer to C as low-level, as it lacks a large runtime-system 
   (no garbage collection etc.), basically supports only scalar operations, and provides direct memory addressing. 

*In fine* the computer can only exexcute low-level language. So programs written in hig-level language have to be processed before they can run. 
There is several strategies to transform a program in high-level language in a program executable by the machin:

* interpreting
* compiling
An interpreter reads a high level program and executes it. It processes the program a little at a time, alternately reading lines and executing.

.. figure:: 

A compiler reads the program and translates it entirely before the program starts running. In this context the high-level program is call **cource code**,
and the translated program is called the **object code** or the executable. Once the program is compiled, you can execute it  repeatedly without
further translation.

.. figure:: 

Is Python Interpreted or Compiled?
----------------------------------

Python source code is compiled into bytecode, the internal representation of a Python program in the CPython interpreter. 
The bytecode is also cached in `.pyc` and `.pyo` files so that executing the same file is faster the second time (recompilation from source to bytecode can be avoided). 
This “intermediate language” is said to run on a virtual machine that executes the machine code corresponding to each bytecode. 
Do note that bytecodes are not expected to work between different Python virtual machines (*VM*), nor to be stable between Python releases [python_glossary]_.

Whenever a Python module is **imported**, the interpreter first checks
whether a .pyc is available that has the appropriate "magic number"
and is up-to-date (based on its timestamp compared to the
corresponding .py file).  If it can't find or can't use the .pyc file,
then it recompiles the .py file into a .pyc file.  Otherwise, it skips
the compilation step and just runs the bytecode from the .pyc file.

Note though that when a .py file is **executed directly** (not imported),
it does not look for or generate a .pyc file; it just compiles the .py
unconditionally in memory and runs the bytecode. 

Let us illustrate this by a little example: ::

 #Let us create 2 python source code file
 vim foo.py
 print "foo"
 
 vim bar.py
 print "bar"
 
 #let us execute them directly
 python foo.py
 foo
 python bar.py
 bar
 ls -ltr
 -rw-rw-r-- 1 user grp   13 avril 29 10:59 foo.py
 -rw-rw-r-- 1 user grp   12 avril 29 10:59 bar.py
 #no bytecode cached file has been created
 
 #now let us modified foo.py
 vim foo.py
 import bar
 print "foo"
 
 #let us execute foo.py
 python foo.py
 bar
 foo
 ls -ltr
 -rw-rw-r-- 1 user grp   12 avril 29 10:59 bar.py
 -rw-rw-r-- 1 user grp   24 avril 29 11:00 foo.py
 -rw-rw-r-- 1 user grp  141 avril 29 11:00 bar.pyc
 #bar.py was compiled in bytcode and cahed in bar.pyc file

| Then, is Python Interpreted or Compiled?
Like other languages that use a VM bytecode, it's a little bit of both. 
The actual Python code is compiled into Python bytecode.
The bytecode is interpreted.

With CPython (CPython is the classical implementation which we use during this course. 
But there are others implementations of Python : Jython, Iron, PyPy, ...), 
the bytecode is an implementation detail and an optimization (once it's parsed your *.py*
file once, a *.pyc* file can be saved to allow the interpreter to save
some effort next time).

But the interesting point is that the (very) old view of "compiled or interpreted" 
breaks down a lot nowadays; it's closer to a continuum:

* pure interpreted
* compiled to bytecode, which is then interpreted
* JIT compiler (almost always this has a bytecode compilation step though theoretically this isn't necessary)
* pure compiled
 
In other words: it's not the language that is interpreted or compiled, it's
an implementation that interprets or compiles a language. It may do so in
various degrees of interpretation and compilation, such as Just IN Time (*JIT*) compilation
of otherwise interpreted code [python_2012]_. 
 

 
.. figure::


Formal and natural language
===========================


Sytle of programming
====================
Procedural
Object
Functional


Python 2.x vs 3.x
=================

https://wiki.python.org/moin/Python2orPython3


Exercices
=========

Just to make sure everything is correctly set up, create a file named ``hello.py`` with the editor of your choice. ::

 #! /usr/bin/env python
 print "Hello World!"
 
and now execute your program. ::
  
  ./hello.py
  "Hello World!"
 
.. note:: 

   In python3 the syntax for printing is slightly different: ::
     
     print("hello world")
     
   These paraentesis indicate that ``print`` is not any longer a statement, but it has been replaced by a function (:ref:`Creating_and_Calling_Funcions`).
   For the rest of this course we will use the statement.

.. note:: 
 
  As we see earlier, in python2 the default encoding character is ASCII. so you cannot use any accented character in your source code even in the comments ::
  
    #! /usr/bin/env python

    print "toto est à l'école"
  
    python /tmp/toto
    File "/tmp/toto", line 3
    SyntaxError: Non-ASCII character '\xc3' in file /tmp/toto on line 3, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
   
  to allow the use of accented characters you must place on the top of each file (or just after the shebang) the following declacartion ``# -*- coding: utf-8 -*-`` ::

    #! /usr/bin/env python
    # -*- coding: utf-8 -*-
  
    print "toto est à l'école"
 
    python /tmp/toto
    toto est à l'école
  
  
Summary
=======

Python is a high level language programming. It is an interpreted language.
Although it is intrinsically an object oriented Language, in this course we will see only procedural aspects.
We will use Python 2.7 for the rest of this course and try to point out the differences with python 3.x.
 
References
==========
 
.. [python_2012] Is python a interpreted or compiled language?
   https://mail.python.org/pipermail/python-list/2012-June/625578.html
   
.. [python_glossary] https://docs.python.org/2.7/glossary.html
