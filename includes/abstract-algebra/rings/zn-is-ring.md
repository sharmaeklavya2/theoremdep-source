$\mathbb{Z}_n = \{0, 1, \ldots, n-1\}$.
Let $a, b \in \mathbb{Z}_n$.
The sum of $a$ and $b$ is defined as $\operatorname{add}(a, b) = (a+b)\%n$.
The product of $a$ and $b$ is defined as $\operatorname{mult}(a, b) = (ab)\%n$.

Under these operations, $\mathbb{Z}_n$ forms a commutative ring with unity.

## Lemmas

\begin{align}
& a \equiv b \pmod{n}
\\ &\iff n \mid (a - b)
\\ &\iff n \mid (a\%n + n\left\lfloor\frac{a}{n}\right\rfloor - b\%n - n\left\lfloor\frac{b}{n}\right\rfloor)
\\ &\iff n \mid (a\%n - b\%n)
\\ &\iff a\%n - b\%n = 0
\\ &\iff a\%n = b\%n
\end{align}

This is because $a\%n - b\%n \in \{-(n-1), -(n-2), \ldots, n-2, n-1\}$
and the only divisor of $n$ in this set is 0.

\[ n \mid (a - a\%n) \iff a \equiv a\%n \pmod{n} \]

## Proof that $\mathbb{Z}_n$ is a ring

* Closure: $\forall x \in \mathbb{Z}, x \% n \in \mathbb{Z}_n$.
Therefore, $\operatorname{add}(a, b) = (a+b) \% n \in \mathbb{Z}_n$
and $\operatorname{mult}(a, b) = (ab)\%n \in \mathbb{Z}_n$.

* $+$ commutativity: $\operatorname{add}(a, b) = (a+b) \% n = (b+a) \% n = \operatorname{add}(b, a)$.

* $+$ Associativity:
    \begin{align}
    & (a+b)\%n \equiv a+b \pmod{n}
    \\ &\Rightarrow (a+b)\%n + c \equiv a+b+c \pmod{n}
    \\ &\Rightarrow ((a+b)\%n + c)\%n = (a+b+c)\%n
    \end{align}

    \begin{align}
    & (b+c)\%n \equiv b+c \pmod{n}
    \\ &\Rightarrow a+(b+c)\%n \equiv a+b+c \pmod{n}
    \\ &\Rightarrow (a+(b+c)\%n)\%n = (a+b+c)\%n
    \end{align}

    Therefore, $((a+b)\%n+c)\%n = (a+(b+c)\%n)\%n$.

* Additive identity: 0
* Additive inverse:
    $\operatorname{inv}_+{0} = 0$.
    When $x \neq 0$, $\operatorname{inv}_+{x} = n-x$.

Therefore, $\mathbb{Z}_n$ is an abelian group under addition.

* $\times$ commutativity: $\operatorname{mult}(a, b) = (ab) \% n = (ba) \% n = \operatorname{mult}(ba)$

* $\times$ Associativity:
    \begin{align}
    & (ab)\%n \equiv ab \pmod{n}
    \\ &\Rightarrow ((ab)\%n) c \equiv abc \pmod{n}
    \\ &\Rightarrow (((ab)\%n) c)\%n \equiv (abc)\%n \pmod{n}
    \end{align}

    \begin{align}
    & (bc)\%n \equiv bc \pmod{n}
    \\ &\Rightarrow a ((bc)\%n) \equiv abc \pmod{n}
    \\ &\Rightarrow (a((ab)\%n))\%n \equiv (abc)\%n \pmod{n}
    \end{align}

    Therefore, $(((ab)\%n)c)\%n = (a((bc)\%n))\%n$.

* Unity: 1

* Distributivity:
    \begin{align}
    & (a+b)\%n \equiv a+b \pmod{n}
    \\ &\Rightarrow (a+b)\%n c \equiv (a+b)c \pmod{n}
    \\ &\Rightarrow ((a+b)\%n c)\%n = ((a+b)c)\%n
    \end{align}

    \begin{align}
    & (ac)\%n \equiv ac \wedge (bc)\%n \equiv bc \pmod{n}
    \\ &\Rightarrow (ac)\%n + (bc)\%n \equiv (ac+bc) \pmod{n}
    \\ &\Rightarrow ((ac)\%n + (bc)\%n)\%n = (ac+bc)\%n = ((a+b)c)\%n
    \end{align}

    Therefore, $(((a+b)\%n)c)\%n = ((ac)\%n + (bc)\%n)\%n$.

Therefore, $\mathbb{Z}_n$ is a commutative ring with unity.
