Read sections 1.1, 1.2, 1.3 and 1.4 from
<a class="cite-ref" href="#cite-prob-and-rand-proc">[prob-and-rand-proc]</a>
for an intuitive understanding and to know the definitions
of 'event', 'sample space', 'probability' and 'probability measure'.
You may optionally read chapter 0 too.

A probability space is a triple $(\Omega, \mathcal{F}, P)$, where:

* $\Omega$ is the sample space, also called the set of all outcomes.
* $\mathcal{F}$ is a $\sigma$-algebra over $\Omega$.
$\mathcal{F}$ is called the set of all events.
* $P: \mathcal{F} \mapsto [0, 1]$ is a measure over $(\Omega, \mathcal{F})$ such that $P(\Omega) = 1$.
$P$ is called a probability measure.

One can usually let $\mathcal{F}$ be equal to the power-set of $\Omega$.
But for certain infinite-sized $\Omega$, certain probability measures cannot be defined
over the power-set of $\Omega$
(see the [Banach-Tarski paradox](https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox)
or [Vitali set](https://en.wikipedia.org/wiki/Vitali_set)).

## Additional properties

These simple properties can be proven using the definition of probability space above:

* Let $S = \{A_1, A_2, \ldots\}$ be a countable set of events.
Then $\bigcap_{A \in S} A \in \mathcal{F}$.
* Let $A$ be an event. Define $\overline{A} = \Omega - A$. Then
$P(\overline{A}) = 1 - P(A)$ (since $A$ and $\overline{A}$ are disjoint and $A \cup \overline{A} = \Omega$).
* $A \subseteq B \implies P(A) \le P(B)$.
* $A \subseteq B \implies P(B-A) = P(B) - P(A)$ (because $A$ and $B-A$ are disjoint).
* $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

## References
