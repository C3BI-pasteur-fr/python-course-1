.. _Input_Output:


************
Input/Output
************

Most of the programs we have seen so far are transient in the sense that they run for a short
time and produce some output, but when they end, their data disappears. If you run the
program again, it starts with a clean state.

Other programs are persistent: they run for a long time (or all the time); they keep at least
some of their data in permanent storage (a hard drive, for example); and if they shut down
and restart, they pick up where they left off.
Examples of persistent programs are operating systems, which run pretty much whenever
a computer is on, and web servers, which run all the time, waiting for requests to come in
on the network.

One of the simplest ways for programs to maintain their data is by reading and writing
text files. In this chapter we will see programs that read and write text files.
An alternative is to store the state of the program in a database this aspect of persitent 
storage will not cover in this course.


File Object
===========

A text file is a sequence of characters stored on a permanent medium like a hard drive,
flash memory, or CD-ROM

You have not to manipulate directly these media. 
Python provides basic functions and methods necessary to manipulate files by default. 
You can do your most of the file manipulation using a ``file object``. 
A file object is a high level representation of a file that abstract the media on wich 
the data are stored.

Files are like books. You open them to start working, then read or write in them and you close them when you
have finished your work. However, you have always to know where you are in the book. As children use their
fingers when they start to learn reading, you manipulate a file pointer which indicates your current position in the
file.

The first step is to get a file object. The way to do this is to use the ``open`` built-in function. 
As string are coded by default in ascii in python2.7 and utf8 in python3 the signature
of the builtin function ``open`` has changed between these two python branches.

 
.. list-table:: open built-in function in Python2 and Python3
   :header-rows: 1
   :widths: 9 9
   
   * - Python 2
     - Python 3
   * - *open(name[, mode[, buffering]])*
   
       Open a file, returning an object of the file type described in section File Objects.
       If the file cannot be opened, IOError is raised.
       
       * *name* : is the file path to be opened
       * *mode* is a string indicating how the file is to be opened.
     - *open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)*
     
       Open a file, returning an object of the file type described in section File Objects.
       If the file cannot be opened, IOError is raised.
         
       * *file* is either a string or bytes object giving the pathname
         (absolute or relative to the current working directory)
         of the file to be opened or an integer file descriptor of the file to be wrapped.
       * *mode* is a string indicating how the file is to be opened. 
       * if *encoding* is not specified the encoding used is platform dependent 
   * - https://docs.python.org/2/library/functions.html#open
     - https://docs.python.org/3/library/functions.html#open 
   
   
the different values for acces mode :

.. tabularcolumns:: |p{1cm}|p{7cm}|p{1cm}|p{7cm}|

+-----------+-----------------------------------------------------------------+-----------+-----------------------------------------------------------------+
| Python 2  |                                                                 | Python 3  |                                                                 |
+===========+=================================================================+===========+=================================================================+
| Character | Meaning                                                         | Character | Meaning                                                         |
+-----------+-----------------------------------------------------------------+-----------+-----------------------------------------------------------------+
| 'r'       | open for reading (default)                                      | 'r'       | open for reading (default)                                      |
+-----------+-----------------------------------------------------------------+-----------+-----------------------------------------------------------------+
| 'w'       | open for writing, truncating the file first                     | 'w'       | open for writing, truncating the file first                     |
+-----------+-----------------------------------------------------------------+-----------+-----------------------------------------------------------------+
|           |                                                                 | 'x'       | open for exclusive creation, failing if the file already exists |
+-----------+-----------------------------------------------------------------+-----------+-----------------------------------------------------------------+
| 'a'       | open for writing, appending to the end of the file if it exists | 'a'       | open for writing, appending to the end of the file if it exists |
+-----------+-----------------------------------------------------------------+-----------+-----------------------------------------------------------------+
| 'b'       | binary mode                                                     | 'b'       | binary mode                                                     |
+-----------+-----------------------------------------------------------------+-----------+-----------------------------------------------------------------+
|           |                                                                 | 't'       | text mode (default)                                             |
+-----------+-----------------------------------------------------------------+-----------+-----------------------------------------------------------------+
| '+'       | open a disk file for updating (reading and writing)             | '+'       | open a disk file for updating (reading and writing)             |
+-----------+-----------------------------------------------------------------+-----------+-----------------------------------------------------------------+
| 'U'       | universal newlines mode                                         | 'U'       | universal newlines mode (deprecated)                            |
+-----------+-----------------------------------------------------------------+-----------+-----------------------------------------------------------------+

