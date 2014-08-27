.. sectnum:: 
   :start: 10
   
   
.. _From_script_to_project:

**********************************
From script to a project in Python
**********************************


Which Python version to use?
============================

We already discuss this topics in the :ref:`Indtroduction <python2vs3>` of this course. 
But I just want to add that Python2 should be stoped in 2017 during the last python convention
they decide to delay the python 2 end of life until 2020. 
But Python 2 is on maintenance phase all new feature will be developed on Python 3 only.
So if you care about the future of your project, and if you have the option, choose Python 3.


.. _pep_8:

Follow the conventions
======================

Python proposed a set of  **conventions** for the Python code comprising the standard library in the main Python distribution.

| A style guide is about consistency. 
| Consistency with this style guide is important. 
| Consistency within a project is more important. 
| Consistency within one module or function is most important.

Some good reasons to ignore a particular guideline:

* When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP.
* To be consistent with surrounding code that also breaks it (maybe for historic reasons) -- although this is also an opportunity to clean up someone else's mess (in true XP style).
* Because the code in question predates the introduction of the guideline and there is no other reason to be modifying that code.
* When the code needs to remain compatible with older versions of Python that don't support the feature recommended by the style guide.

all these conventions rules are described in the `Python Enhancement Proposal 8 <http://legacy.python.org/dev/peps/pep-0008/>`_ 

Why pep 8
---------

code is read much more often than it is written. 
The guidelines provided here are intended to improve the readability of code and make it consistent across the wide spectrum of Python code.
As PEP 20 says, "**Readability counts**".

maintenance a long term 

collaboration

We can compare these conventions to the punctuation. If you write a text in natural language and if you omit the any punctuation,
never begin a new sentence by a capital letter, don't make paragraph. Even your text could be syntactically right, it will be very hard to understand.
If you write just few lines like that, maybe someone will do the efforts to understand you. But if you write a novel like this, no way, nobody
will read you. Even you if you want to read you in future it will need to do lot of efforts to understand yourself.

So if you want to share youre program, if you want to maintain it in future, follow the pep8 conventions. 

main conventions
----------------

**Indentation**
   Use 4 spaces per indentation level.

**Blank Lines**
   | Separate top-level function and class definitions with two blank lines.
   | Method definitions inside a class are separated by a single blank line.
   | Use blank lines in functions, sparingly, to indicate logical sections

**Source File Encoding**
   Code in the core Python distribution should always use UTF-8 (or ASCII in Python 2).

   Files using ASCII (in Python 2) or UTF-8 (in Python 3) should not have an encoding declaration.
   
**Imports**   
   Imports should usually be on separate lines, e.g.: ::
   
      Yes: import os
           import sys
   
      No:  import sys, os
   
   It's okay to say this though: ::
   
      from subprocess import Popen, PIPE
   
   Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
   
   Imports should be grouped in the following order:
   
   #. standard library imports
   #. related third party imports
   #. local application/library specific imports
   
   You should put a blank line between each group of imports.

**Whitespace in Expressions and Statements**
   Avoid extraneous whitespace in the following situations:
   
   * Immediately inside parentheses, brackets or braces: ::
   
       Yes: spam(ham[1], {eggs: 2})
       No:  spam( ham[ 1 ], { eggs: 2 } )
   
   * Immediately before a comma, semicolon, or colon: ::
   
       Yes: if x == 4: print x, y; x, y = y, x
       No:  if x == 4 : print x , y ; x , y = y , x
   
   * Immediately before the open parenthesis that starts the argument list of a function call: ::
   
       Yes: spam(1)
       No:  spam (1)
   
   * Immediately before the open parenthesis that starts an indexing or slicing: ::
   
       Yes: dict['key'] = list[index]
       No:  dict ['key'] = list [index]
   
   * More than one space around an assignment (or other) operator to align it with another. ::
   
       Yes:
   
       x = 1
       y = 2
       long_variable = 3
   
       No:
   
       x             = 1
       y             = 2
       long_variable = 3
   
**Comments**
   Comments that contradict the code are worse than no comments. 
   Always make a priority of keeping the comments up-to-date when the code changes!
   
   Python coders from non-English speaking countries: please write your comments in English, 
   unless you are 120% sure that the code will never be read by people who don't speak your language.
   
   Use inline comments sparingly.

**Naming Conventions**

   **Names to Avoid**
      Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
      
      In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.
      Package and Module Names
      Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability.

   **Class Names**
      Class names should normally use the CapWords convention.

   **Function Names**
      Function names should be lowercase, with words separated by underscores as necessary to improve readability.

   **Function and method arguments**
      Always use self for the first argument to instance methods.
      
      Always use cls for the first argument to class methods.
      
      If a function argument's name clashes with a reserved keyword, 
      it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. 
      Thus *class_* is better than *clss*. (Perhaps better is to avoid such clashes by using a synonym.)

   **Constants**
      Constants are usually defined on a module level and written in all capital letters with underscores separating words. 
      Examples include MAX_OVERFLOW and TOTAL.


Managing code
=============

The project code base evolves so much that it is important to track all the changes
that are made, even more so when many developers work on it. That is the role of a
version control system.

Version control systems (VCS) provide a way to share, synchronize, and back up any
kind of files and keep a trace of every modifications done on the project. 

On you're lab book, you write every experiments, the results on so on.
The lab book help you when you want to know whta are you did last time why it'work or not.
It help you to prove you are the author of discovery. 
The vcs do the same thing for you with your code.
Futhermmore it allow you to collaborate like if you share the same labbook between several
labs and in fine you can exactly know what people did on the project.  

what vcs do for you?

