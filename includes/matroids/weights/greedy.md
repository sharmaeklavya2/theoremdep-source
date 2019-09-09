Let $M = (S, I)$ be a matroid and $X \subseteq S$.
Let $w$ be a weight function.
Then there is a greedy algorithm which can compute
a max-weight basis of $X$.

## Algorithm

Algorithm in python-pseudocode:

    A = {}
    for x in sorted(X, key=w, reverse=True):
        if A + x ∈ I:
            A.add(x)
    return A

## Proof of correctness

Let $A$ be the output of the greedy algorithm
and $B$ be max-weight basis.

Since $x$ is added to $A$ only when $A+x \in I$, $A$ is an independent set.
Since $B$ is a basis, $|A| \le |B|$.

Suppose $|B| > |A|$. By exchange axiom, $\exists x \in B-A, A + x \in I$.
Let $D = \{ y \in A: w(y) \ge w(x) \}$.
Since $x$ was not added to $A$, $D + x \not\in I$.
Therefore, $A + x \not\in I$ (by contrapositive of hereditary property).
This is a contradiction. Therefore, $A$ is a basis.
Therefore, $|A| = |B|$.

Let $A = [a_1, a_2, \ldots, a_n]$ and $B = [b_1, b_2, \ldots, b_n]$.
Assume that $w(A) \neq w(B)$. Then $\exists i, w(a_i) \neq w(b_i)$.
Let $i = \min_j (w(a_j) \neq w(b_j))$.
Since $A$ is greedy, $w(a_i) > w(b_i)$.

As per the exchange axiom, repeatedly add elements from $B$ to $[a_1, a_2, \ldots, a_i]$ to get a basis $C$.
These newly added elements will have a total weight at least $\sum_{j=i+1}^n w(b_j)$.
Therefore, $w(C) - w(B) \ge w(a_i) - w(b_i) > 0$.
Therefore, $w(C) > w(B)$.
This contradicts the fact that $B$ is a max-weight basis.
Therefore, $w(A) = w(B)$, so $A$ is a max-weight basis.
