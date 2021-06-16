<span class="invisible">
$\newcommand{\Fcal}{\mathcal{F}}$
$\newcommand{\Dhat}{\widehat{D}}$
$\newcommand{\Shat}{\widehat{S}}$
$\newcommand{\That}{\widehat{T}}$
$\newcommand{\Fcalhat}{\widehat{\mathcal{F}}}$
</span>
Let $X_1$ and $X_2$ be random variables over $\sigma$-algebras
$(D_1, \Fcal_1)$ and $(D_2, \Fcal_2)$, respectively.
Let $(\Dhat, \Fcalhat)$ be a $\sigma$-algebra.
Let $f: D_2 \mapsto \Dhat$ be a measurable function from
$(D_2, \Fcal_2)$ to $(\Dhat, \Fcalhat)$.

If $X_1$ and $X_2$ are independent, then $X_1$ and $f(X_2)$ are also independent.

# Proof

Let $S_1 \in \Fcal_1$ and $\Shat \in \Fcalhat$. We will prove that
$\Pr(X_1 \in S_1 \cap f(X_2) \in \Shat) = \Pr(X_1 \in S_1)\Pr(f(X_2) \in \Shat)$.
This would imply that $X_1$ and $f(X_2)$ are independent.

For any set $\That \subseteq \Dhat$, define
$f^{-1}(\That) = \{x_2 \in D_2: f(x_2) \in \That\}$.
Therefore, $x_2 \in f^{-1}(\That) \iff f(x_2) \in \That$.
Since $f$ is measurable, we get that $\That \in \Fcalhat \implies f^{-1}(\That) \in \Fcal_2$.
Let $S_2 = f^{-1}(\Shat)$. Therefore, $S_2 \in \Fcal_2$.

\begin{align}
& \Pr(X_1 \in S_1 \cap f(X_2) \in \Shat)
\\ &= \Pr(X_1 \in S_1 \cap X_2 \in S_2)
\\ &= \Pr(X_1 \in S_1)\Pr(X_2 \in S_2)  \tag{since $X_1$ and $X_2$ are independent}
\\ &= \Pr(X_1 \in S_1)\Pr(f(X_2) \in \Shat)
\end{align}
