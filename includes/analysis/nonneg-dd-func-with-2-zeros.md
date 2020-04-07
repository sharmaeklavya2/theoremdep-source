Let $f: \mathbb{R} \mapsto \mathbb{R}$ be a function such that

* $f$ is differentiable in $[a, b]$.
* $\forall x \in [a, b], f''(x) \ge 0$.
* $f(a) = f(b) = 0$.

Then $\forall x \in [a, b], f(x) \le 0$.

## Proof idea

<span class="text-danger">(Rigorous proof needed)</span>

Assume that $\exists t \in (a, b)$ such that $f(t) > 0$.
Then by mean value theorem, $\exists x_1 \in (0, t)$ such that $f'(x_1) > 0$
and $\exists x_2 \in (t, 1)$ such that $f'(x_2) < 0$.
But this contradicts the fact that $f''(x) \ge 0$.
Therefore, such a $t$ doesn't exist.
