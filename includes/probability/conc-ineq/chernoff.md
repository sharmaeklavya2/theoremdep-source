Let $X_1, X_2, \ldots, X_n$
$\newcommand{\E}{\operatorname{E}}$
be independent Bernoulli random variables, where $\Pr(X_i=1) = p_i$.

Let $X = \sum_{i=1}^n X_i$. Let $\mu = \E(X)$. Let $\delta > 0$.

\[ \Pr(X \ge (1+\delta)\mu)
\le \left(\frac{e^{\delta}}{(1+\delta)^{1+\delta}}\right)^{\mu}
\le \exp\left(-\frac{\mu\delta^2}{2+\delta}\right)
\le \begin{cases}\exp\left( - \frac{\mu\delta^2}{3} \right) & 0 < \delta \le 1
\\ \exp\left( - \frac{\mu\delta}{3} \right) & \delta \ge 1 \end{cases} \]

\[ \Pr(X \le (1-\delta)\mu)
\le \left(\frac{e^{-\delta}}{(1-\delta)^{1-\delta}}\right)^{\mu}
\le \exp\left(-\frac{\mu\delta^2}{2}\right)
\quad \textrm{where } \delta < 1 \]

\[ \Pr(\lvert X - \mu \rvert > \delta\mu)
\le 2\left(\frac{e^{\delta}}{(1+\delta)^{1+\delta}}\right)^{\mu}
\le 2\exp\left(-\frac{\mu\delta^2}{3}\right)
\quad \textrm{where } \delta < 1 \]

## Proof

By linearity of expectation, we get
\[ \mu = \E(X) = \sum_{i=1}^n \E(X_i) = \sum_{i=1}^n p_i \]
\begin{align}
\Pr(e^{tX} \ge e^{ta})
&\le \frac{\E(e^{tX})}{e^{ta}}  \tag{Markov bound}
\\ &= e^{-ta}\E\left(\prod_{i=1}^n e^{tX_i}\right)
\\ &= e^{-ta}\prod_{i=1}^n \E(e^{tX_i})  \tag{$X_i$ are independent}
\\ &= e^{-ta}\prod_{i=1}^n (1 + p_i(e^t-1))
\\ &\le e^{-ta}\prod_{i=1}^n e^{p_i(e^t-1)}  \tag{$1+x \le e^x$}
\\ &= \exp(\mu(e^t-1) - ta)
\end{align}

Let $t = \ln(1+\delta)$, $a = \mu(1+\delta)$.
Since $t > 0$, $\Pr(X \ge a) = \Pr(e^{tX} \ge e^{ta})$.
\[ \Pr(X \ge (1+\delta)\mu) \le \exp(\mu(\delta - (1+\delta)\ln(1+\delta)))
= \left(\frac{e^{\delta}}{(1+\delta)^{1+\delta}}\right)^{\mu} \]
Using the bound $\ln(1+\delta) \ge \frac{2\delta}{1+\delta}$, we get
\[ \Pr(X \ge (1+\delta)\mu) \le \exp\left(-\frac{\mu\delta^2}{2+\delta}\right) \]

We can further simplify this by considering the cases $\delta \le 1$ and $\delta \ge 1$ separately.
\begin{align}
& \delta \le 1 \implies 2 + \delta \le 3 \implies \frac{\delta^2}{2+\delta} \ge \frac{\delta^2}{3}
\\ &\implies \Pr(X \ge (1+\delta)\mu) \le \exp\left(-\frac{\mu\delta^2}{2+\delta}\right)
\le \exp\left( - \frac{\mu\delta^2}{3} \right)
\end{align}
\begin{align}
& \delta \ge 1 \implies 1 + \frac{2}{\delta} \le 3 \implies \frac{\delta}{\delta+2} \ge \frac{1}{3}
\\ &\implies \Pr(X \ge (1+\delta)\mu) \le \exp\left(-\frac{\mu\delta^2}{2+\delta}\right)
\le \exp\left( - \frac{\mu\delta}{3} \right)
\end{align}

Now let $0 < \delta < 1$, $t = \ln(1-\delta)$, $a = \mu(1-\delta)$.
Since $t < 0$, $\Pr(X \le a) = \Pr(e^{tX} \ge e^{ta})$.
\[ \Pr(X \le (1-\delta)\mu) \le \exp(\mu(-\delta - (1-\delta)\ln(1-\delta)))
= \left(\frac{e^{-\delta}}{(1-\delta)^{1-\delta}}\right)^{\mu} \]

Let $f(x) = x + (1-x)\ln(1-x) - \frac{x^2}{2}$.
Then $f'(x) = - x - \ln(1-x)$ and $f''(x) = \frac{x}{1-x}$.
For $0 < x < 1$, $f''(x) > 0$.
Since $f'(0) = 0$, $f'(x) \ge 0$.
Since $f(0) = 0$, $f(x) \ge 0$.

\[ \Pr(X \le (1-\delta)\mu)
\le \exp(\mu(-\delta - (1-\delta)\ln(1-\delta)))
\le \exp\left(-\frac{\mu\delta^2}{2}\right) \]

Let $g(x) = (x - (1+x)\ln(1+x)) - (-x-(1-x)\ln(1-x)) = 2x - (1+x)\ln(1+x) + (1-x)\ln(1-x)$.

Then $g'(x) = -\ln(1-x^2)$. Since $g(0) = 0$ and $g'(x) \ge 0$, $g(x) \ge 0$.
This gives us
\[ \left(\frac{e^{\delta}}{(1+\delta)^{1+\delta}}\right)^{\mu}
\ge \left(\frac{e^{-\delta}}{(1-\delta)^{1-\delta}}\right)^{\mu} \]

\begin{align}
& \Pr(\lvert X - \mu \rvert > \delta\mu)
\\ &= \Pr(X \ge (1+\delta)\mu) + \Pr(X \le (1-\delta)\mu)
\\ &\le \left(\frac{e^{\delta}}{(1+\delta)^{1+\delta}}\right)^{\mu}
+ \left(\frac{e^{-\delta}}{(1-\delta)^{1-\delta}}\right)^{\mu}
\\ &\le 2\left(\frac{e^{\delta}}{(1+\delta)^{1+\delta}}\right)^{\mu}
\\ &\le 2\exp\left(-\frac{\mu\delta^2}{3}\right)
\end{align}
