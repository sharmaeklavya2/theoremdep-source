<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
</span>
Let $X$ be a real-valued random variable (over probability space $(\Omega, \mathcal{F}, \Pr)$).
Let $f(z) = \E(|X - z|)$. Then

1.  If $m$ is a median of $X$ and $c$ is not a median of $X$, then $f(c) > f(m)$.
2.  If $m_1$ and $m_2$ are medians of $X$, then $f(m_1) = f(m_2)$.

## Proof

Let $a < b$. Then
\begin{align}
& f(b) - f(a) = \E(|X-b|) - \E(|X-a|)
\\ &= \E(|X-b|-|X-a|)  \tag{linearity of expectation}
\\ &= \int_{\omega \subseteq \Omega} (|X(\omega)-b|-|X(\omega)-a|)\Pr(\omega)
\\ &= \int_{\omega \subseteq \Omega \wedge X(\omega) \le a} (|X(\omega)-b|-|X(\omega)-a|)\Pr(\omega)
    \\ &\qquad+ \int_{\omega \subseteq \Omega \wedge a < X(\omega) < b}
        (|X(\omega)-b|-|X(\omega)-a|)\Pr(\omega)
    \\ &\qquad+ \int_{\omega \subseteq \Omega \wedge X(\omega) \ge b}
        (|X(\omega)-b|-|X(\omega)-a|)\Pr(\omega)
\\ &= \int_{\omega \subseteq \Omega \wedge X(\omega) \le a} (b-a)\Pr(\omega)
    \\ &\qquad+ \int_{\omega \subseteq \Omega \wedge a < X(\omega) < b}
        (a+b-2X(\omega))\Pr(\omega)
    \\ &\qquad+ \int_{\omega \subseteq \Omega \wedge X(\omega) \ge b}
        (a-b)\Pr(\omega)
\\ &= (b-a)(\Pr(X \le a) - \Pr(X \ge b))
    + \int_{\omega \subseteq \Omega \wedge a < X(\omega) < b} (a+b-2X(\omega))\Pr(\omega).
\end{align}

### Proof of part 2

Let $m_1$ and $m_2$ be medians of $X$.
Without loss of generality, assume $m_1 < m_2$.
Then $\Pr(m_1 < X < m_2) = 0$, $\Pr(X \le m_1) = 1/2$ and $\Pr(X \ge m_2)$.
Hence,
\[ f(m_2) - f(m_1) = (m_2 - m_1)(\Pr(X \le m_1) - \Pr(X \ge m_2)) = 0. \]

### Proof of part 1 when $c > m$

Since $m$ is a median, we get $\Pr(X \le c) \ge \Pr(X \le m) \ge 1/2$.
Since $c$ is not a median, we get $\Pr(X \ge c) < 1/2$.

**Case 1**: $\Pr(m < X < c) = 0$.

\[ f(c) - f(m) = (c-m)(\Pr(X \le m) - \Pr(X \ge c)) > (c-m)(1/2 - 1/2) = 0 \]

**Case 2**: $\Pr(m < X < c) > 0$.

\[ m < X < c \implies -(c-m) < m+c-2X < c-m \]
Hence,
\begin{align}
& f(c) - f(m)
\\ &= (c-m)(\Pr(X \le m) - \Pr(X \ge c))
    + \int_{\omega \subseteq \Omega \wedge m < X(\omega) < c} (m+c-2X(\omega))\Pr(\omega).
\\ &> (c-m)(\Pr(X \le m) - \Pr(X \ge c)) - (c-m)\Pr(m < X < c)
\\ &= (c-m)(\Pr(X \le m) - \Pr(X > m))
\\ &= (c-m)(2\Pr(X \le m) - 1)
\ge 0  \tag{$m$ is a median}
\end{align}

### Proof of part 1 when $c < m$

(Analogous to the case where $c > m$.)