* Made a change to code, realised it was a mistake and wanted to revert back?
* Lost code or had a backup that was too old?
* Had to maintain multiple versions of a product?
* Wanted to see the difference between two (or more) versions of your code?
* Wanted to prove that a particular change broke or fixed a piece of code?
* Wanted to review the history of some code?
* Wanted to submit a change to someone else's code?
* Wanted to share your code, or let other people work on your code?
* Wanted to see how much work is being done, and where, when and by whom?
* Wanted to experiment with a new feature without interfering with working code?

do I need to use a vcs?
Here is a simple flowchart that will help you decide whether you should be using version control for your research software and related files.

.. image:: _static/figs/use_a_vcs.png
   :align: center
   :height: 500px
   :alt: do I need a vcs?

The vcs are categorized in two families:

#. Centralized systems
#. Distributed systems

Centralized Systems
-------------------

A centralized version control system is based on a single server that holds the files
and lets people check in and check out the changes that are made to those files. 
The principle is quite simple: Everyone can get a copy of the files on his/her system and
work on them. From there, every user can commit his/her changes to the server. 
They will be applied and the revision number will be raised. Other users will then be able
to get those changes by synchronizing their repository copy through an update.
The repository evolves through all the commits, and the system archives all revisions
into a database to undo any change, or provide information on what has been done:

.. image:: _static/figs/CVCS.png
   :align: center
   :height: 300px
   :alt: cvcs schema

The most know centralized system is `subversion <http://subversion.apache.org/>`_


Distributed Systems
-------------------

Distributed VCS is the answer to the centralized VCS. It does not rely on a main
server that people work with, but on peer-to-peer principles. Everyone can hold and
manage his/her own independent repository for a project, and synchronize it with
other repositories:

.. image:: _static/figs/DVCS.png
   :align: center
   :height: 300px
   :alt: dvcs schema
   
The key concept is that people push and pull the files with other repositories, and
this behavior changes according to the way people work and the way the project is
managed. Since there is no main repository anymore, the maintainer of the project
needs to define a strategy for people to push and pull the changes.


the most known DVCS are `git <http://git-scm.com/>`_ , 
`mercurial <http://mercurial.selenic.com/>`_ , 
`bazaar <http://bazaar.canonical.com/en/>`_, ...

GitHub
------

`GitHub <https://github.com/>`_ is a web platform based on git which aim
to make software development more collaborative. It's focus on:

* collaboration, 
* code review, 
* and code management for open source and private projects. 

There are lot of webhook which allow to trigger some action when you modify your github repository.
with thesewebhook you can set up a continuous integration system.  
 
`Improving GitHub for science <https://github.com/blog/1840-improving-github-for-science>`_
   Citable code for academic software
      Sharing your work is good, but collaborating while also getting required academic credit is even better. 
      It possible to get a Digital Object Identifier (DOI) for any GitHub repository archive.
   
      With a DOI for your GitHub repository archive, your code becomes citable.
   
   Academic accounts on GitHub
      We also know that as a scientific researcher, sometimes you're going to want to work privately. 
      That's why we've created a discount where individual academic researchers can receive a free micro plan with 5 private repos, 
      while research groups can receive a free silver plan with 20 repos.
   
      To set up an academic account on GitHub, first associate an academic email address with your account and then request a GitHub Education discount.


Documenting Your Project
========================

Documentation is work that is often neglected by developers and sometimes by managers. 
This is often due to a lack of time towards the end of development cycles,
and the fact that people think they are bad at writing. Some of them are bad, but the
majority of them are able to produce fine documentation.

In any case, the result is a disorganized documentation made of documents that are
written in a rush. Developers hate doing this kind of work most of the time. 
Things get even worse when existing documents need to be updated. 
Many projects out there are just providing poor, out-of-date documentation 
because the manager does not know how to deal with it.

But setting up a documentation process at the beginning of the project and treating
documents as if they were modules of code makes documenting easier.

`sphinx <http://sphinx-doc.org/index.html>`_  
Sphinx is a tool that makes it easy to create documentation.
It was originally created for the new Python documentation, 
So it has excellent facilities for the documentation of Python projects.
Sphinx uses reStructuredText as its markup language which a simple but powerfull syntax.
This course has been created with sphinx.
few features supported by sphinx

* Output formats: HTML (including Windows HTML Help), LaTeX (for printable PDF versions), ePub, Texinfo, manual pages, plain text
* Extensive cross-references: semantic markup and automatic links for functions, classes, citations, glossary terms and similar pieces of information
* Hierarchical structure: easy definition of a document tree, with automatic links to siblings, parents and children
* Automatic indices: general index as well as a language-specific module indices
* Code handling: automatic highlighting using the Pygments highlighter
* Extensions: automatic testing of code snippets, inclusion of docstrings from Python modules (API docs),

readthedoc
----------

`readthedoc <https://readthedocs.org/>`_ is a web plateform which hosts documentation.
It's based on sphinx and you can link you vcs to *readthedoc* for instance there is a webhook in github
to link your github repository to readthedoc so each time you make a change in github (commit), the documentation is updateded on readthedocs.
readthedocs host freely your project for the open source community.

 
Unit tests
==========

unittest automation
https://travis-ci.org/
https://travis-ci.org/mobyle2/mobyle2.exec_engine

`coverage <http://nedbatchelder.com/code/coverage/>`_

Debuging
========

pylint
http://www.pylint.org/

Optimization
============

profiling

Virtualenv
==========

http://virtualenv.readthedocs.org/en/latest/virtualenv.html
virtualenv, help developers and packagers. 
virtualenv builds python sandboxes where it is possible to do whatever you want as a simple user without putting in jeopardy your global environment.

virtualenv allows you to safety:

* install any python packages
* add debug lines everywhere (not only in your scripts)
* switch between python versions
* try your code as you are a final user
* and so on ...
