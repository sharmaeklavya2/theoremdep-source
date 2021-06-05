<span class="invisible">
$\newcommand{\Size}{\operatorname{size}}\newcommand{\Opt}{\operatorname{opt}}$
$\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$
</span>
Let $I$ be a 1D bin packing instance.
Without loss of generality, assume bins have size 1.
Let $\Opt(I)$ be the minimum number of bins needed to pack $I$.
Then for any constant $\epsilon$, there is a polynomial-time algorithm which packs $I$ in
$\frac{1}{1-\epsilon}\Opt(I) + 1$ bins.

## Algorithm

Algorithm $\operatorname{bin-pack}(I, \epsilon)$:

* $I_S = \{s \in I: s < \epsilon\}$ and $I_L = \{s \in I: s \ge \epsilon\}$.
* $k = \floor{\epsilon \Size(I_L)} + 1$.
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
\[ \Size(I_L) \ge \epsilon |I_L| \implies |I_L| \le \frac{\Size(I_L)}{\epsilon} \]

The number of distinct items in $I_1$ is
\[ \ceil{\frac{|I_L|}{k}}
\le 1 + \frac{\Size(I_L)/\epsilon}{\floor{\epsilon \Size(I_L)} + 1}
\le 1 + \frac{1}{\epsilon^2} \]
Therefore, there is a constant number of distinct item types.
The maximum number of items a bin can accommodate is $\frac{1}{\epsilon}$, which is also a constant.
So the exact-bin-pack algorithm runs in polynomial time.

By the property of linear grouping, we get $I_1 \preceq I_L$. Therefore,
\begin{align}
|P| &= |P_1| + |P_2| \le \Opt(I_1) + k-1
\\ &\le \Opt(I_L) + \epsilon \Size(I_L)
\le (1+\epsilon)\Opt(I_L)
\\ &\le (1+\epsilon)\Opt(I)
\end{align}

Since $Q$ is obtained by adding $I_S$ to $P$ via first-fit,
\begin{align}
|Q| &\le \max\left(|P|, \frac{1}{1-\epsilon}\Size(I)+1\right)
\\ &\le \max\left( (1+\epsilon)\Opt(I), \frac{1}{1-\epsilon}\Opt(I)+1 \right)
\\ &\le \frac{1}{1-\epsilon}\Opt(I)+1
\end{align}
