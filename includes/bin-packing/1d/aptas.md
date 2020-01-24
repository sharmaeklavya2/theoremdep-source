$\newcommand{\Size}{\operatorname{size}}\newcommand{\Opt}{\operatorname{opt}}$
Let $I$ be a 1D bin-packing instance.
Let $\Opt(I)$ be the minimum number of bins needed to pack $I$.
Then for any constant $\epsilon$, there is a polynomial-time algorithm which packs $I$ in
$\frac{1}{1-\epsilon}\Opt(I) + 1$ bins.

## Algorithm

Algorithm $\operatorname{bin-pack}(I, \epsilon)$:

* $I_S = \{s \in I: s < \epsilon\}$ and $I_L = \{s \in I: s \ge \epsilon\}$.
* $k = \lfloor \epsilon \Size(I) \rfloor$.
* if $k \texttt{ == } 0$:
    * $P = \operatorname{exact-bin-pack}(I_L)$.
* else:
    * $(I_1, I_2) = \operatorname{linear-grouping}(I_L, k)$.
    * $P_1 = \operatorname{exact-bin-pack}(I_1)$.
    * Pack each item in $I_2$ in a separate bin. Let $P_2$ be the resulting packing.
    * $P' = P_1 + P_2$ (i.e. pack $I_1 + I_2$ using $|P_1| + |P_2|$ bins).
    * Use $P'$, which is a packing of $I_1 + I_2$, to get a packing $P$ for $I_L$.
      This can be done because $I_L \preceq I_1 + I_2$.
* Add $I_S$ to $P$ using first-fit to get packing $Q$. Return $Q$.

In this algorithm, $P$ is a packing of $I_L$ and $Q$ is a packing of $I$.

## Running time and approximation ratio

Since $I_L$ has items of size $\ge \epsilon$,
\[ \Size(I_L) \ge \epsilon n \implies n \le \frac{\Size(I)}{\epsilon} \]

When $k = 0$, then $\epsilon \Size(I_L) < 1 \implies n < \frac{1}{\epsilon^2}$.`
Therefore, there are a constant number of items.
The exact-bin-pack algorithm will run in constant time.
$|P| = \Opt(I_L) < \Opt(I) + k$.

When $k > 0$, then $\epsilon \Size(I_L) \ge 1$.
Using the fact that for $x \ge 1, \lfloor x \rfloor \ge \frac{x}{2}$, we get
\[ k = \lfloor \epsilon \Size(I_L) \rfloor \ge \frac{\epsilon \Size(I_L)}{2} \]
The number of distinct items in $I_1$ is
\[ \frac{n}{k} \le \frac{\frac{\Size(I)}{\epsilon}}{\frac{\epsilon \Size(I_L)}{2}}
= \frac{2}{\epsilon^2} \]
Therefore, there is a constant number of distinct item types.
The maximum number of items a bin can accommodate is $\frac{1}{\epsilon}$, which is also a constant.
So the exact-bin-pack algorithm runs in polynomial time.

We get $|P_1| = \Opt(I_1)$ and $|P_2| = k$.
$|P| = \Opt(I_1) + k \le \Opt(I) + k$ because $I_1 \preceq I_L$ and $\Opt(I_L) \le \Opt(I)$.
So for both cases, $k=0$ and $k>0$, we get
\[ |P| \le \Opt(I) + k \le \Opt(I) + \epsilon \Size(I) \le (1+\epsilon)\Opt(I) \]

Since $Q$ is obtained by adding $I_S$ to $P$ via first-fit,
\begin{align}
|Q| &\le \max\left(|P|, \frac{1}{1-\epsilon}\Size(I)+1\right)
\\ &\le \max\left( (1+\epsilon)\Opt(I), \frac{1}{1-\epsilon}\Opt(I)+1 \right)
\\ &\le \frac{1}{1-\epsilon}\Opt(I)+1
\end{align}
