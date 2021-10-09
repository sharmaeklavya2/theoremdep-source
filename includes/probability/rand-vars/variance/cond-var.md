<span class="invisible">
$\newcommand{\Var}{\operatorname{Var}}$
$\newcommand{\E}{\operatorname{E}}$
</span>
Let $X$ be a random variable on $(\Omega, \mathcal{F}, \Pr)$ and $A$ be an event.
Then $\Var(X \mid A)$ is the same as $\Var(X)$,
except that the probability measure for computing $\Var$
is $\Pr_{|A}$ instead of $\Pr$.

Equivalently, $\Var(X \mid A) = \E((X-\E(X \mid A))^2 \mid A) = \E(X^2 \mid A) - \E(X \mid A)^2$.

Let $X$ be a real-valued random variable, and $Y$ be a random variable.
Define $g(y) = \Var(X \mid Y=y)$. Then $\Var(X \mid Y)$ is defined as the random variable $g(Y)$.
