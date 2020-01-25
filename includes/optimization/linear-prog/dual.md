The dual of the linear program
\[ P: \max \left\{ c^Tx: Ax \le b, x \ge 0 \right\} \]
is
\[ D: \min \left\{ b^Ty: A^Ty \ge c, y \ge 0 \right\} \]
Also, the dual of $D$ is $P$.

For other kinds of linear programs, the dual can either be obtained by
first converting to standard form, or by applying this method:
<http://www.cs.columbia.edu/coms6998-3/lpprimer.pdf>.

This can be proven by a straightforward application of the definition
of duality for general optimization problems.
The proof is too tedious to write, so I'm omitting it here.