The values can be combine as following

.. tabularcolumns:: |p{1cm}|p{7cm}|p{1cm}|p{7cm}|

+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| Python 2 |                                                                                            | Python 3     |                                                                                            |
+==========+============================================================================================+==============+============================================================================================+
| Modes    | Meaning                                                                                    | Character    | Meaning                                                                                    |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'r'      | Opens a file for reading only in text format.                                              | 'rt' / 'r'   | Opens a file for reading only in text format.                                              |
|          | The file pointer is placed at the beginning of the file. This is the default mode.         |              | The file pointer is placed at the beginning of the file. This is the default mode.         |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'rb'     | Opens a file for reading only in binary format.                                            | 'rb'         | Opens a file for reading only in binary format.                                            |
|          | The file pointer is placed at the beginning of the file. This is the default mode.         |              | The file pointer is placed at the beginning of the file. This is the default mode.         |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'r+'     | Opens a file for both reading and writing in text format.                                  | 'rt+' / 'r+' | Opens a file for both reading and writing in text format.                                  |
|          | The file pointer will be at the beginning of the file.                                     |              | The file pointer will be at the beginning of the file.                                     |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'rb+'    | Opens a file for both reading and writing in binary format.                                | 'rb+'        | Opens a file for both reading and writing in binary format.                                |
|          | The file pointer will be at the beginning of the file.                                     |              | The file pointer will be at the beginning of the file.                                     |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'w'      | Opens a file for writing only.                                                             | 'wt' / 'w'   | Opens a file for writing only.                                                             |
|          | Overwrites the file if the file exists.                                                    |              | Overwrites the file if the file exists.                                                    |
|          | If the file does not exist, creates a new file for writing.                                |              | If the file does not exist, creates a new file for writing.                                |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'wb'     | Opens a file for writing only in binary format.                                            | 'wb'         | Opens a file for writing only in binary format.                                            |
|          | Overwrites the file if the file exists.                                                    |              | Overwrites the file if the file exists.                                                    |
|          | If the file does not exist, creates a new file for writing.                                |              | If the file does not exist, creates a new file for writing.                                |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'w+'     | Opens a file for both writing and reading.                                                 | 'wt+' / 'w+' | Opens a file for both writing and reading.                                                 |
|          | Overwrites the existing file if the file exists.                                           |              | Overwrites the existing file if the file exists.                                           |
|          | If the file does not exist, creates a new file for reading and writing.                    |              | If the file does not exist, creates a new file for reading and writing.                    |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'wb+'    | Opens a file for both writing and reading in binary format.                                | 'wb+'        | Opens a file for both writing and reading in binary format.                                |
|          | Overwrites the existing file if the file exists.                                           |              | Overwrites the existing file if the file exists.                                           |
|          | If the file does not exist, creates a new file for reading and writing.                    |              | If the file does not exist, creates a new file for reading and writing.                    |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'a'      | Opens a file for appending. The file pointer is at the end of the file if the file exists. | 'at' / 'a'   | Opens a file for appending. The file pointer is at the end of the file if the file exists. |
|          | That is, the file is in the append mode.                                                   |              | That is, the file is in the append mode.                                                   |
|          | If the file does not exist, it creates a new file for writing.                             |              | If the file does not exist, it creates a new file for writing.                             |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'ab'     | Opens a file for appending in binary format.                                               | 'ab'         | Opens a file for appending in binary format.                                               |
|          | The file pointer is at the end of the file if the file exists.                             |              | The file pointer is at the end of the file if the file exists.                             |
|          | That is, the file is in the append mode.                                                   |              | That is, the file is in the append mode.                                                   |
|          | If the file does not exist, it creates a new file for writing.                             |              | If the file does not exist, it creates a new file for writing.                             |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'a+'     | Opens a file for both appending and reading.                                               | 'at+' / 'a+' | Opens a file for both appending and reading.                                               |
|          | The file pointer is at the end of the file if the file exists.                             |              | The file pointer is at the end of the file if the file exists.                             |
|          | The file opens in the append mode.                                                         |              | The file opens in the append mode.                                                         |
|          | If the file does not exist, it creates a new file for reading and writing.                 |              | If the file does not exist, it creates a new file for reading and writing.                 |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
| 'ab+'    | Opens a file for both appending and reading in binary format.                              | 'ab+'        | Opens a file for both appending and reading in binary format.                              |
|          | The file pointer is at the end of the file if the file exists.                             |              | The file pointer is at the end of the file if the file exists.                             |
|          | The file opens in the append mode.                                                         |              | The file opens in the append mode.                                                         |
|          | If the file does not exist, it creates a new file for reading and writing.                 |              | If the file does not exist, it creates a new file for reading and writing.                 |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+
|          |                                                                                            | 'x'          | open for exclusive creation.                                                               |
|          |                                                                                            |              | if file already exists, raise FileExistsError                                              |
+----------+--------------------------------------------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------+

