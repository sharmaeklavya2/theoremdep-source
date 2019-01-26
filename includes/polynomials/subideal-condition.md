Let $R$ be a ring and $p(x), q(x) \in R[x]$.

Then $p(x) \mid q(x) \iff q(x)F[x] \subseteq p(x)F[x]$.

## Proof

\begin{align}
& p(x) \mid q(x)
\\ &\Rightarrow \exists r(x) \in F[x], q(x) = p(x)r(x)
\\ &\Rightarrow \forall f(x) \in F[x], q(x)f(x) = p(x)r(x)f(x) \in p(x)F[x]
\\ &\Rightarrow q(x)F[x] \subseteq p(x)F[x]
\end{align}

\begin{align}
& q(x)F[x] \subseteq p(x)F[x]
\\ &\Rightarrow q(x) \in p(x)F[x]
\\ &\Rightarrow \exists r(x) \in F[x], q(x) = p(x)r(x)
\\ &\Rightarrow p(x) \mid q(x)
\end{align}
