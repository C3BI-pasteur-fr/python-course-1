.. _Creating_and_Calling_Functions:

******************************
Creating and Calling Functions
******************************

Creating and Calling Functions
==============================

Names and Docstrings
--------------------

.. _arguments:

Arguments and Parameters
------------------------

.. _unpack:

Parameter Unpacking
-------------------

Return values
-------------

Variables Scope and Life time
-----------------------------

Although scopes are determined statically, they are used dynamically. At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:

    the innermost scope, which is searched first, contains the local names
    the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
    the next-to-last scope contains the current module’s global names
    the outermost scope (searched last) is the namespace containing built-in name