Python distinguishes between binary and text I/O. 
Files opened in binary mode (including 'b' in the mode argument) return contents as bytes objects without any decoding. 
In text mode (the default, or when 't' is included in the mode argument), 
the contents of the file are returned as ``str``, in python2 the content must be encoded in ascii or we have to `decoded <http://www.tutorialspoint.com/python/string_decode.htm>`_ explicitly before.
in Python3 the bytes having been first decoded using a platform-dependent encoding or using the specified encoding if given.
 
 
.. note::

   Python doesn’t depend on the underlying operating system’s notion of text files; all the processing is done by Python itself, and is therefore platform-independent
  
.. note::

   In addition to the standard values (rwa+) mode may be 'U' or 'rU'. Python is usually built with universal newlines support; 
   supplying 'U' opens the file as a text file, but lines may be terminated by any of the following: 
   the Unix end-of-line convention '\n', the Macintosh convention '\r', or the Windows convention '\r\n'. 
   All of these external representations are seen as '\n' by the Python program. 
   If Python is built without universal newlines support a mode with 'U' is the same as normal text mode. 
   Note that file objects so opened also have an attribute called newlines which has a value of None 
   (if no newlines have yet been seen), '\n', '\r', '\r\n', or a tuple containing all the newline types seen.
   
   
some file object methods and attributs
--------------------------------------
 


read([size])
^^^^^^^^^^^^

Read at most size bytes from the file (less if the read hits EOF before obtaining size bytes). 
If the size argument is negative or omitted, read all data until EOF is reached. 
The bytes are returned as a string object.   

readline([size])
^^^^^^^^^^^^^^^^

Read one entire line from the file. A trailing newline character is kept in the string (but may be absent when a file ends with an incomplete line).

readlines()
^^^^^^^^^^^

Read until EOF using readline() and return a list containing the lines thus read. 
If the optional sizehint argument is present, instead of reading up to EOF, 
whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.
 
close()
^^^^^^^

Close the file. A closed file cannot be read or written any more.
Any operation which requires that the file be open will raise a **ValueError** after the file has been closed. 
Calling close() more than once is allowed.

flush()
^^^^^^^  

Flush the internal buffer

tell() 
^^^^^^   

Return the file’s current position

seek(offset[, whence])
^^^^^^^^^^^^^^^^^^^^^^   

Set the file’s pointer. 
The *whence* argument is optional 

   * defaults to os.SEEK_SET or 0 (absolute file positioning); 
   * other values are os.SEEK_CUR or 1 (seek relative to the current position)
   * and os.SEEK_END or 2 (seek relative to the file’s end). There is no return value.

::

   >>> f = open('workfile', 'r+')   
   >>> f.write('0123456789abcdef')
   >>> f.seek(5)     # Go to the 6th byte in the file
   >>> f.read(1)
   '5'
   >>> f.seek(-3, 2) # Go to the 3rd byte before the end
   >>> f.read(1)
   'd'
   

next()
^^^^^^

A file object is its own iterator.
When a file is used as an iterator, typically in a for loop, the next() method is called repeatedly. 
This method returns the next input line, or raises StopIteration when EOF is hit when the file is open for reading (behavior is undefined when the file is open for writing).::
      
   f = open('foobar' , 'r')
   for line in f:
      do something
   
