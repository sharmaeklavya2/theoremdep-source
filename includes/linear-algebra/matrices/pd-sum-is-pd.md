Let $A$ and $B$ be real $n$ by $n$ matrices. Then

* If $A$ and $B$ are positive definite, then $A+B$ is positive definite.
* If $A$ and $B$ are positive semidefinite, then $A+B$ is positive semidefinite.
* If $A$ and $B$ are negative definite, then $A+B$ is negative definite.
* If $A$ and $B$ are negative semidefinite, then $A+B$ is negative semidefinite.

## Proof

If $A$ and $B$ are positive definite,
\[ \forall u \in \mathbb{R}^n - \{0\}, u^T(A+B)u = u^TAu + u^TBu > 0 + 0 = 0 \]
If $A$ and $B$ are positive semidefinite,
\[ \forall u \in \mathbb{R}^n, u^T(A+B)u = u^TAu + u^TBu \ge 0 + 0 = 0 \]
If $A$ and $B$ are negative definite,
\[ \forall u \in \mathbb{R}^n - \{0\}, u^T(A+B)u = u^TAu + u^TBu < 0 + 0 = 0 \]
If $A$ and $B$ are negative semidefinite,
\[ \forall u \in \mathbb{R}^n, u^T(A+B)u = u^TAu + u^TBu \le 0 + 0 = 0 \]
