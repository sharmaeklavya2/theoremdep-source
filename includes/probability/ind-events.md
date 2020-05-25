Events $A$ and $B$ are said to be independent for the probability measure $\Pr$
iff at least one of these holds:

* $\Pr_{|A}$ is not defined.
* $\Pr_{|B}$ is not defined.
* $\Pr_{|B}$ is defined, and $\Pr(A \mid B) = \Pr(A)$.

If for event $C$, $\Pr_{|C}$ is defined and
$A$ and $B$ are independent for $\Pr_{|C}$, then
then $A$ and $B$ are said to be independent conditioned on $C$.

**Theorem 1**: Independence is a symmetric relation.

**Proof**:
This is easy to prove when $\Omega$ is countable, because
when $\Pr_{|A}$ and $\Pr_{|B}$ are defined,
\[ \Pr(A \mid B) = \Pr(A)
\iff \Pr(A \cap B) = \Pr(A)\Pr(B)
\iff \Pr(B \mid A) = \Pr(B) \]
<span class="text-danger">(Proof pending for uncountable $\Omega$)</span>
\[ \tag*{$\square$} \]

**Theorem 2**:
When it is given that $\Pr(A) > 0$ and $\Pr(B) > 0$,
$A$ and $B$ are independent iff $\Pr(A \cap B) = \Pr(A)\Pr(B)$.

**Proof**:
$A$ and $B$ are independent iff
$\Pr(A \mid B) = \Pr(A)$ iff
$\Pr(A \cap B) = \Pr(A)\Pr(B)$.
\[ \tag*{$\square$} \]

**Theorem 3**:
If events $A$ and $B$ are independent, then
$\Pr(A \cap B) = \Pr(A)\Pr(B)$ (the converse need not be true).

**Proof**:
If $\Pr_{|A}$ or $\Pr_{|B}$ is not defined, then $\Pr(A) = 0$ or $\Pr(B) = 0$.
\[ 0 \le \Pr(A \cap B) \le \min(\Pr(A), \Pr(B)) = 0 \]
Therefore, $\Pr(A \cap B) = \Pr(A)\Pr(B) = 0$.

If $\Pr_{|A}$ and $\Pr_{|B}$ are defined, then
the definition of $\Pr_{|B}$ dictates that
$\Pr(A \cap B) = \Pr_{|B}(A)\Pr(B)$.
Since $A$ and $B$ are independent, $\Pr_{|B}(A) = \Pr(A)$.
\[ \tag*{$\square$} \]

Let $S = \{A_1, A_2, \ldots\}$ be a countable set of events
such that $\forall A \in S, \Pr(A) > 0$.
Then events in $S$ are said to be independent iff
\[ \Pr\left(\bigcap_{A \in S} A\right) = \prod_{A \in S} \Pr(A) \]
The events in $S$ are said to be pairwise independent iff
any 2 distinct events in $S$ are independent.
