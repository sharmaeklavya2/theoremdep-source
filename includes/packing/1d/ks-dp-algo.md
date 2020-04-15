There is a dynamic-programming algorithm for the knapsack problem.
See Algorithm 3.1 in the book
['The Design of Approximation Algorithms'](http://www.designofapproxalgs.com/book.pdf)
by Williamson and Shmoys.

When the item sizes and item profits are integers,
the running time is $O(\min(nB, nV, 2^n))$,
where $B$ is the knapsack capacity and $V$ is the sum of profits of all items.
