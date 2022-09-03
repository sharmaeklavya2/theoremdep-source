Let $A \in \mathbb{R}^{m \times n}$. Let $I \subseteq [n]$ and $J \subseteq [m]$.
Then the dual of the linear program
\[ P: \min_{x: x_J \ge 0} c^Tx \quad\textrm{where}\quad
((Ax)_i \ge b_i, \forall i \in I) \textrm{ and } ((Ax)_i = b_i, \forall i \in [n]-I) \]
is
\[ D: \max_{y: y_I \ge 0} b^Ty \quad\textrm{where}\quad
((A^Ty)_j \le c_j, \forall j \in J) \textrm{ and } ((A^Ty)_j = c_j, \forall j \in [m]-J) \]
Also, the dual of $D$ is $P$.

As a special case, on setting $J = [n]$ and $I = [m]$, we get that the dual of
\[ P: \min_{x \ge 0} c^Tx \textrm{ where } Ax \ge b \]
is
\[ D: \max_{y \ge 0} b^Ty \textrm{ where } A^Ty \le c \]

Equivalently, we can obtain the dual by applying this method:
<http://www.cs.columbia.edu/coms6998-3/lpprimer.pdf>.
