Let $X$ be a finite set.

A permutation of $X$ is a bijection from $X$ to $X$.
A group where every element is a permutation of $X$ is called a permutation group.
The group operator is function composition.

The set of all permutations of $X$, denoted by $S_X$, is a group and is called the symmetric group on $X$.
Consequently, all permutation groups are subgroups of the symmetric group.

A cycle of length $n$, denoted as $(a_1, a_2, \ldots, a_n)$, is a permutation where
$a_i$ maps to $a_{i+1}$ for all $1 \le i < n$ and $a_n$ maps to $a_1$.

A transposition is a cycle of length 2.

## Proof that $S_X$ is a group

* Closure: The composition of 2 bijections is a bijection.
* Associativity: Function composition is associative.
* Identity: The identity permutation, which maps $x$ to $x$ for all $x \in X$, is the identity of $S_X$.
* Inverse: Every bijection has an inverse.
