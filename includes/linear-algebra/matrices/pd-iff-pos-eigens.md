Let $A$ be a real $n$ by $n$ symmetric matrix.
This means that all its eigenvalues are real.
Let $\lambda_{\textrm{min}}$ and $\lambda_{\textrm{max}}$ be the minimum and maximum eigenvalues.
Then

* $A$ is positive definite iff $\lambda_{\textrm{min}} > 0$.
* $A$ is positive semidefinite iff $\lambda_{\textrm{min}} \ge 0$.
* $A$ is negative definite iff $\lambda_{\textrm{max}} < 0$.
* $A$ is negative semidefinite iff $\lambda_{\textrm{max}} \le 0$.

## Proof

\[ \forall u \in \mathbb{R}^n, \lambda_{\textrm{min}}u^Tu \le u^TAu \le \lambda_{\textrm{max}}u^Tu \]
Also, the above bounds are tight. The theorems of this page directly follow from the above bound.
