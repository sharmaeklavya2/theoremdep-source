Let $M = (S, I)$ be a matroid.
Then $X$ is a dependent set in $M$ iff $X$ contains a circuit $C$.

## Proof

Suppose $X$ contains a circuit $C$.
Since $C \not\in I$, by contrapositive of hereditary property, $X \not\in I$.

Suppose $X$ is dependent but doesn't contain a circuit.
Therefore, $X$ is not a circuit.
Therefore, if $|X| > 0$, we can remove an element from $X$ to get a smaller dependent set $Y$.
$Y$ doesn't have a circuit too because if $Y$ contained a circuit
then $X$ would also contain it since $Y \subseteq X$.

Therefore, we can keep repeating this process and after each step we will get a dependent set.
But the process will stop when we reach the empty set
and the empty set is independent.
This is a contradiction. Therefore, if $X$ is dependent, it contains a circuit.
