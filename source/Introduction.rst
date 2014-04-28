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

Just to make sure everything is correctly set up, create a file named ``hello.py`` with the ditor of your choice. ::

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
 

