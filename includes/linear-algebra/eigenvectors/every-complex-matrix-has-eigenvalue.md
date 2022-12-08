Every matrix over $\mathbb{C}$ has at least one eigenvalue.

## Proof

Let $A$ be an $n$ by $n$ matrix over $\mathbb{C}$.

Let $p_A(x) = |xI - A|$ be the characteristic polynomial of $A$.
$p_A$ is a monic polynomial of degree $n$.

By the fundamental theorem of algebra,
\[ p_A(x) = \prod_{i=1}^n (x - a_i) \]
where $\forall i, a_i \in \mathbb{C}$.

By the Cayley-Hamilton theorem, $p_A(A) = 0$.

\[ p_A(A) = 0
\implies \prod_{i=1}^n (A-a_iI) = 0
\implies \left|\prod_{i=1}^n (A-a_iI)\right| = 0
\implies \prod_{i=1}^n |A-a_iI| = 0
\]

$\exists i, |A-a_iI| = 0$, because $\mathbb{C}$ is a field
and a field has no zero-divisors.

Let $a_i = \lambda$.

\begin{align}
& |A-\lambda I| = 0
\\ &\Rightarrow \operatorname{rank}(A-\lambda I) < n
\\ &\Rightarrow \exists u \neq 0, (A - \lambda I)u = 0
\\ &\Rightarrow \exists u \neq 0, Au = (\lambda I)u = \lambda u
\end{align}

Therefore, $(\lambda, u)$ is an eigenvalue-eigenvector pair for $A$.