write()
^^^^^^^

Write a string to the file. 
There is no return value. 
Due to buffering, the string may not actually show up in the file until the flush() or close() method is called.

writelines(sequence)
^^^^^^^^^^^^^^^^^^^^

Write a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings. 
There is no return value. (The name is intended to match readlines(); writelines() does not add line separators.)

closed
^^^^^^
bool indicating the current state of the file object. This is a read-only attribute; the close() method changes the value. 

name
^^^^   
the name of the file.


Why It's important to close files
=================================

Python does not promise that it will close the files for you. 
The operating system does, when the program exits.  
In some very trivial program, that's right away.  
But if your program does something else for a while, 
or repeats this sequence of steps dozens of times, 
you could **run out** of resources, or **overwrite** something.

The place to close the input file is right after you're done reading the 
data, and before opening the output file.

but examine in practice how to close a file.

.. code-block:: python

   try:
      f = open('/tmp/foo' ,'r')
   Except IOError as err:
      print "cannot open
   
   for line in f:
      fields = line.split()
      id = fields[1]
      comment = fields[2]

In this piece of code we protect the open in a try/except but what happen 
if an error occured during the data processing, if one line have not a fields[2] for instance.
An error is raised but the file is not closed. If this piece of code is en closed in a larger
try/except the file will stay open until the end of the script.

.. code-block:: python

   try:
      f = open('/tmp/foo' ,'r')
      for line in f:
         fields = line.split()
         id = fields[1]
         comment = fields[2]
   Except IOError as err:
      print "cannot open
   Except Exception:
      f.close()   

OK now we can catch all error and we close the file if an error occured during the data reading/processing
but it is not closed if the process finish normally. So we can again improve our code: 

.. code-block:: python
   
   try:
      f = open('/tmp/foo' ,'r')
      for line in f:
         fields = line.split()
         id = fields[1]
         comment = fields[2]
   Except IOError as err:
      print "cannot open
   finally:
      f.close()    
        
It's work perfectly but we have to write technical code (ty/except/finally) and the ``close`` can be far away the ``open`` which not increase the code reading.
Python introduce in python2.6 the notion of context manager with the ``with`` keywords.
which is a generalization of: 

.. code-block:: python

   try:
      use a ressource
   except Exception as err:
      rollback
      close ressource
   finally
      commit ressource
      close ressource

so the code to open a file using a with become: ::
  
   with open('/tmp/foo' ,'r') as f:
      for line in f:
         fields = line.split()
         id = fields[1]
         comment = fields[2]

It is good practice to use the ``with`` keyword when dealing with file objects. 
This has the advantage that the file is properly closed after its suite finishes, 
even if an exception is raised on the way.
It is also much shorter and readable than writing equivalent *try-finally* blocks.


helpful functions to manipulate files
=====================================
 
 
os.path
-------
 
``os.path`` module provide a lot of usefil function to manipulate path :
 
os.path.abspath(path)
^^^^^^^^^^^^^^^^^^^^^
 
Return a normalized absolutized version of the pathname path.
 
os.path.exists(path)
^^^^^^^^^^^^^^^^^^^^

Return True if path refers to an existing path. 
Returns False for broken symbolic links. 
On some platforms, this function may return False if permission is not granted to execute os.stat() on the requested file, even if the path physically exists.

os.path.realpath(path)
^^^^^^^^^^^^^^^^^^^^^^

Return the canonical path of the specified filename, 
eliminating any symbolic links encountered in the path (if they are supported by the operating system).
  
os.path.join(path1[, path2[, ...]])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Join one or more path components intelligently. 
If any component is an absolute path, all previous components 
(on Windows, including the previous drive letter, if there was one) are thrown away, and joining continues. 
The return value is the concatenation of path1, and optionally path2, etc., with exactly one directory separator (os.sep) following each non-empty part except the last.
 
 
 
for complete descriptions : https://docs.python.org/2/library/os.path.html#module-os.path
 
 
os
--
 
 wheras ``os`` package provide function to manipulate file itself: 
 
os.remove(path) or os.unlink(path)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove (delete) the file path. If path is a directory, OSError is raised; 
see rmdir() below to remove a directory.

