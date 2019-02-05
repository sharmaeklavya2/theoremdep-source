The Gram-Schmidt process takes a set of n linearly independent vectors as input and outputs a set of n orthogonal vectors which have the same span.

Let $W = \{w_1, w_2, \ldots, w_n\}$ be a linearly independent set of vectors from an inner product space.
Then the Gram-Schmidt process outputs $V = \{v_1, v_2, \ldots, v_n\}$ where

\[ v_i = w_i - \sum_{j=1}^{i-1} c_{i, j} v_j
\textrm{ where } c_{i, j} = \frac{\langle w_i, v_j \rangle}{\|v_j\|^2} \]

Then:

* $\operatorname{span}(V) = \operatorname{span}(W)$.
* $\forall i, v_i \neq 0$.
* $\forall i \neq j, \langle v_i, v_j \rangle = 0$.

Also, scaling each $v_i$ by a (possibly different) non-zero scalar maintains orthogonality and does not change the span.

## Proof by induction

Let $V_k = \{v_1, v_2, \ldots, v_k\}$ and $W_k = \{w_1, w_2, \ldots, w_k\}$.

Let the predicate $P(k)$ be the 'logical and' of the following statements:

1.  $\operatorname{span}(V_k) = \operatorname{span}(W_k)$.
2.  $\forall i \le k, v_i \neq 0$.
3.  $\forall i < j \le k, \langle v_i, v_j \rangle = \langle v_j, v_i \rangle = 0$.

Base case:

$v_1 = w_1$.

1.  $\operatorname{span}(V_1) = \operatorname{span}(\{v_1\}) = \operatorname{span}(\{w_1\}) = \operatorname{span}(W_1)$.
2.  Since $W$ is linearly independent, $w_1 \neq 0 \Rightarrow v_1 \neq 0$.
3.  The third part of $P(1)$ is trivially true.

Therefore, $P(1)$ holds.

Inductive step:

Assume $P(k)$ is true (inductive hypothesis).

### Part 1

\[ \forall i \le k, w_i \in \operatorname{span}(W_k) = \operatorname{span}(V_k) \subseteq \operatorname{span}(V_{k+1}) \]

\[ w_{k+1} = v_{k+1} + \sum_{j=1}^k c_{k+1, j} v_j \in \operatorname{span}(V_{k+1}) \]

Since, each of $w_1, w_2, \ldots, w_{k+1}$ is a linear combination of $V_{k+1}$.
Their linear combination is also a linear combination of $V_{k+1}$.
Therefore, $\operatorname{span}(W_{k+1}) \subseteq \operatorname{span}(V_{k+1})$.

\[ \forall i \le k, v_i \in \operatorname{span}(V_k) = \operatorname{span}(W_k) \subseteq \operatorname{span}(W_{k+1}) \]

\begin{align}
& \sum_{j=1}^k c_{k+1, j} v_j
    \in \operatorname{span}(V_k) = \operatorname{span}(W_k) \subseteq \operatorname{span}(W_{k+1})
\\ &\Rightarrow v_{k+1} = w_{k+1} - \sum_{j=1}^k c_{k+1, j} v_j
    \in \operatorname{span}(W_{k+1})
\end{align}

Since, each of $v_1, v_2, \ldots, v_{k+1}$ is a linear combination of $W_{k+1}$.
Their linear combination is also a linear combination of $W_{k+1}$.
Therefore, $\operatorname{span}(V_{k+1}) \subseteq \operatorname{span}(W_{k+1})$.

Therefore, $\operatorname{span}(V_{k+1}) = \operatorname{span}(W_{k+1})$,
which is part 1 of $P(k+1)$.

### Part 2

\[ v_{k+1} = 0 \implies w_{k+1} = \sum_{i=1}^k c_{k+1, i} v_i \in \operatorname{span}(V_k) = \operatorname{span}(W_k) \]

$w_{k+1} \in \operatorname{span}(W_k)$ means $W_{k+1}$ is linearly dependent, which is a contradiction.
Therefore, $v_{k+1} \neq 0$.
Combining this fact with part 2 of $P(k)$, we get $\forall i \le k+1, v_i \neq 0$,
which is the part 2 of $P(k+1)$.

### Part 3

Let $i \le k$.

\begin{align}
\langle v_{k+1}, v_i \rangle
&= \left\langle w_{k+1} - \sum_{j=1}^k \frac{\langle w_{k+1}, v_j \rangle}{\|v_j\|^2} v_j \; , v_i \right\rangle
\\ &= \langle w_{k+1}, v_i \rangle - \sum_{j=1}^k \frac{\langle w_{k+1}, v_j \rangle}{\|v_j\|^2} \langle v_j, v_i \rangle
    \tag{linearity in first argument}
\\ &= \langle w_{k+1}, v_i \rangle - \frac{\langle w_{k+1}, v_i \rangle}{\|v_i\|^2} \langle v_i, v_i \rangle
    \tag{$\because i \neq j \Rightarrow \langle v_j, v_i \rangle = 0$}
\\ &= \langle w_{k+1}, v_i \rangle - \langle w_{k+1}, v_i \rangle = 0
\end{align}

\[ \langle v_i, v_{k+1} \rangle = \overline{\langle v_{k+1}, v_i \rangle}
= \overline{0} = 0 \tag{by conjugate symmetry} \]

Combining the above fact with part 3 of $P(k)$, we get part 3 of $P(k+1)$.

Therefore, $P(n)$ is true by mathematical induction.
