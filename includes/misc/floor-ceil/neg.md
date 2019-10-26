Let $x \in \mathbb{R}$.
Then $\lfloor -x \rfloor = -\lceil x \rceil$.

## Proof

By the definition of floor and ceil, we get that
$\lfloor x \rfloor = n \iff x \in [n, n+1)$
and $\lceil x \rceil = n \iff x \in (n-1, n]$.
\[ \lfloor -x \rfloor = n \iff -x \in [n, n+1) \iff x \in (-n-1, -n] \iff \lceil x \rceil = -n \]
