If a permutation can be written as a product of only an odd number of transpositions, it is called an odd permutation.
If a permutation can be written as a product of only an even number of transpositions, it is called an even permutation.
Every permutation is either an odd permutation or an even permutation.

## Proof

Let there be $n$ cycles in the canonical cycle notation of the permutation $\lambda$.
Let the $i^{\textrm{th}}$ cycle be $\sigma_i$ of length $n_i$.
Then the parity of $\lambda$ is defined as

\[ \operatorname{parity}(\lambda) = \left( \sum_{i=1}^n (n_i - 1) \right) \% 2 \]

### Lemma 1: multiplying a permutation by a transposition changes its parity

Let $\tau$ be a transposition.

* Case 1: $\tau$ does not intersect $\lambda$:

    Then $\operatorname{parity}(\lambda\tau) = (\operatorname{parity}(\lambda) + 1) \% 2$

* Case 2: One element of $\tau$ intersects $\sigma_i$:

    The canonical cycle notation of $\lambda\tau$ is
    $\sigma_1\ldots\sigma_{i-1}\mu\sigma_{i+1}\ldots\sigma_n$,
    where $\mu$ is a cycle of length $n_i+1$.
    Therefore, $\operatorname{parity}(\lambda\tau) = (\operatorname{parity}(\lambda) + 1) \% 2$

* Case 3: Both elements of $\tau$ intersect $\sigma_i$:

    The canonical cycle notation of $\lambda\tau$ is
    $\sigma_1\ldots\sigma_{i-1}\mu_1\mu_2\sigma_{i+1}\ldots\sigma_n$,
    where the sum of lengths of cycles $\mu_1$ and $\mu_2$ is $n_i$.
    Therefore, $\operatorname{parity}(\lambda\tau) = (\operatorname{parity}(\lambda) - 1) \% 2$

* Case 4: $\tau$ intersects both $\sigma_i$ and $\sigma_j$, where $i<j$:

    The canonical cycle notation of $\lambda\tau$ is
    $\sigma_1\ldots\sigma_{i-1}\mu\sigma_{i+1}\ldots\sigma_{j-1}\sigma_{j+1}\ldots\sigma_n$,
    where $\mu$ is a cycle of length $n_i + n_j$.
    Therefore, $\operatorname{parity}(\lambda\tau) = (\operatorname{parity}(\lambda) + 1) \% 2$

Therefore, $\operatorname{parity}(\lambda\tau)$ is different from $\operatorname{parity}(\lambda)$.

### Lemma 2: The parity of the product of $n$ transpositions is $n\%2$.

**Proof by induction**:

$P(n)$: Product of $n$ transpositions is $n\%2$.

**Base case**: A permutation with 0 transpositions is the identity permutation
and its parity is 0. $\implies P(0)$.

**Inductive step**:

Assume $P(n)$, where $n \ge 0$.
Let $\lambda\tau$ be a product of $n+1$ transpositions, where $\tau$ is a transposition.

\begin{align}
& \operatorname{parity}(\lambda\tau)
\\ &= (\operatorname{parity}(\lambda) + 1) \% 2 \tag{By lemma 1}
\\ &= (n + 1) \% 2 \tag{By induction hypothesis}
\\ &\Rightarrow P(n+1)
\end{align}

Since $P(0)$ and $P(n) \Rightarrow P(n+1)$, by mathematical induction, $P(n)$ holds $\forall n \ge 0$.

### Conclusion

We can therefore define the parity of a permutation as the parity of the number
of transpositions it can be written as the product of.
