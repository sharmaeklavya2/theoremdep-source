Let $X = [X_0, X_1, \ldots]$ be a markov chain with transition function $P$ and state space $D$.

State $j$ is said to be *accessible* from state $i$ iff
$P^{(t)}(i, j) > 0$ for some $t \ge 0$.
We can prove that $j$ is accessible from $i$ iff
there exist states $k_0, k_2, \ldots, k_r$ such that
$P(k_t, k_{t+1}) > 0, \forall 0 \le t < r$ and $k_0 = i$ and $k_r = j$.
We can also prove that accessibility is a reflexive and transitive relation.

States $i$ and $j$ are said to *communicate* iff
$i$ is accessible from $j$ and $j$ is accessible from $i$.
We can prove that communication is an equivalence relation.
Hence, communication partitions the state space into equivalence classes, called *state classes*.
If there is just one state class (i.e., all states communicate),
then the markov chain is called *irreducible*.

State class $J$ is said to be accessible from state class $I$
iff $\exists j \in J$ and $\exists i \in I$ such that $j$ is accessible from $i$.
Then we can show that $\forall i \in I$ and $\forall j \in J$, $j$ is accessible from $i$.
Furthermore, we can prove that accessibility induces a partial ordering on the state classes.

## Intermediate transitions of accessibility

$j$ is accessible from $i$ iff $\exists m \ge 0$ such that $P^{(m)}(i, j) > 0$.
Let $k_0 = i$ and $k_m = j$.
\begin{align}
& P^{(m)}(i, j)
\\ &= \Pr(X_m = j \mid X_0 = i)
\\ &= \sum_{k_1 \in D} \sum_{k_2 \in D} \ldots \sum_{k_{m-1} \in D}
    \Pr\left(\bigwedge_{t=1}^m X_t = k_t \mid X_0 = k_0\right)
\\ &= \sum_{k_1 \in D} \sum_{k_2 \in D} \ldots \sum_{k_{m-1} \in D}
    \prod_{t=1}^m \Pr\left(X_t = k_t \mid \bigwedge_{s=0}^{t-1} X_s = k_s\right)
\\ &= \sum_{k_1 \in D} \sum_{k_2 \in D} \ldots \sum_{k_{m-1} \in D}
    \prod_{t=1}^m \Pr\left(X_t = k_t \mid X_{t-1} = k_{t-1}\right)
    \tag{by markov property}
\\ &= \sum_{k_1 \in D} \sum_{k_2 \in D} \ldots \sum_{k_{m-1} \in D}
    \prod_{t=1}^m P(k_{t-1}, k_t).
\end{align}
All these terms are non-negative.
Hence, $P^{(m)}(i, j) > 0 \iff \exists k_0, k_2, \ldots, k_m$ such that
$P(k_{t-1}, k_t) > 0, \forall 1 \le t \le m$ and $k_0 = i$ and $k_m = j$.

## Proof that accessibility of states is a reflexive and transitive relation

$i$ is accessible from $i$, since $P^{(0)}(i, i) = 1 > 0$.
Hence, accessibility is reflexive.

Suppose $j$ is accessible from $k$ and $k$ is accessible from $i$.
Then $\exists m \ge 0$ and $\exists n \ge 0$, such that
$P^{(m)}(i, k) > 0$ and $P^{(n)}(k, j) > 0$.
Then by the Chapman-Kolmogorov equation,
\[ P^{(m+n)}(i, j) = \sum_{r} P^{(m)}(i, r)P^{(n)}(r, j)
    \ge P^{(m)}(i, k)P^{(n)}(k, j) > 0. \]
Hence, $j$ is accessible from $i$.
Hence, accessibility is transitive.

## Proof that communication is an equivalence relation

$i$ communicates with $i$, since $P^{(0)}(i, i) = 1 > 0$.
Hence, communication is reflexive.

It is easy to see that communication is symmetric.

Suppose $i$ and $k$ communicate and $k$ and $j$ communicate.
By the transitivity of accessibility, we get that $i$ and $j$ communicate.
Hence, communication is transitive.

## Accessibility of state classes

Suppose state class $J$ is accessible from state class $I$.
Then $\exists i' \in I$ and $\exists j' \in J$ such that
$j'$ is accessible from $i'$.
Now let $i \in I$ and $j \in J$.
Since $i$ and $i'$ are in the same class $I$, $i'$ is accessible from $i$.
Since $j$ and $j'$ are in the same class $J$, $j$ is accessible from $j'$.
Hence, by transitivity of accessibility of states,
$i$ is accessible from $j$.

## Proof that accessibility induces a partial ordering on state classes

A state class $I$ is accessible from itself,
since for any $i \in I$, $i$ is accessible from itself.

Suppose state class $K$ is accessible from state class $I$ and
state class $J$ is accessible from state class $K$. This means that
$\exists k_1 \in K$ and $\exists i \in I$ such that $k_1$ is accessible from $i$,
and $\exists j \in J$ and $\exists k_2 \in K$ such that $j$ is accessible from $k_2$.
Then $k_2$ and $k_1$ are accessible from each other, since they belong to the same state class $K$.
Hence, by the transitivity of accessibility of states,
we get that accessibility of state classes is also transitive.

Suppose two distinct state classes $I$ and $J$ are accessible from each other.
Then $\exists i_1 \in I$ and $\exists j_1 \in J$ such that $i_1$ is accessible from $j_1$,
and $\exists i_2 \in I$ and $\exists j_2 \in J$ such that $j_2$ is accessible from $i_2$.
$i_1$ and $i_2$ are accessible from each other since they are from the same state class $I$.
$j_1$ and $j_2$ are accessible from each other since they are from the same state class $J$.
By transitivity of accessibility, this means that $j_1$ is accessible from $i_1$.
Hence, $j_1$ and $i_1$ communicate. But this is a contradiction,
since $i_1$ and $j_1$ are in different state classes.
Hence, no two state classes are accessible from each other.
Hence, accessibility of state classes is anti-symmetric.
Hence, accessibility of state classes is a partial ordering.
