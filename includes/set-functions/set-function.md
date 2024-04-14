<span class="invisible">
$\newcommand{\Fcal}{\mathcal{F}}$
$\newcommand{\Scal}{\mathcal{S}}$
</span>
Let $\Omega$ be a set (called the *ground set*) and let $\Fcal$ be a subset of the power-set of $\Omega$.
Then the function $f: \Fcal \to \mathbb{R}$ is called a set function over $(\Omega, \Fcal)$.

For notational convenience, we denote $f(e) = f(\{e\})$ for $e \in \Omega$.

If $\Omega$ is finite and $\Fcal$ is not specified, then we let $\Fcal$ be $2^{\Omega}$ by default.
If $\Omega$ is infinite, we assume $(\Omega, \Fcal)$ to be a sigma-algebra over $\Omega$.

For any sets $A, B \subseteq \Omega$, we define $f(A \mid B) := f(A \cup B) - f(B)$.
$f(A \mid B)$ is called $f$'s *marginal* for $A$ over $B$.
