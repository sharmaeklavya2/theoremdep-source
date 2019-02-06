Let $U$ and $V$ be vector spaces with bases $P$ and $Q$ respectively.
Let $\phi$ be a bijection from $P$ to $Q$.
If $P$ and $Q$ are finite, a bijection exists between them iff $|P| = |Q|$;
the bijection maps the $i^{\textrm{th}}$ element of $P$ to the $i^{\textrm{th}}$ element of $Q$.

A basis changer $T: U \mapsto V$ is a bijection of the form:

\[ T\left(\sum_{p \in P} a_p p \right) = \sum_{p \in P} a_p \phi(p) \]

## Proof

Since every vector in $U$ can be expressed as a unique linear combination of vectors in $P$,
$T$ is well-defined.

Since every vector in $Q$ can be expressed as a unique linear combination of vectors in $Q$,
$T$ is onto.

\begin{align}
& T\left(\sum_{p \in P} a_p p\right) = T\left(\sum_{p \in P} b_p p\right)
\\ &\Rightarrow \sum_{p \in P} a_p \phi(p) = \sum_{p \in P} b_p \phi(p)
\\ &\Rightarrow \forall p \in P, a_p = b_p \tag{$\because$ of unique representation in $V$}
\\ &\Rightarrow \sum_{p \in P} a_p p = \sum_{p \in P} b_p p
\end{align}

Therefore, $T$ is one-to-one. Therefore, $T$ is a bijection.
