Let $A$ and $B$ be real $n$ by $n$ symmetric matrices.
Then $A$, $B$ and $A+B$ have real eigenvalues.

* Let $\lambda^-$ and $\lambda^+$ be the minimum and maximum eigenvalues of $A$.
* Let $\mu^-$ and $\mu^+$ be the minimum and maximum eigenvalues of $B$.
* Let $\gamma^-$ and $\gamma^+$ be the minimum and maximum eigenvalues of $A+B$.

Then
\[ \lambda^- + \mu^- \le \gamma^- \le \gamma^+ \le \lambda^+ + \mu^+ \]

## Proof

Let $\lambda(X)$ be the set of eigenvalues of matrix $X$.

\begin{align}
& \lambda(A) \in [\lambda^-, \lambda^+] \wedge \lambda(B) \in [\mu^-, \mu^+]
\\ &\Rightarrow \lambda(A-\lambda^-I) \subseteq [0, \lambda^+ - \lambda^-]
\wedge \lambda(B-\mu^-I) \subseteq [0, \mu^+ - \mu^-] \tag{affine transformation}
\\ &\Rightarrow (A-\lambda^-I) \textrm{ is PSD } \wedge (B-\mu^-I) \textrm{ is PSD}
\\ &\Rightarrow (A-\lambda^-I) + (B - \mu^-I) \textrm{ is PSD}
\\ &\Rightarrow (A + B) - (\lambda^- + \mu^-)I \textrm{ is PSD}
\\ &\Rightarrow \lambda((A + B) - (\lambda^- + \mu^-)I) \subseteq [0, \infty)
\\ &\Rightarrow \lambda(A + B) \subseteq [\lambda^- + \mu^-, \infty)
\end{align}

\begin{align}
& \lambda(A) \in [\lambda^-, \lambda^+] \wedge \lambda(B) \in [\mu^-, \mu^+]
\\ &\Rightarrow \lambda(A-\lambda^+I) \subseteq [\lambda^- - \lambda^+, 0]
\wedge \lambda(B-\mu^+I) \subseteq [\mu^- - \mu^+, 0] \tag{affine transformation}
\\ &\Rightarrow (A-\lambda^+I) \textrm{ is NSD } \wedge (B-\mu^-I) \textrm{ is NSD}
\\ &\Rightarrow (A-\lambda^+I) + (B - \mu^+I) \textrm{ is NSD}
\\ &\Rightarrow (A + B) - (\lambda^+ + \mu^+)I \textrm{ is NSD}
\\ &\Rightarrow \lambda((A + B) - (\lambda^+ + \mu^+)I) \subseteq (-\infty, 0]
\\ &\Rightarrow \lambda(A + B) \subseteq (-\infty, \lambda^+ + \mu^+]
\end{align}

Therefore, $\lambda(A+B) \subseteq [\lambda^- + \mu^-, \lambda^+ + \mu^+]$.
