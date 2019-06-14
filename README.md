# linked_list_intersection
Finding the first common node of two linked lists in optimal time

We have two linked lists 

  A = a0 -> a1 -> ... and B = b0 -> b1 -> ...

Denote their lengths by lA and lB

Let their first common node be X. A usual algorithm to find X is:

1) Iterate through A and B
2) Compute difference d = lA - lB
3) Retrace from the beginning (with offset d) to find X

This operates in time O(lA + lB).

Here we devise and implement an algorithm that runs in time

O( d(X,a0) + d(X,b0) )

where d(,) denotes distance between two nodes. So basically we operate in time proportional to the initial segments before the first common Node.


