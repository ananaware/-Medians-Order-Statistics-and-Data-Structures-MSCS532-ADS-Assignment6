\# MSCS 532 – Algorithms and Data Structures

\## Assignment 6: Medians, Order Statistics, and Elementary Data Structures



Student: Anushka Nanaware



\---



\## Overview



This assignment explores algorithms for selecting the k-th smallest element (order statistics) and implements fundamental data structures such as stacks, queues, and linked lists. Both theoretical and empirical analyses are performed to evaluate algorithm performance.



\---



\## Part 1 – Selection Algorithms



Two algorithms were implemented to find the k-th smallest element in an array:



1\. Randomized Quickselect

2\. Deterministic Selection using the Median of Medians method



\### Randomized Quickselect

This algorithm randomly selects a pivot and partitions the array similarly to Quicksort. Its expected running time is O(n), although the worst-case time complexity is O(n²).



\### Deterministic Selection (Median of Medians)

This algorithm guarantees O(n) worst-case time complexity by selecting a good pivot using the median-of-medians strategy. While theoretically optimal, it often performs slower in practice due to additional overhead.



\---



\## Empirical Analysis



Experiments were conducted using randomly generated arrays of different sizes.



| Input Size | Randomized Quickselect | Deterministic Select |

|------------|-----------------------|----------------------|

| 100 | \~0.00005 s | \~0.00005 s |

| 1000 | \~0.0002 s | \~0.0004 s |

| 5000 | \~0.0011 s | \~0.0016 s |

| 10000 | \~0.0026 s | \~0.0046 s |



Results show that randomized Quickselect typically performs faster in practice due to lower overhead.



\---



\## Part 2 – Elementary Data Structures



The following data structures were implemented from scratch using Python:



\### Stack

A stack follows the Last-In-First-Out (LIFO) principle.



Operations implemented:

\- push

\- pop

\- peek

\- is\_empty



Time complexity:

\- Push: O(1)

\- Pop: O(1)



\---



\### Queue

A queue follows the First-In-First-Out (FIFO) principle.



Operations implemented:

\- enqueue

\- dequeue



Time complexity:

\- Enqueue: O(1)

\- Dequeue: O(n) using array implementation



\---



\### Singly Linked List



Operations implemented:

\- insertion

\- deletion

\- traversal



Time complexity:

\- Insertion: O(n)

\- Deletion: O(n)



Linked lists provide dynamic memory allocation and efficient insertions compared to arrays.



\---



\## Files in Repository



selection\_algorithms.py  

experiment.py  

data\_structures.py  

README.md  



\---



\## How to Run



Run the selection algorithms:



python selection\_algorithms.py



Run the experiment:



python experiment.py



Run the data structure tests:



python data\_structures.py



\---



\## Conclusion



This assignment demonstrates the importance of efficient selection algorithms and foundational data structures. The deterministic selection algorithm provides strong theoretical guarantees, while randomized Quickselect performs better in most practical scenarios. Understanding the performance and use cases of stacks, queues, and linked lists is fundamental to algorithm design and software development.

