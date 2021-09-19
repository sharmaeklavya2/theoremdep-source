<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Xbar}{\overline{X}}$
$\newcommand{\Ybar}{\overline{Y}}$
</span>
Let $X$ and $Y$ be two complex-valued random variables.
Then $|\E(X\Ybar)|^2 \le \E(|X|^2)\E(|Y|^2)$.

## Proof

Let $V$ be the set of all complex-valued random variables.

**Lemma 1**: $V$ is a vector space over $\mathbb{C}$.

*Proof*. $(V, +)$ is an abelian group because

* Addition of random variables gives another random variable.
* Addition of random variables is associative.
* 0 is an additive identity.
* $-X$ is the additive inverse of random variable $X$.
* Addition of random variables is commutative.

$V$ is a vector space because

* $(V, +)$ is an abelian group.
* Scalar multiplication is associative.
* Distributivity holds.
* 1 is a unit scalar for $V$.

<p style="text-align: right;">□</p>

For two random variables $X$ and $Y$,
define the inner-product $\langle X, Y \rangle$ as $\E(X\Ybar)$.

**Lemma 2**: $(V, \langle \cdot \rangle)$ is an inner-product space.

*Proof*.

* Conjugate symmetry:
\[ \langle X, Y \rangle = \E(X\Ybar) = \overline{\E(Y\Xbar)} = \overline{\langle Y, X \rangle}. \]
* Linearity in first argument (follows from linearity of expectation of random variables):
\[ \langle X_1 + X_2, Y \rangle = \E((X_1 + X_2)\Ybar) = \E(X_1\Ybar) + \E(X_2\Ybar)
= \langle X_1, Y \rangle + \langle X_2, Y \rangle. \]
\[ \langle aX, Y \rangle = \E((aX)\Ybar) = a\E(X\Ybar) = a \langle X, Y \rangle. \]
* Positive definiteness:
\[ \langle X, X \rangle = \E(|X|^2) \ge 0. \]
\[ \langle X, X \rangle = 0 \iff \E(|X|^2) = 0 \iff X = 0. \tag*{□} \]

On applying the Cauchy-Schwarz inequality for inner-product spaces, we get
\[ |\E(X\Ybar)|^2 = |\langle X, Y \rangle|^2
\le \langle X, X \rangle \langle Y, Y \rangle
= \E(|X|^2)\E(|Y|^2). \]
