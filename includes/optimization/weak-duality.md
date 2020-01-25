Consider the optimization problem $P$:
\[ \min_{x \in \mathbb{R}^d} f(x) \textrm{ where } \forall i \in I, c_i(x) \ge 0 \wedge \forall j \in J, h_j(x) = 0 \]
The corresponding Lagrangian is
\[ L(x, \lambda, \mu) = f(x) - \lambda^Tc(x) - \mu^Th(x) \]
Let $D$ be the dual of $P$:
\[ \max_{\lambda, \mu} g(\lambda, \mu) \textrm{ where } g(\lambda, \mu) \neq -\infty \wedge \lambda \ge 0 \]
where
\[ g(\lambda, \mu) = \min_{x \in \mathbb{R}^d} L(x, \lambda, \mu) \]

Let $x_0$ be a feasible solution to $P$ and $(\lambda_0, \mu_0)$ be feasible solution to $D$. Then
\[ g(\lambda_0, \mu_0) \le L(x_0, \lambda_0, \mu_0) \le f(x_0) \]

## Proof

\begin{align}
& g(\lambda_0, \mu_0)
\\ &= \min_{x \in \mathbb{R}^d} L(x, \lambda_0, \mu_0)
\\ &\le L(x_0, \lambda_0, \mu_0)
\\ &= f(x_0) - \lambda_0^Tc(x_0) - \mu^Th(x_0)
\\ &\le f(x_0) \tag{$\lambda_0 \ge 0 \wedge c(x_0) \ge 0 \wedge h(x_0) = 0$ by feasibility}
\end{align}
