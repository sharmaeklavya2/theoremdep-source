<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\Otild}{\widetilde{O}}$
$\newcommand{\Sum}{\operatorname{sum}}$
$\newcommand{\lin}{\operatorname{lin}}$
</span>
Let $I$ be a 1BP instance containing $n$ items.
Then we can obtain a feasible solution $x$ to the configuration LP of $I$,
such that $\Sum(x) \le (1+\eps)\lin(I)$.
Moreover, we can do this in time
\[ O\left(\frac{n^5}{\eps^4}\log\left(\frac{n}{\eps}\right)^3\right). \]

Proof follows directly from the dependencies.
