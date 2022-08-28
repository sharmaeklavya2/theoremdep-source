<span class="invisible">
$\newcommand{\defeq}{=}$
$\newcommand{\xhat}{\widehat{x}}$
</span>
Let $X \defeq \{x^{(i)} \in \mathbb{R}^n: 1 \le i \le m\}$.
Let $P$ be the convex hull of $X$.
Then $|x_j|$ is finite for all $j$ and all $x \in P$.

## Proof

Let $\beta \defeq \max_{i=1}^m \max_{j=1}^n |x^{(i)}_j|$.
Let $\xhat \in P$. Let $\xhat = \sum_{i=1}^m \alpha_i x^{(i)}$ such that
$\alpha_i \ge 0$ for all $i$ and $\sum_{i=1}^m \alpha_i = 1$. Then for any $j$,
\begin{align}
\|\xhat_j\| &= \left|\sum_{i=1}^m \alpha_i x^{(i)}_j\right|
\\ &\le \sum_{i=1}^m |\alpha_i x^{(i)}_j|
\\ &\le \sum_{i=1}^m \alpha_i \beta = \beta.
\end{align}
