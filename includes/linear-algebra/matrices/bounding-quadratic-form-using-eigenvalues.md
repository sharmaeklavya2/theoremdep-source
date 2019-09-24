Let $A$ be a $n$ by $n$ real symmetric matrix.
Let $\lambda_{\textrm{min}}$ and $\lambda_{\textrm{max}}$
be the minimum and maximum eigenvalues of $A$. Then
\[ \forall u \in \mathbb{R}^n, \lambda_{\textrm{min}}u^Tu \le u^TAu \le \lambda_{\textrm{max}}u^Tu \]

## Proof

Since $A$ is real and symmetric, it is orthogonally diagonalizable.
Specifically, let $[v_1, v_2, \ldots, v_n]$ be $n$ orthonormal eigenvectors of $A$
and let $[\lambda_1, \lambda_2, \ldots, \lambda_n]$ be the corresponding eigenvalues.
Let $P$ be the matrix whose $i^{\textrm{th}}$ column is $v_i$
and let $D$ be a diagonal matrix whose $i^{\textrm{th}}$ diagonal entry is $\lambda_i$.
Then $P$ and $D$ are real and $A = PDP^T$ and $P^TP = I$.

Let $v = P^Tu$. Then
\[ v^Tv = (P^Tu)^T(P^Tu) = u^T(PP^T)u = u^Tu \]
\[ u^TAu = u^T(PDP^T)u = (P^Tu)^TD(P^Tu) = v^TDv = \sum_{i=1}^n \lambda_i v_i^2 \]

Without loss of generality, assume that $\lambda_1 \ge \lambda_2 \ge \ldots \ge \lambda_n$.
\begin{align}
& \forall i, \lambda_n \le \lambda_i \le \lambda_1
\\ &\Rightarrow \sum_{i=1}^n \lambda_n v_i^2 \le \sum_{i=1}^n \lambda_i v_i^2 \le \sum_{i=1}^n \lambda_1 v_i^2
\\ &\Rightarrow \lambda_n v^Tv \le \sum_{i=1}^n \lambda_i v_i^2 \le \lambda_1 v^Tv
\\ &\Rightarrow \lambda_n u^Tu \le u^TAu \le \lambda_1 u^Tu
\end{align}
