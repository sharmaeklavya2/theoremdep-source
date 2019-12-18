\[ \binom{n}{i} = \frac{\binom{n}{k}}{\binom{i}{k}} \binom{n-k}{i-k} \]

## Proof

Repeatedly apply the decrement identity to get

\[ \binom{n}{i} = \frac{n(n-1)\ldots(n-k+1)}{i(i-1)\ldots(i-k+1)} \binom{n-k}{i-k} \]

\begin{align}
n(n-1)\ldots(n-k+1) &= k!\binom{n}{k}
& i(i-1)\ldots(i-k+1) &= k!\binom{i}{k}
\end{align}
