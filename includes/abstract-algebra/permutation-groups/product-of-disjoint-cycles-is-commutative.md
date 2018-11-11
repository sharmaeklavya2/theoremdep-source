## Proof

Let $\sigma = (a_1, a_2, \ldots, a_k)$ and $\tau = (b_1, b_2, \ldots, b_l)$ be two disjoint permutations
in the symmetric group $S_X$.

We have to prove that $\forall x \in X, \sigma(\tau(x)) = \tau(\sigma(x))$.

* Case 1: $x \not\in \sigma \wedge x \not\in \tau$:
    * $\sigma(\tau(x)) = \sigma(x) = x$
    * $\tau(\sigma(x)) = \tau(x) = x$.

* Case 2: $x = a_i \in \sigma \wedge x \not\in \tau$:
    * $\sigma(\tau(a_i)) = \sigma(a_i) = a_{(i+1)\%k}$
    * $\tau(\sigma(a_i)) = \tau(a_{(i+1)\%k}) = a_{(i+1)\%k}$

* Case 3: $x \not\in \sigma \wedge x = b_i \in \tau$:

    Similar to case 2.

Since in all 3 cases $\sigma(\tau(x)) = \tau(\sigma(x))$,
product of two disjoint cycles is commutative.
