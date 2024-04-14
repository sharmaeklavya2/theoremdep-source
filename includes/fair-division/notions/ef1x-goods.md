In fair division of indivisible goods, an allocation $A$ is said to be

* EF1-fair to agent $i$ iff
\[ v_i(A_i) ≥ \max_{j ≠ i} \begin{cases}
\min_{g \in A_j} v_i(A_j \setminus \{g\}) & \textrm{ if } A_j \neq \emptyset
\\ 0 & \textrm{ if } A_j = \emptyset\end{cases}. \]
* EFX-fair to agent $i$ iff
\[ v_i(A_i) ≥ \max_{j ≠ i} \begin{cases}
\max_{g \in A_j} v_i(A_j \setminus \{g\}) & \textrm{ if } A_j \neq \emptyset
\\ 0 & \textrm{ if } A_j = \emptyset\end{cases}. \]

Furthermore, if agent $i$'s valuation function is submodular, we say that
$A$ is EFX<sup>0</sup>-fair to agent $i$ iff
\[ v_i(A_i) ≥ \max_{j ≠ i} \begin{cases}
\max_{g \in A_j: v_i(g) > 0} v_i(A_j \setminus \{g\})
    & \textrm{ if } A_j \neq \emptyset \textrm{ and } v_i(g) > 0 \textrm{ for some } g \in A_j
\\ 0 & \textrm{ otherwise} \end{cases}. \]

It is trivial to see that EF implies EFX, and EFX implies EF1.
For submodular valuations, EFX implies EFX<sup>0</sup>.

Some people actually mean EFX<sup>0</sup> when they say EFX.
