Consider the optimization problem $P$:
\[ \min_{x \in \mathbb{R}^d} f(x) \textrm{ where } \forall i \in I, c_i(x) \ge 0 \wedge \forall j \in J, h_j(x) = 0 \]
The corresponding Lagrangian is
\[ L(x, \lambda, \mu) = f(x) - \lambda^Tc(x) - \mu^Th(x) \]
Define $g$ as
\[ g(\lambda, \mu) = \min_{x \in \mathbb{R}^d} L(x, \lambda, \mu) \]
Let $D$ be this optimization problem:
\[ \max_{\lambda, \mu} g(\lambda, \mu) \textrm{ where } g(\lambda, \mu) \neq -\infty \wedge \lambda \ge 0 \]
Then $D$ is said to be the dual of $P$.
