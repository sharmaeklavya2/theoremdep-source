Let $B = [u_1, u_2, \ldots, u_n]$ be a basis of a vector space $V$.
Let $w = \sum_{i=1}^n \alpha_i u_i$.
Then $B' = [u_1, u_2, \ldots, u_{k-1}, w, u_{k+1}, \ldots, u_n]$ is a basis of $V$ iff $\alpha_k \neq 0$.

## Proof

Without loss of generality, assume $k = n$.
Since $B'$ contains $n = \dim(V)$ vectors, $B'$ is a basis of $V$
iff $B'$ is linearly independent.
We will now try to prove that $\alpha_n = 0$ iff $B'$ is linearly dependent.

Assume $\alpha_n = 0$. Then $b = \sum_{i=1}^{n-1} \alpha_i u_i$,
so $B'$ is linearly dependent.

Let $B'$ be linearly dependent.
Then for some non-zero vector $[\mu_1, \mu_2, \ldots, \mu_n]$, we have
\begin{align}
& \sum_{i=1}^{n-1} \mu_iu_i + \mu_nb_n = 0
\\ &\iff \sum_{i=1}^{n-1} \mu_iu_i + \mu_n\left(\sum_{i=1}^n \alpha_iu_i\right) = 0
\\ &\iff \sum_{i=1}^{n-1} (\mu_i + \mu_n\alpha_i)u_i + \mu_n\alpha_nu_n = 0
\end{align}

Since $B$ is a linearly independent, we get $\mu_n\alpha_n = 0$ and $\mu_i + \mu_n\alpha_i = 0$
for all $1 \le i < n$.
If $\mu_n = 0$, then $\mu_i = -\mu_n\alpha_i = 0$, which is a contradiction
since $[\mu_1, \mu_2, \ldots, \mu_n]$ is a non-zero vector.
Hence, $\mu_n \neq 0$, and so $\alpha_n = 0$.
