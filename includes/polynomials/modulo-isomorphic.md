Let $F$ be a field.
Let $\phi: F[x]/p(x) \mapsto F[x]/p(x)F[x]$ where
$\phi(f(x)) = f(x) + p(x)F[x]$.
Then $\phi$ is an isomorphism.

## Proof

### $\phi$ is homomorphic

\begin{align}
& \phi(f_1(x)) + \phi(f_2(x))
\\ &= (f_1(x) + p(x)F[x]) + (f_2(x) + p(x)F[x])
\\ &= (f_1(x) + f_2(x)) + p(x)F[x] \tag{coset addition}
\\ &= \phi(f_1(x) + f_2(x)) + p(x)F[x]
\end{align}

\begin{align}
& \phi(f_1(x))\phi(f_2(x))
\\ &= (f_1(x) + p(x)F[x])(f_2(x) + p(x)F[x])
\\ &= f_1(x)f_2(x) + p(x)F[x] \tag{coset multiplication}
\\ &= \phi(f_1(x)f_2(x))
\end{align}

### $\phi$ is injective

\begin{align}
& \phi(f_1(x)) = \phi(f_2(x))
\\ &\Rightarrow f_1(x) + p(x)F[x] = f_2(x) + p(x)F[x]
\\ &\Rightarrow (f_1(x)-f_2(x)) + p(x)F[x] = p(x)F[x] \tag{coset subtraction}
\\ &\Rightarrow f_1(x) - f_2(x) \in p(x)F[x]
\\ &\Rightarrow \exists q(x) \in F[x], f_1(x) - f_2(x) = p(x)q(x)
\end{align}

\begin{align}
& f_1(x), f_2(x) \in F[x]/p(x)
\\ &\Rightarrow (\deg(f_1) < \deg(p) \wedge \deg(f_2) < \deg(p))
\\ &\Rightarrow \deg(f_1 - f_2) \le \max(\deg(f_1), \deg(f_2)) < \deg(p)
\\ &\Rightarrow \deg(pq) < \deg(p)
\\ &\Rightarrow \deg(p) + \deg(q) < \deg(p)
\\ &\Rightarrow \deg(q) < 0
\\ &\Rightarrow q = 0
\\ &\Rightarrow pq = f_1 - f_2 = 0
\\ &\Rightarrow f_1 = f_2
\end{align}

### $\phi$ is surjective

Let $f(x) + p(x)F[x] \in F[x]/p(x)F[x]$.
By polynomial division theorem, $f = pq + r$ and $\deg(r) < \deg(p) \Rightarrow r(x) \in F[x]/p(x)$.

\begin{align}
& f(x) - r(x) = p(x)q(x) \in p(x)F[x]
\\ &\Rightarrow (f(x) - r(x)) + p(x)F[x] = p(x)F[x]
\\ &\Rightarrow f(x) + p(x)F[x] = r(x) + p(x)F[x] = \phi(r)
\end{align}
