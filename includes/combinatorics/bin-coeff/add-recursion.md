For $n \ge 1$,
\[ \binom{n}{k} = \binom{n-1}{k} + \binom{n-1}{k-1} \]

On rearranging terms and replacing $n$ by $n+1$, we get
\[ \binom{n}{k} = \binom{n+1}{k} - \binom{n}{k-1} \]
On rearranging terms and replacing $n$ by $n+1$ and $k$ by $k+1$, we get
\[ \binom{n}{k} = \binom{n+1}{k+1} - \binom{n}{k+1} \]

## Combinatorial proof

When $k < 0$ or $k > n$, all 3 terms are 0, so the identity holds.
For $k = 0$, $\binom{n}{k} = 1$ and $\binom{n-1}{k} + \binom{n-1}{k-1} = 1 + 0 = 1$.

For the case when $1 \le k \le n$, we have a combinatorial proof.
Suppose we have a set $S$ of $n$ distinct elements. Let $a \in S$.

* The number of subsets of $S$ of size $k$ is $\binom{n}{k}$.
* The number of subsets of $S$ of size $k$ which don't contain $a$
is the number of subsets of $S-\{a\}$ of size $k$ which is $\binom{n-1}{k}$.
* The number of subsets of $S$ of size $k$ which contain $a$
is the number of subsets of $S-\{a\}$ of size $k-1$ which is $\binom{n-1}{k-1}$.

Therefore, $\binom{n}{k} = \binom{n-1}{k} + \binom{n-1}{k-1}$.

## Alternative proof outline

An algebraic proof is also possible by using the decrement identities
to express $\binom{n-1}{k}$ and $\binom{n-1}{k-1}$ in terms of $\binom{n}{k}$.
