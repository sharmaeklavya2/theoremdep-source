Let $G$ be a group. Let $S$ be a subgroup of $G$ and $N$ be a normal subgroup of $G$.
Then the following hold:

1.  $SN$ is a subgroup of $G$.
2.  $S \cap N$ is a normal subgroup of $S$.
3.  $SN/N \cong S/(S \cap N)$.

## Proof or result 1

$SN$ is a non-empty subset of $G$.

Let $s_1n_1, s_2n_2 \in SN$ where $s_1, s_2 \in S$ and $n_1, n_2 \in N$.

\begin{align}
& (s_1n_1)(s_2n_2)^{-1}
\\ &= s_1n_1n_2^{-1}s_2^{-1}
\\ &= s_1ns_2^{-1} \tag{where $n = n_1n_2^{-1} \in N$}
\\ &= s_1s_2^{-1}n' \tag{where $n' \in N$, because $N$ is normal in $G$}
\\ &= sn' \tag{where $s = s_1s_2^{-1} \in S$}
\\ &\in SN
\end{align}

Therefore, $SN$ is a subgroup of $G$.

## Proof of result 2

$S \cap N$ is a non-empty subset of $S$.

\begin{align}
& h_1, h_2 \in S \cap N
\\ &\Rightarrow h_1, h_2 \in S \wedge h_1, h_2 \in N
\\ &\Rightarrow h_1h_2^{-1} \in S \wedge h_1h_2^{-1} \in N \tag{because $S$ and $N$ are subgroups of $G$}
\\ &\Rightarrow h_1h_2^{-1} \in S \cap N
\end{align}

Therefore, $S \cap N$ is a subgroup of $S$.

Let $s \in S$ and $h \in S \cap N$.

$shs^{-1} \in S$, because of closure of $S$.
$shs^{-1} \in N$, because $N$ is normal in $G$.

Therefore, $shs^{-1} \in S \cap N$, which means $S \cap N$ is normal in $S$.

## Proof of result 3

\[ SN/N = \{snN: s \in S, n \in N\} = \{sN: s \in S \} \]

Let $\psi: S \mapsto G/N$ such that $\psi(s) = sN$.
Then $\psi(S) = \{sN: s \in S\} = SN/N$.

\begin{align}
& \psi(s_1s_2)
\\ &= (s_1s_2)N
\\ &= (s_1N)(s_2N) \tag{because $N$ is normal in $G$}
\\ &= \psi(s_1)\psi(s_2)
\end{align}

Therefore, $\psi$ is a homomorphism.

\begin{align}
& \psi(s) = \operatorname{id}(G/N) = N
\\ &\Rightarrow sN = N
\\ &\Rightarrow s \in N
\\ &\Rightarrow s \in S \cap N
\end{align}

Therefore, $\operatorname{ker}(\psi) = S \cap N$.

By the first isomorphism theorem,
\[ \psi(S) \cong S/\operatorname{ker}(\psi) \Rightarrow SN/N \cong S/(S \cap N) \]
