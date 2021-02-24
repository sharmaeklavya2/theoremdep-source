## Standard definition

Events $A$ and $B$ are said to be independent for the probability measure $\Pr$
iff $\Pr(A \cap B) = \Pr(A)\Pr(B)$.

It is easy to see that independence is a symmetric relation.

If for event $C$, $\Pr_{|C}$ is defined and $A$ and $B$ are independent for $\Pr_{|C}$,
then $A$ and $B$ are said to be independent conditioned on $C$.

Let $S = \{A_1, A_2, \ldots\}$ be a countable set of events.
Then events in $S$ are said to be independent iff
\[ \Pr\left(\bigcap_{A \in S} A\right) = \prod_{A \in S} \Pr(A) \]
The events in $S$ are said to be pairwise independent iff
any 2 distinct events in $S$ are independent.

## Alternative definition

I'm unsatisfied with the standard definition.
See [this math.se post](https://math.stackexchange.com/q/3692185/573551) for the reason.
Therefore, I'm proposing an alternative definition here.

Events $A$ and $B$ are said to be independent (in the alternative sense)
for the probability measure $\Pr$ iff at least one of these holds:

* $\Pr_{|B}$ is not defined.
* $\Pr_{|B}$ is defined, and $\Pr(A \mid B) = \Pr(A)$.

Below are 2 theorems that slightly legitimize my definition
by comparing it with the standard definition.

**Theorem 1**: If $A$ and $B$ are alternatively independent,
then $A$ and $B$ are independent.

**Proof**:
If $\Pr_{|B}$ is not defined, then $\Pr(B) = 0$.
Since $\Pr(A \cap B) \le \Pr(B)$, $\Pr(A \cap B) = 0 = \Pr(A)\Pr(B)$.

If $\Pr_{|B}$ is defined, then the definition of $\Pr_{|B}$ dictates that
$\Pr(A \cap B) = \Pr_{|B}(A)\Pr(B)$.
Since $A$ and $B$ are independent, $\Pr_{|B}(A) = \Pr(A)$.
\[ \tag*{$\square$} \]

**Theorem 2**: If $\Omega$ is countable or $\Pr(B) > 0$, then
$A$ and $B$ are alternatively independent iff they are independent.

**Proof**:
Suppose $\Pr(B) > 0$.
\begin{align}
& A \textrm{ and } B \textrm{ are alternatively independent}
\\ &\iff \Pr(A \mid B) = \Pr(A)
\\ &\iff \Pr(A \cap B) = \Pr(A)\Pr(B)
\\ &A \textrm{ and } B \textrm{ are independent}
\end{align}
When $\Omega$ is countable and $\Pr(B) = 0$, then $\Pr_{|B}$ is not defined,
so $A$ and $B$ are alternatively independent.

**Corollary**:
When $\Omega$ is countable or both $\Pr(A)$ and $\Pr(B)$ are positive,
then alternative independence is a symmetric relation.

The main drawback of my definition is that I'm unable to prove that it's symmetric.
