<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Consider a fair division instance with 6 goods and 3 agents having equal entitlements and additive valuations.
Valuations are given by this table:

<table>
<tr><th>$j$</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr>
<tr><td>$v$<sub>1</sub>( $j$ )</td>
    <td>20</td><td>20</td><td>20</td><td>10</td><td>10</td><td>10</td></tr>
<tr><td>$v$<sub>2</sub>( $j$ ), $v$<sub>3</sub>( $j$ )</td>
    <td>20</td><td>10</td><td>10</td><td>1</td><td>1</td><td>1</td></tr>
</table>

Then the allocation $A \defeq (\{4, 5, 6\}, \{1\}, \{2, 3\})$ is MEFS, but no allocation is epistemic EF.

## Proof

Agents 2 and 3 are envy-free in $A$.
Agent 1 has $B \defeq (\{1, 4\}, \{2, 5\}, \{3, 6\})$ as her MEFS-certificate for $A$.
Hence, $A$ is MEFS.

Suppose an epistemic EF allocation $X$ exists.
Let $Y^{(i)}$ be each agent $i$'s epistemic-EF-certificate.
For agent 2 to be envy-free in $Y^{(2)}$,
we require $Y^{(2)}_2 \supseteq \{1\}$ or $Y^{(2)}_2 \supseteq \{2, 3\}$.
Similarly, $Y^{(3)}_3 \supseteq \{1\}$ or $Y^{(3)}_3 \supseteq \{2, 3\}$.
Since $Y^{(i)}_i = X_i$ for all $i$, we get $X_2 \cup X_3 \supseteq \{1, 2, 3\}$.
Hence, $X_1 \subseteq \{4, 5, 6\}$.
But then no epistemic-EF-certificate exists for agent 1 for $X$,
contradicting our assumption that $X$ is epistemic EF.
Hence, no epistemic EF allocation exists.
