Let $M = (S, I)$ be a matroid.
Let $X \subset S$ and $e \not\in X$.
Let $w$ be a weight function over $M$.
Let $B$ be a max-weight basis of $X$.

If $B + e \in I$, then $B + e$ is a max-weight basis of $X + e$.

If $B + e \not\in I$, $B + e$ contains a circuit $C$.
Let $\widehat{e}$ be the min-weight element of $C$.
Then $g(X+e) = B + e - \widehat{e}$.

## Proof

$|B + e| = |B| + 1 = r(X) + 1$.

### Case 1: $B + e \in I$

If $B + e \in I$, then $B + e$ is a basis of $X + e$, so $r(X+e) = r(X) + 1$.
Therefore, $B + e$ is a max-weight basis of $X + e$.

### Case 2: $B + e \not\in I$

$B + e \not\in I \implies r(X+e) = r(X)$.

$C$ contains $e$, otherwise $B$ would be dependent.

Order the elements of $X+e$ in descending order of weight.
If there are some elements with the same weight, order them arbitrarily.
Since $\widehat{e}$ is the min-weight element of $C$,
$w(e) \ge w(\widehat{e})$.
Let $W$ be the elements of $X$ before $e$ in this order.

The greedy algorithm for computing max-weight basis can be visualized as a streaming algorithm
to which we can feed elements one-by-one and it keeps track of the selected elements so far.
Create 2 instances of this algorithm, $A_1$ and $A_2$.
We intend to feed $X$ to $A_1$ and $X+e$ to $A_2$.

Feed $W$ to both instances. Both of them will select the same set of elements, $P$.
Since $W \subseteq X$, $P \subseteq B$.

Now feed $e$ to $A_2$.
Suppose $A_2$ doesn't select $e$. It means that $P+e$ contains a circuit $C'$.
Since $C' \subseteq P+e \subseteq B+e$ and $B+e$ contains a unique circuit $C$, $C' = C$.
Therefore, all other elements of $C$ are in $P$, so $\widehat{e} = e$.

Since $A_2$ didn't select $e$, it will select the same elements as $A_1$
when we feed the remaining elements $X - W$ to both of them.
Therefore, both of them select $B$.
Since the greedy algorithm selects the max-weight basis,
$B$ is a max-weight basis for $X + e$.
Since $\widehat{e} = e$, $B + e - \widehat{e}$ is a max-weight basis of $X + e$.

Now suppose $A_2$ selects $e$.
Now feed elements of $X - W$ (in decreasing order) one-by-one to both $A_1$ and $A_2$
and pause when they select different elements.
They will eventually select different elements, because if they don't,
then $A_2$ would select $B+e$, which is not a basis.

If $A_2$ selects an element $x$, then $A_1$ will also select $x$ in the corresponding step.
This is because if $A_1$'s selection at some step is $L$,
then $A_2$'s selection at that step is $L + e$,
and if $L+e+x$ is independent then $L+x$ is also independent.

Let $x$ be the first element which $A_1$ selects but $A_2$ doesn't.
Let $A_1$'s selection before this be $Q$. So $Q \subset B$.
$Q + e$ is independent but $Q + e + x$ is not.
Since, $Q + e + x \subseteq B + e$, $Q + e + x$ contains the circuit $C$ and $x \in C$.
Therefore, all elements of $C$ other than $x$ are in $Q + e$.
Therefore, $x = \widehat{e}$.

Till now $A_1$ has selected $B_1 = P + Q + \widehat{e}$ and $A_2$ has selected $B_2 = P + e + Q$.
Now feed the remaining elements of $X$ to both $A_1$ and $A_2$.
Out of these newly fed elements, suppose $A_1$ selects $R_1$ and $A_2$ selects $R_2$.
Since the greedy algorithm always returns a basis, $|R_1| = |R_2|$.

$B_2 + \widehat{e} = B_1 + e = P + Q + e + \widehat{e} \supset C \not\in I$.
So when we use the exchange axiom to transfer elements from $B_1 + R_1$ to $B_2$,
we get $B_2 + R_1$ as the basis.
When we use the exchange axiom to transfer elements from $B_2 + R_2$ to $B_1$,
we get $B_1 + R_2$ as the basis.
Since the greedy algorithm selected $B_1 + R_1$ instead of $B_1 + R_2$, $w(R_1) \ge w(R_2)$.
Since the greedy algorithm selected $B_2 + R_2$ instead of $B_2 + R_1$, $w(R_2) \ge w(R_1)$.
Therefore, $w(R_1) = w(R_2)$. So $B_2 + R_1 = B + e - \widehat{e}$ is also a max-weight basis.
