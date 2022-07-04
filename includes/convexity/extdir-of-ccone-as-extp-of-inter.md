<span class="invisible">
$\newcommand{\inprod}[2]{\langle #1, #2 \rangle}$
$\newcommand{\dhat}{\widehat{d}}$
</span>
Let $C$ be a convex cone (in an inner product space over $\mathbb{R}$).
Let $c$ be a vector such that $\inprod{c}{x} > 0$ for all $x \in C - \{0\}$.
Let $\gamma \in \mathbb{R}_{> 0}$ and $S = \{x \in C: \inprod{c}{x} = \gamma\}$.

If $d$ is an extreme direction of $C$, then $(\gamma/\inprod{c}{d})d$ is an extreme point of $S$.
If $d$ is an extreme point of $S$, then $d$ is an extreme direction of $C$.

## Proof

We can assume without loss of generality that $\gamma$ is 1, since we can scale $c$.

Two vectors $u$ and $v$ are called collinear iff $u/\inprod{c}{u} = v/\inprod{c}{v}$.

Let $d \in C - \{0\}$. Let $\dhat = d/\inprod{c}{d}$. Then $\inprod{c}{\dhat} = 1$, so $\dhat \in S$.
Suppose $\dhat$ is a non-extreme point of $S$.
Then $\dhat = (1-\alpha) d^{(1)} + \alpha d^{(2)}$ for some $d^{(1)}, d^{(2)} \in S$
where $d^{(1)} \neq d^{(2)}$ and $\alpha \in (0, 1)$.
Note that $d^{(1)}$ and $d^{(2)}$ are not collinear.
Then $d = \inprod{c}{d}(1-\alpha) d^{(1)} + \inprod{c}{d}\alpha d^{(2)}$,
so $d$ is not an extreme direction of $C$.
Hence, if $d$ is an extreme direction of $C$, then $\dhat$ is an extreme point of $S$.

Let $d$ be an extreme point of $S$. Then $d \neq 0$.
Suppose $d$ is not an extreme direction of $C$.
Then $d = \alpha d^{(1)} + \beta d^{(2)}$, such that $\alpha > 0$, $\beta > 0$,
and $d^{(1)}, d^{(2)} \in C - \{0\}$ such that $d^{(1)}/\inprod{c}{d^{(1)}} \neq d^{(2)}/\inprod{c}{d^{(2)}}$.
Let $\dhat^{(1)} = d^{(1)}/\inprod{c}{d^{(1)}}$ and $\dhat^{(2)} = d^{(2)}/\inprod{c}{d^{(2)}}$.
Then $\dhat^{(1)} \neq \dhat^{(2)}$ and $\dhat^{(1)}, \dhat^{(2)} \in S$.
Hence, we get $d = (\alpha \inprod{c}{d^{(1)}})\dhat^{(1)} + (\beta \inprod{c}{d^{(2)}}) \dhat^{(2)}$.
Since, $1 = \inprod{c}{d} = \alpha \inprod{c}{d^{(1)}} + \beta \inprod{c}{d^{(2)}}$,
we get that $d$ is a strict convex combination of $\dhat^{(1)}$ and $\dhat^{(2)}$.
Hence, $d$ is not an extreme point of $S$, which is a contradiction.
Hence, $d$ is an extreme direction of $C$.
