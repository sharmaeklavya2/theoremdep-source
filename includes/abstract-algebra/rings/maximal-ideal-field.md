Let $R$ be a commutative ring with unity. Let $I$ be a proper ideal of $R$.

$I$ is defined to be a maximal ideal iff no proper ideal of $R$ is a proper superset of $I$.

$I$ is a maximal ideal iff $R/I$ is a field.

## Proof

Since $R$ is a commutative ring with unity,
$R/I$ is a commutative ring with unity $1+I$.

### Proof of 'only-if' part

Let $a+I \in R/I$ be a non-zero element.
Thus, $a \not\in I$.
Since $0 \in I$, $a \neq 0$.

Let $J = \{ra + i: r \in R \wedge i \in I\}$.

* $0 = 0a + 0 \in J$, so $J$ is non-empty.
* Let $r_1a + i_1, r_2a + i_2 \in J$. Then $(r_1a + i_1) - (r_2a + i_2) = (r_1 - r_2)a + (i_1 - i_2) \in J$.
* Let $r_1a + i_1, r_2a + i_2 \in J$. Then $(r_1a + i_1)(r_2a + i_2) = (r_1ar_2)a + (r_1ai_2 + i_1r_2a + i_1i_2) \in J$.
* Let $r' \in R \wedge ra + i \in J$. Then $r'(ra + i) = (r'r)a + r'i \in J$ and $(ra + i)r' = (rr')a + ir' \in J$.

Therefore, $J$ is an ideal of $R$.

Let $i \in I$. Then $i = 0a + i \in J$. Therefore, $I \subseteq J$.
$a = 1a + 0 \in J$, but $a \not\in I$. Therefore, $I \subset J$ and $I \neq J$.

Let $I$ be a maximal ideal. This means that $J = R$.

Since $1 \in R, 1 \in J$, which means $\exists b \exists i, 1 = ba + i$.
$\Rightarrow 1 + I = ba + I = (b + I)(a + I)$.
Therefore, every non-0 element $a+I$ in $R/I$ has an inverse.
Therefore, $R/I$ is a field.

### Proof of 'if' part

Let $R/I$ be a field. So $0 + I, 1 + I \in R/I$.
Therefore, $I \neq R$.

Since $I$ is not a maximal ideal, let $J$ be an ideal of $R$ which is a superset of $I$.
Let $a \in J-I$. Since $a \not\in I, a + I \neq 0 + I$.

Since $R/I$ is a field and $a+I$ is non-0, $a+I$ has an inverse.
Therefore, $\exists b, (a+I)(b+I) = ab + I = 1 + I$.
Therefore, $\exists i, ab + i = 1$.

$ba \in J$ because $a \in J$ and absorption.
$ba + i \in J$ because $I \subset J$ and closure of $J$.
Therefore, $1 \in J$.
By absorption, $\forall r \in R, r \in J$.
Therefore, $R = J$.
Therefore, $I$ is maximal.
