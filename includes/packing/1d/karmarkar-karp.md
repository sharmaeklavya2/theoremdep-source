<span class="invisible">
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\floor}[1]{\left\lfloor{#1}\right\rfloor}$
$\newcommand{\lin}{\operatorname{lin}}$
$\newcommand{\LP}{\operatorname{LP}}$
$\newcommand{\Opt}{\operatorname{opt}}$
$\newcommand{\Sum}{\operatorname{sum}}$
</span>
The Karmarkar-Karp algorithm is a polynomial-time algorithm for 1D bin packing.

Its output's cost is at most $\lin(I) + O(\log^2(\Size(I)))$.
This makes it achieve an additive approximation of $O(\log^2(\Opt(I)))$.

## Algorithm

Let $I$ be a bin packing instance with $m$ distinct items.
Let there be $b_i$ items of type $I$.
Call $b$ the item frequency vector of $I$.
Let $L$ be the config LP, let $T$ be the configuration matrix
and let $N$ be the number of configurations.
Let $\delta = 1 / \Size(I)$.

Algorithm $\operatorname{large-bin-pack}(I)$:

* if $\Size(I) < 10$:
    * Pack $I$ using Next-Fit algorithm.
* else:
    * $(I', J) = \operatorname{harmonic-grouping}(I)$
    * Pack $J$ using Next-Fit algorithm (packing discards).
    * $x = \operatorname{approx-solve-config-lp}(I', \delta)$.
    In the configuration LP, items have the same type iff they have the same size.
    * For each config $C$, pack $\floor{x_C}$ bins of $C$ (integral packing).
      Call the packed items $I_1$ and the remaining items $I_2$.
    * $\operatorname{large-bin-pack}(I_2)$.

Algorithm $\operatorname{bin-pack}(I)$:

* $I_S = \{s \in I: s < \delta\}$ and $I_L = \{s \in I: s \ge \delta\}$.
* $P = \operatorname{large-bin-pack}(I_L)$.
* Add $I_S$ to $P$ using first-fit to get packing $Q$. Return $Q$.

## Correctness, running time and approximation

Since an FPTAS exists for 1D knapsack, it is possible to approximately fractionally solve the config LP.

Let there be $t$ invocations of large-bin-pack
where $\Size(I) \ge 10$.

### Cost of integral packing

Items of type $i$ that we want to pack as per $\floor{x}$ is
\[ \sum_{j=1}^N T[i, j]\floor{x_j} = (T\floor{x})_i \]
Since there are only $b_i$ items of type $i$, we will pack $\min((T\floor{x})_i, b_i)$ items.
Since $(T\floor{x})_i \ge \min((T\floor{x})_i, b_i)$,
$\floor{x}$ is a feasible solution to $\LP(I_1)$.

When $(T\floor{x})_i \ge b_i$, $I_2$ has 0 items of type $i$.
So $x - \floor{x}$ satisfies the $i^{\textrm{th}}$ constraint of $\LP(I_2)$.
When $(T\floor{x})_i \le b_i$, $I_2$ has $b_i - (T\floor{x})_i$ items.
\[ (T(x-\floor{x}))_i = (Tx)_i - (T\floor{x})_i \ge b_i - (T\floor{x})_i \]
So $x - \floor{x}$ satisfies the $i^{\textrm{th}}$ constraint of $\LP(I_2)$.
Therefore, $x - \floor{x}$ is a feasible solution to $\LP(I_2)$.

\begin{align}
\Sum(\floor{x}) &\le \Sum(x) - \lin(I_2)  \tag{$x - \floor{x}$ is feasible for $\LP(I_2)$}
\\ &\le (\lin(I') + \delta) - \lin(I_2)  \tag{$x$ is approx optimal for $\LP(I')$}
\\ &\le \lin(I) - \lin(I_2) + \delta  \tag{$I' \preceq I$}
\end{align}
<span class="text-danger">How can we compare configuration LPs of $I'$ and $I$
if they categorize items into types differently?</span>

$I_2$ in a certain invocation of large-bin-pack becomes $I$ in the next invocation.
This implies that the cost of packing items as per $\floor{x}$
over all invocations of large-bin-pack is at most $\lin(I) + t\delta \le \Opt(I) + t\delta$.

### Cost of packing discards

As per harmonic grouping,
\[ \Size(J) \le 3\ln\left(\frac{3}{\min(J)}\right)+\frac{9}{2}
\le 3\ln\left(\frac{3}{\delta}\right) + \frac{9}{2} \]
The cost of packing items from $J$ over all invocations of large-bin-pack is
\[ \le \sum_{i=1}^t (2\Size(J^{(i)})+1) \le t\left(6\ln\left(\frac{3}{\delta}\right) + 10\right) \]

Let $m(I')$ be the number of distinct items in $I'$.
By the properties of harmonic grouping, $m(I') \le \Size(I')/2 - 1$.
Since the config LP for $I'$ has $m(I')$ constraints,
$x$ has at most $m(I')$ non-zero entries.

\begin{align}
& \Size(I_2) \le \lin(I_2) \le \Sum(x - \floor{x}) \le |\{j: x_j > 0\}|
\\ &\le m(I') \le \Size(I') / 2 - 1 \le \Size(I) / 2
\end{align}
Since $\Size(I)$ reduces by at least half in each invocation,
\[ t \le \floor{\lg\left(\frac{\Size(I)}{10}\right)} + 1 \]

Therefore, cost of packing discards over all invocations of large-bin-pack is at most
\[ \left(\lg\frac{\Size(I)}{10}+2\right) \left(6\ln(3\Size(I)) + 10\right)
\in O(\lg^2\Size(I)) \subseteq O(\lg^2\Opt(I)) \]

### Running time and total cost

There are $O(\lg(\Size(I))) \subseteq O(\lg(n))$ iterations
and each iteration takes polynomial time, since harmonic grouping, Next-Fit
and solving the config LP can be done in polynomial time.

The cost of packing in the base case ($\Size(I) < 10$) is at most 21.
The cost of integral packing is $\Opt(I) + O\left(\frac{\lg(\Size(I))}{\Size(I)}\right)$.
The cost of packing discards is $O(\lg^2(\Opt(I)))$.
Therefore, total cost of packing is at most $\Opt(I) + O(\lg^2(\Opt(I)))$.
