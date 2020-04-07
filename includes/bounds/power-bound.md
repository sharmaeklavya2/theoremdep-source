Let $0 \le a \le 1$.
\begin{align}
\forall x \ge -1, &\quad (1+x)^a \le 1+ax
\\ \forall 0 \le x \le k, &\quad 1 + \frac{ax}{k+1} \le 1 + \frac{\ln(1+k)}{k}ax \le (1+x)^a
\end{align}

## Proof

### Upper bound

Let $f(x) = (1+ax) - (1+x)^a$.
We would like to prove that $f(x) \ge 0$ for all $x$.

\[ f'(x) = a - a(1+x)^{a-1} = a\left(1 - (1+x)^{-(1-a)}\right) \]
\[ x \ge 0 \implies 1+x \ge 1 \implies (1+x)^{-(1-a)} \le 1
\implies f'(x) \ge 0 \]
\[ -1 \le x \le 0 \implies 0 \le 1+x \le 1 \implies (1+x)^{-(1-a)} \ge 1
\implies f'(x) \le 0 \]
Since $f(0) = 0$ and $f(x)$ increases as we go away from 0,
$\forall x, f(x) \ge 0$.

### Lower bound

Let $\gamma = \frac{1}{k}\ln(1+k)$.
We'll prove that $\forall 0 \le x \le k, \; e^{\gamma x} \le 1+x$.
That would imply (using the bound on exponential) that
\[ 1+\gamma ax \le e^{\gamma ax} \le \left(e^{\gamma x}\right)^a \le (1+x)^a \]

Let $g(x) = e^{\gamma x} - (1+x)$. $g(0) = 0$. $g(k) = e^{\gamma k} - (1+k) = 0$.

$g''(x) = \gamma^2 e^{\gamma x} > 0$ and $g(0) = g(k) = 0$.
Therefore, $g(x) \le 0$ for $x \in [0, k]$.
Therefore, $e^{\gamma x} \le 1+x$ for $x \in [0, k]$.

By the bound on log, we get $\frac{k}{k+1} \le \ln(1+k)$.
Therefore,
\[ 1 + \frac{ax}{k+1} \le 1 + \frac{\ln(1+k)}{k}ax \]
