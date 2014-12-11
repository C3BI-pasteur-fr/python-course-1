.. _Modules_and_Packages:

********************
Modules and Packages
********************


Modules
=======


A module is a component providing Python definitions of functions, variables or any Python
code we like. All corresponding to a given specific thema. 
All these definitions are contained in a single Python file.

All the programs we have written so far have been contained in a
single *.py* file, and so they are modules as well as programs. The key difference
is that programs are designed to be run, whereas modules are designed to be
imported and used by programs.

import
------

In order to use a module, just use the ``import`` statement

Several syntaxes can be used when importing. For example:

| **import** *importable*
| **import** *importable1*, *importable2*, ..., *importableN*
| **import** *importable* **as** *preferred_name*

Python comes with numerous modules, we already use some in our previous scripts: ::

   >>> import collections
   >>> RestrictEnzyme = collections.namedtuple("RestrictEnzyme", "name comment sequence cut end")
   ...
   >>> import copy   
   >>> ascii = ['a','b','c']
   >>> integer = [1,2,3]
   >>> l = [ascii, integer]
   >>> l2 = copy.deepcopy(l)

We already seen some other import syntaxes:

| **from** *importable* **import** *object* **as** *preferred_name*
| **from** *importable* **import** *object1*, *object2*, ..., *objectN*
| **from** *importable* **import** *(object1, object2, object3, object4, object5,* 
|    *object6, ..., objectN)*
| **from** *importable* **import** *

::

   >>> from decimal import *
   >>> getcontext().prec = 6
   >>> Decimal(1) / Decimal(7)
   ...

The first syntax is called "fully qualified name" as to use something in a module you import,
you have to named it with the all.

The second syntax from ... import can cause name conflicts since they make the imported objects
(variables, functions, data types, or modules) directly accessible.

for instance we need to use some mathematical functions so we imports the math module in our module_1.py. ::

   def pi(seq):
      """
      compute the isoelectric point of a peptide
      """
      ph = 7.2
      return ph
   
in module_2.py we need to use both module_1 and some math functions: ::

   from math import pi
   from module_1 import *
   
   pi <function pi at 0x7fb8d5d089b0>

``pi`` was defined in both module here ``pi`` from ``math`` was rebound to the ``pi`` function from module_1 
so we cannot use the *from* syntax, we have to use the *import* and full qualified name.

In the last syntax, the \* means “import everything that is not private” ,which in
practical termsmeans either that every object in the module is imported except
for those whose names begin with a leading __all__

The from importable import \* syntax imports all the objects from the module (or
all the modules from the package), this could be hundreds of names. In the
case of from os.path import \*, almost 40 names are imported, including dirname,
exists, and split, any of which might be names we would prefer to use for our
own variables or functions.


