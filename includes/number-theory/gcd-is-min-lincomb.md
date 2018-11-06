The GCD of two numbers is their smallest positive linear combination.

## Proof

Let $p_{a, b}(x, y): \gcd(x, y) = \gcd(a, b) \wedge x, y \in a\mathbb{Z} + b\mathbb{Z}$.

$$(\gcd(x, y) = \gcd(x-y, y) = \gcd(a, b)) \wedge (x, y \in a\mathbb{Z} + b\mathbb{Z} \iff x-y, y \in a\mathbb{Z} + b\mathbb{Z})$$

Therefore,

$$(p_{a, b}(x, y) \iff p_{a, b}(x, y)) \Rightarrow (p_{a, b}(x, y) \iff p_{a, b}(y, x\%y))$$

Let $\lambda$ be the operation defined by $(x, y) \mapsto (y, x\%y)$ where $y$ is not 0.
$p_{a, b}$ is invariant over $\lambda$.

Applying $\lambda$ on $(x, y)$ decreases $y$.
Therefore, successively applying $\lambda$ on $(a, b)$ will eventually reduce it to the form $(e, 0)$.

$p_{a, b}(a, b)$ is trivially true.
$p_{a, b}(e, 0)$ is true since $p_{a, b}$ is invariant over $\lambda$.

$$p_{a, b}(e, 0)
\Rightarrow e = \gcd(a, b) \wedge e \in a\mathbb{Z} + b\mathbb{Z}
\Rightarrow \gcd(a, b) \in a\mathbb{Z} + b\mathbb{Z}$$

Let $d$ be the smallest positive linear combination of $a$ and $b$.

$$g \mid a \wedge g \mid b \Rightarrow g \mid d \Rightarrow g \le d \Rightarrow g = d$$

Therefore, $\gcd(a, b)$ is the smallest positive linear combination of $a$ and $b$.
