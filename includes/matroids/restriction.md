Let $M = (S, I)$ be a matroid.
Let $T \subseteq S$ and $M' = (T, I')$,
where $I' = \{ X \cap T: X \subseteq I \}$.

Then $M'$ is called the restriction of $M$ to $T$.
It can be proved that $M'$ is also a matroid.

## Proof

Let $X \in I$. By the hereditary property, $X \cap T \in I$.
Therefore, $I' \subseteq I$.

Let $X \subseteq Y \subseteq T$. Then
\begin{align}
& Y \in I'
\\ &\implies Y \in I  \tag{$I' \subseteq I$}
\\ &\implies X \in I  \tag{hereditary property of $M$}
\\ &\implies X \cap T \in I'  \tag{definition of $I'$}
\\ &\implies X \in I'  \tag{$X \subseteq T \Rightarrow X \cap T = X$}
\end{align}
Therefore, hereditary property holds for $M'$.

Let $X, Y \in I'$ and $|X| < |Y|$.
Since $I' \subseteq I$, by the exchange property of $M$,
$\exists e \in Y-X$ such that $X + e \in I$.
Therefore, $(X + e) \cap T \in I' \implies X + e \in I'$.

Therefore, the exchange property also holds for $M'$.
