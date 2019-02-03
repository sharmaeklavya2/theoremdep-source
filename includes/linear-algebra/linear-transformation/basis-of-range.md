Let $T: U \mapsto V$ be a linear transformation with kernel $K$
where $U$ has a finite basis of size $n$.

Let $P = \{u_1, u_2, \ldots, u_k\}$ be a basis of $K$.
Since $P$ is a linearly independent subset of $U$,
it can be expanded to form a basis of $U$
(this also explains why $P$ should be finite).
Let $Q = \{u_{k+1}, \ldots, u_n\}$ such that $P \cup Q$ is a basis of $U$.

Then $T(Q)$ is a basis of $T(U)$.
Consequently, $\operatorname{dim}(T(U)) = |Q| = n-k$.

## Proof

\begin{align}
& \sum_{i=k+1}^n a_iT(u_i) = 0
\\ &\Rightarrow T\left(\sum_{i=k+1}^n a_iu_i\right) = 0
\\ &\Rightarrow \sum_{i=k+1}^n a_iu_i \in K
\\ &\Rightarrow \sum_{i=k+1}^n a_iu_i = \sum_{i=1}^k (-a_i)u_i \tag{for some $a_1, a_2, \ldots, a_k$}
\\ &\Rightarrow \sum_{i=1}^n a_iu_i = 0
\\ &\Rightarrow a_i = 0 \forall i
\end{align}
Therefore, $T(Q)$ is linearly independent.

\begin{align}
u \in U &\Rightarrow u = \sum_{i=1}^n a_iu_i \tag{for some $a_1, a_2, \ldots, a_n$}
\\ &\Rightarrow T(u) = T\left(\sum_{i=1}^n a_iu_i \right)
\\ &\Rightarrow T(u) = \sum_{i=1}^n a_iT(u_i)
\\ &\Rightarrow T(u) = \sum_{i=k+1}^n a_iT(u_i)
\\ &\Rightarrow T(u) \in \operatorname{span}(T(Q))
\end{align}

Therefore, $T(Q)$ spans $T(U)$.
Therefore, $T(Q)$ is a basis of $T(U)$.
