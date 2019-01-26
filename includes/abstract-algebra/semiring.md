Let $R$ be a set and $+$ and $\circ$ be binary operations.
Then $(R, +, \circ)$ is a semiring iff the following statements are true
for all $r_1, r_2, r_3 \in R$:

* Additive closure: $r_1 + r_2 \in R$.
* Additive commutativity: $r_1 + r_2 = r_2 + r_1$.
* Additive associativity: $(r_1 + r_2) + r_3 = r_1 + (r_2 + r_3)$.
* Existence of 0: $\exists 0 \in R, \forall r \in R, 0 + r = r + 0 = r$.
* Multiplicative closure: $r_1 \circ r_2 \in R$.
* Mutiplicative associativity: $(r_1 \circ r_2) \circ r_3 = r_1 \circ (r_2 \circ r_3)$.
* Left Distributivity: $r_1 \circ (r_2 + r_3) = (r_1 \circ r_2) + (r_1 \circ r_3)$.
* Right Distributivity: $(r_1 + r_2) \circ r_3 = (r_1 \circ r_3) + (r_2 \circ r_3)$.

Additionally, if $\exists 1 \in R, \forall r \in R, r \circ 1 = 1 \circ r = r$,
then $1$ is called a unity of $R$ and $R$ is a semiring with unity.

If $r_1 \circ r_2 = r_2 \circ r_1$, then $R$ is called a commutative semiring.
