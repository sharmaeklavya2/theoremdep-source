Let $x$ and $y$ be vectors from the inner product space $V$ and $x \neq 0$.
Then $y = kx$ for some scalar $k$ iff $|\langle x, y \rangle|^2 = \|x\|^2\|y\|^2$.

## Proof of 'only-if' part

Let $y = kx$ for some scalar $k$.

\begin{align}
& |\langle x, y \rangle|^2
\\ &= \langle x, kx \rangle \overline{\langle x, kx \rangle}
\\ &= \langle x, kx \rangle \langle kx, x \rangle \tag{by conjugate symmetry}
\\ &= \overline{k}\langle x, x \rangle k\langle x, x \rangle \tag{by (anti-)linearity}
\\ &= \langle x, x \rangle k\overline{k}\langle x, x \rangle \tag{multiplicative commutativity in field}
\\ &= \langle x, x \rangle \langle kx, kx \rangle \tag{by (anti-)linearity}
\\ &= \|x\|^2 \|y\|^2
\end{align}

## Proof of 'if' part

By the positive-definiteness property of inner-product spaces, $x \neq 0 \Rightarrow \|x\|^2 \neq 0$.

Let $|\langle x, y \rangle|^2 = \|x\|^2\|y\|^2$.

\[ w = y - \frac{\langle y, x \rangle}{\|x\|^2}x \]

(Intutively, $w$ is the component of $y$ perpendicular to $x$. We have to prove that this is 0.)

\begin{align}
& \langle w, x \rangle
\\ &= \left\langle y - \frac{\langle y, x \rangle}{\|x\|^2}x, x \right\rangle
\\ &= \langle y, x \rangle - \frac{\langle y, x \rangle}{\|x\|^2} \langle x, x \rangle \tag{by linearity in first argument}
\\ &= \langle y, x \rangle - \langle y, x \rangle = 0
\end{align}

\begin{align}
& \langle w, y \rangle
\\ &= \left\langle y - \frac{\langle y, x \rangle}{\|x\|^2}x , y \right\rangle
\\ &= \langle y, y \rangle - \frac{\langle y, x \rangle}{\|x\|^2} \langle x , y \rangle \tag{by linearity in first argument}
\\ &= \frac{\|x\|^2\|y\|^2 - \langle y, x \rangle\langle x , y \rangle}{\|x\|^2}
\\ &= \frac{\|x\|^2\|y\|^2 - \overline{\langle x, y \rangle}\langle x , y \rangle}{\|x\|^2} \tag{conjugate symmetry}
\\ &= \frac{\|x\|^2\|y\|^2 - |\langle x, y \rangle|^2}{\|x\|^2} = 0
\end{align}

\begin{align}
& \|w\|^2 = \langle w, w \rangle
\\ &= \left\langle w, y - \frac{\langle y, x \rangle}{\|x\|^2}x \right\rangle
\\ &= \langle w, y \rangle - \frac{\overline{\langle y, x \rangle}}{\|x\|^2} \langle w, x \rangle \tag{by anti-linearity}
\\ &= 0 - \frac{\overline{\langle y, x \rangle}}{\|x\|^2} 0 = 0
\end{align}

By the positive-definiteness property of inner-product spaces, $\|w\|^2 = 0 \Rightarrow w = 0$

Therefore, $y = \frac{\langle y, x \rangle}{\|x\|^2}x \Rightarrow y = kx$ for some scalar $k$.
