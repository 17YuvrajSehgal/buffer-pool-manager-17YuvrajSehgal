# Computer Science Department, Brock University
## COSC 4P32: Database Systems

Assignment 2 - Implementing Buffer Pool

In this class we assume that the primary storage location of the database is on disk.

The goal of this programming project is to implement a buffer pool in your storage manager.  The buffer pool is responsible for moving physical pages back and forth from main memory to disk

### First Step

Using the computer that you normally use for your school work (e.g., laptop), create an account on GitHub (if you do not already have one). 
You may need to install git on it. Checkout your 4P32-BufferManager repository by cliking on the link above. 

You are given the following components:
- Disk Manager: It is responsible to create, read, write and delete pages on disk
- Buffer Pool Manager: It is responsible for fetching database pages from the DiskManager and storing them in memory. 
- Replacer: It keeps track of when Page are accessed so that it can decide which one to evict when it must free a frame to make room for copying a new physical page from disk.
- Page: It is the representation of in-memory pages

You will need to implement/extend the following two components in your storage manager:

- Least recently used (LRU) Replacement Policy: it discards the least recently used page first. This algorithm requires keeping track of what was used when. 
- Buffer Pool Manager

### Second Step

Implemente the functions in the files buffer_pool_manager.py and lru_replacer.py 
Complete the exercise given in "exercise.py"


### Third Step

Once you are finished, "git push" your code to the Git Classroom

