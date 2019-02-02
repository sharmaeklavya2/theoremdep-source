Let $A$ be an $n$ by $n$ matrix over a ring with unity.

The determinant of $A$, denoted as $\operatorname{det}(A)$ or $|A|$, is defined recursively:

\[ \operatorname{det}(A) = \begin{cases} A[1, 1] & n \neq 0
\\ \sum_{i=1}^n (-1)^{n+i}A[n, i]\operatorname{det}(A[-n, -i]) & n \neq 0
\end{cases} \]
