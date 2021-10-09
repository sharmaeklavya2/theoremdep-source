<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
</span>
Let $f: D \mapsto \mathbb{R}$ be a function, where $D \subseteq \mathbb{R}$.

Let $(b, c) \subseteq D$, where $b < c$. Then $\limsup_{x \to b} f(x)$ is defined as
\[ \limsup_{x \to b} f(x) = C \iff
    \forall \eps > 0, \exists \delta > 0, \forall x \in (b, b + \delta],
    |f(x) - C| \le \eps. \]
If no such $C$ exists, then $\limsup_{x \to b} f(x)$ is not defined.
$\limsup_{x \to b}$ is also written as $\lim_{x \to b^+}$.
It can be proven that if $\limsup$ exists, it is unique.

Let $(a, b) \subseteq D$, where $a < b$. Then $\liminf_{x \to b} f(x)$ is defined as
\[ \liminf_{x \to b} f(x) = C \iff
    \forall \eps > 0, \exists \delta > 0, \forall x \in [b - \delta, b),
    |f(x) - C| \le \eps. \]
If no such $C$ exists, then $\liminf_{x \to b} f(x)$ is not defined.
$\liminf_{x \to b}$ is also written as $\lim_{x \to b^-}$.
It can be proven that if $\liminf$ exists, it is unique.

Let $a \le b \le c$ and $a < c$ and $(a, c) - \{b\} \subseteq D$. Then
\[ \lim_{x \to b} f(x) = C \iff \forall \eps > 0, \exists \delta > 0,
(0 \le |x - b| \le \delta \implies |f(x) - C| \le \eps. \]
If no such $C$ exists, then $\lim_{x \to b} f(x)$ is not defined.
It can be proven that if $\lim$ exists, it is unique.

If $a < b < c$, and $(a, c) - \{b\} \subseteq D$,
then it can be proven that $\lim_{x \to b} f(x) = C$ iff
$\limsup_{x \to b} f(x) = \liminf_{x \to b} f(x) = C$.

$f$ is said to be continuous at $z$ iff $\lim_{x \to z} f(x) = f(z)$.
$f$ is continuous on a set $S$ iff $f$ is continuous at $z$ for every $z \in S$.

## Proof that if $\limsup$ exists, then it is unique

Let $(b, c) \subseteq D$, where $b < c$. Let $C_1$ and $C_2$ be two $\limsup$s, i.e.,
\[ \forall \eps > 0, \exists \delta > 0, \forall x \in (b, b + \delta],
    (|f(x) - C_1| \le \eps \textrm{ and } |f(x) - C_2|). \]
But then $|C_1 - C_2| = |(f(x) - C_2) - (f(x) - C_1)| \le |f(x) - C_1| + |f(x) - C_2| \le 2\eps$,
so $\eps \ge |C_1 - C_2|/2$, which contradicts the '$\forall \eps > 0$' part of the definition.

## Proof that if $\liminf$ exists, then it is unique

Proof is analogous to that of $\limsup$.

## Proof that if $\lim$ exists, then it is unique

Proof is analogous to that of $\limsup$.