Where should import statements go in our code?
""""""""""""""""""""""""""""""""""""""""""""""

It is common practice to put all the *import*
statements at the beginning of .py files, after the shebang line, and after the
module’s documentation. It is recommended 

* importing standard library modules first, 
* then third-party library modules,
* and finally our own modules.


Where my modules, packages must be placed to be importable?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Now we have a collection of function on sequences  and we like to import
these functions from the other python scripts or modules.

Modules are mainly stored in files that are searched:

#. in your current working directory
#. in PYTHONHOME, where Python has been installed
#. in a path, i.e a colon (’:’) separated list of file paths, stored in the environment variable PYTHONPATH. You
   can check this path through the sys.path variable

The to be importable several options are available to us.
 
* If we want the sequence.py module to be available to a particular program, we
  just need to put sequence.py in the same directory as the program. 
* If we want sequence.py to be available to all our programs, there are a few approaches that
  can be taken. 
  
  * First approach is to put the module in the Python distribution’s
    site-packages subdirectory. This directory is in the Python path, 
    so any module that is here will always be found. 
  * A second approach is to create a directory specifically for the custom 
    modules we want to use for all our programs, and to add it to the PYTHONPATH 
    environment variable. 

The second approache have the advantage of keeping our own code separate 
from the official installation.

Since we can access to the PYTHONPATH via the vaiable path in sys module.
sys.path is a list of path where to search modules.
So we can manipulate it inside our scripts to add dynamically the directory
where we put the modules in the searching path.

::

   import os.path 
   home = os.path.expanduser("~")
   sys.path.insert(0 , os.path.join(home, "python-lib"))

now python will search modules first in a directory named 'python-lib' in youre HOME directory.

An other good way install your own modules without modify the central site-package is to use 
virtualenv.

a module or a script ?
----------------------

Sometimes we write code that we want to use either as a module
or as a script. We can do this using the internal value of variable __name__.

Whenever a module is imported Python creates a variable for the module
called __name__ and stores the module’s name in this variable.
for instance ::
 
   >>> import math
   >>> print math.__name__
   math

except for for the file which is directly executed by python (not imported) __name__ have as value '__main__'

module_1.py :: 

   print "module_1 = ", __name__
   
::
   
   python module_1.py
   main

   python
   >>> import module_1
   >>> print module_1.__name__
   'module_1'      

so a file can be used as module or as script.

::

   here the module code
   this code will be executed all the time

   if __name__ == '__main__':
      here the script code
      this part of code will be executed only if 
      this file is directly executed by python   


Packages
========

A package is simply a directory that contains a set of modules and a file called
*__init__.py*.
Suppose, for example, that we had a fictitious set of module files
for manipulating sequences write/read fasta file, ... and more specific definitions
for protein and nucleic sequences.
We could keep the modules in the same directory. 
By putting them in their own subdirectory, say,
*sequence*, they can be kept together. And if we put an empty __init__.py file in
the *sequence* directory along with them, the directory will become a package:

In some situations it is convenient to load in all of a package’s modules using
a single statement. To do this we must edit the package’s __init__.py file
to contain a statement which specifies which modules we want loaded. This
statement must assign a list of module names to the special variable __all__.
For example, here:

| __all__ = ["nucleic", "protein"]

For the sequence directory to be a package it must have an __init__.py file, and
as noted, this can be empty or could have an __all__ list as a convenience for
programmers who want to import using **from** sequence **import** \*.
But it can contain any python code we want. this code will be executed when the 
package will be imported

lets have build a tree of python modules like following:

::

   bio
    |_ __init__.py
    |
    |_sequence
        |_ __init__.py define functions read_fasta, write_fasta, genetic_code , __all__ ...
        |
        |_protein molecular_weight, isolectric
        |
        |_nucleic reverse_comp, translate
        
in my program I can use these modules like this: ::
    
    from bio.sequence import read_fasta
    import bio.sequence.nucleic
    
    sequence = read_fasta('my_fasta_file')
    prot  = bio.sequence.nucleic.translate(sequence)
    
to specify a module inside a package we just specify the path to the module
using the '.' as package or module separator. 

As to specify a file path the module "path" can be absolute or relative.

| *absolute* path begin with the name of a package/module
| *relative* path use '.' or '..' to goback from one level.

for instance in my module *nucleic.py* I can use *sequence* like this: ::
   
   from ..sequence import genetic_code
   
   def translate(sequence)
      prot_seq = ''
      for i in range(len(seq)):
         codon = seq[i, i+3]
         prot_seq += genetic_code[codon]
         ...
         

.. warning::        
   
   If you use relative import in your module you cannot excute directly your module like 
   python mon_module.py anymore. If you try this python raise the folowing error
   
   **ValueError**: Attempted relative import in non-package 
  
  
.. warning::

   In Python 3, implicit relative imports within packages are no longer available.
   Only absolute imports and explicit relative imports are supported. 
   In addition, star imports (e.g. from x import \*) are only permitted in module level code.

.. note::

   Due to efficiency considerations, once you have imported a module, if you attempt to import it again, 
   Python does not raise an error but just does a nohup operation.
   
    
Standard Library
================

Python provide a lot of libraries  
which are organized in package and modules.
The full description of modules are available on the pyhton.org web site (`Python 2 <https://docs.python.org/2/py-modindex.html>`_ , `Python 3 <https://docs.python.org/3/py-modindex.html>`_).
When you code in python always refer to these documentations.
These libraies are called "standard library".


Exercises
=========

Exercise
--------

Write a program that calculates the similarity of 2 RNA sequences.

* To compute the simalirity you need to parse a file containing the :download:`similarity matrix <_static/data/similarity_matrix>`.
  
  **Hint**: use the module containing the functions that handle a matrix from previous chapter.
  put this matrix.py file in a directory named "my_python_lib" in your home or Desktop
  and import it in your current program (the similarity script must be placed elsewhere).
* The similarity of the 2 sequences is the sum of base similarities. 
  so you have to compare the first base of two sequences and use the matrix to get the similarity
  from the similarity table, on so on for all bases then sum these similarities.
  
 