os.rename(src, dst)
^^^^^^^^^^^^^^^^^^^

Rename the file or directory src to dst. If dst is a directory, OSError will be raised. 
On Unix, if dst exists and is a file, it will be replaced silently if the user has permission. 
 
 
or directories
 
os.mkdir(path[, mode])
^^^^^^^^^^^^^^^^^^^^^^

Create a directory named path with numeric mode mode. 
The default mode is 0777 (octal). On some systems, mode is ignored. 
Where it is used, the current umask value is first masked out. If the directory already exists, OSError is raised.

os.makedirs(path[, mode])
^^^^^^^^^^^^^^^^^^^^^^^^^

Recursive directory creation function. Like mkdir(), but makes all intermediate-level directories needed to contain the leaf directory. 

os.getcwd()
^^^^^^^^^^^

Return a string representing the current working directory.

os.listdir(path)
^^^^^^^^^^^^^^^^

Return a list containing the names of the entries in the directory given by path. 
The list is in arbitrary order. It does not include the special entries '.' and '..' even if they are present in the directory.
    
os.rmdir(path)
^^^^^^^^^^^^^^

Remove (delete) the directory path. Only works when the directory is empty, otherwise, OSError is raised. 
  
os.removedirs(path)
^^^^^^^^^^^^^^^^^^^

Remove directories recursively. Works like rmdir() except that, 
if the leaf directory is successfully removed, removedirs() tries to successively 
remove every parent directory mentioned in path until an error is raised 
(which is ignored, because it generally means that a parent directory is not empty).
 
to acces to all functions and whole descriptions : https://docs.python.org/2/library/os.html#files-and-directories
 
 
shutil
------
 
If you have to manipulate non empty directories tree use rmtree from ``shutil`` module.
  
shutil.rmtree(path[, ignore_errors[, onerror]])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete an entire directory tree; path must point to a directory (but not a symbolic link to a directory). 
 
https://docs.python.org/2/library/shutil.html#shutil.rmtree

just an example to illustrate a typicall work with files.
In this example we reading a file containing several numbers per line, 
and write the average in a file named 'my_script.out' in a new directory 'results': 

.. literalinclude:: _static/code/average.py
   :linenos:
   :language: python
   
:download:`script average.py<_static/code/average.py>`


Exercises
=========

Exercise
--------

Write a function which take the path of file as parameter
and display it's content on the screen.

We wait same behavior as the shell *cat* command. 

Exercise
--------

Write a function which take the path of a file in rebase format
and return in a dictionnary the collection of the enzyme contains in the file.
The sequence of the binding site must be cleaned up.

:download:`rebase_light.txt <_static/data/rebase_light.txt>` .
 
Exercise
--------

write a function which take the path of a fasta file
and return a data structure of your choice that allow to stock 
the id of the sequence and the sequence itself.

:download:`seq.fasta <_static/data/seq.fasta>` .

Exercise
--------

Modify the code at the previous exercise to read multiple sequences fasta file.
use the file :download:`abcd.fasta <_static/data/abcd.fasta>` to test your code.
    

Exercise
--------

Read a multiple sequence file in fasta format and write to a new file, one sequence by file,
only sequences starting with methionine and containing at least six tryptophanes (W).

Use the same file as previous exercise to test you code. 
(*you should create files for sequences: ABCD1_HUMAN, ABCD1_MOUSE, ABCD2_HUMAN, ABCD2_MOUSE, ABCD2_RAT, ABCD4_HUMAN, ABCD4_MOUSE*)

bonus
^^^^^

Write sequences with 80 aa/line


Exercise
--------

we ran a blast with the folowing command *blastall -p blastp -d uniprot_sprot -i query_seq.fasta -e 1e-05 -m 8 -o blast2.txt*

-m 8 is the tabular output. So each fields is separate to the following by a '\t' 

The fields are: query id, database sequence (subject) id, percent identity, alignment length, number of mismatches, number of gap openings, 
query start, query end, subject start, subject end, Expect value, HSP bit score. 

:download:`blast2.txt <_static/data/blast2.txt>` .

| parse the file
| sort the hits by their *percent identity* in the descending order.
| write the results in a new file.

(adapted from *managing your biological data with python*)

Hint: look operator.itemgetter