Let $A$ and $B$ be events. Then the probability of $A$ conditioned on $B$,
denoted as $\Pr(A|B)$ is defined as
\[ \Pr(A|B) = \frac{\Pr(A \cap B)}{\Pr(B)} \]

Often, $\Pr(A|B_1 \cap B_2 \cap \ldots \cap B_m)$ is denoted as $\Pr(A|B_1, B_2, \ldots, B_m)$.

Note that $\Pr(A) = \Pr(A | \Omega)$, where $\Omega$ is the sample space.

It is easy to see that
\[ \Pr(A|B \cap C) = \frac{\Pr(A \cap B | C)}{\Pr(B | C)} \]

Events $A$ and $B$ are said to be independent
when conditioned on $C$ iff $\Pr(A|B \cap C) = \Pr(A | C)$.
When $C = \Omega$, we simply say that $A$ and $B$ are independent.

An equivalent definition of independence is:
$A$ and $B$ are independent when conditioned on $C$ iff $\Pr(A \cap B | C) = \Pr(A|C)\Pr(B|C)$.
This means that independence is a symmetric relation.
Therefore, $A$ and $B$ are independent when conditioned on $C$
iff $\Pr(B|A \cap C) = \Pr(B|C)$.

Let $S = \{A_1, A_2, \ldots\}$ be a countable set of events.
Then events in $S$ are said to be independent iff
\[ \Pr\left(\bigcap_{A \in S} A\right) = \prod_{A \in S} \Pr(A) \]
The events in $S$ are said to be pairwise independent iff
any 2 distinct events in $S$ are independent.
