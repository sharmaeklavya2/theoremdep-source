<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\Size}{\operatorname{size}}\newcommand{\Opt}{\operatorname{opt}}$
$\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$
</span>
Let $I$ be a 1D bin packing instance containing $n$ items.
Without loss of generality, assume bins have size 1.
Then for any constant $\eps > 0$, there is an algorithm that packs $I$ in
$\frac{1}{1-\eps}\Opt(I) + 1$ bins in $O((n+1)^R R/\eps^2)$ time,
where $R = \ceil{1/\eps}^{\ceil{1/\eps^2}}$.

## Algorithm

Algorithm $\operatorname{binPack}(I, \eps)$:

* $I_S = \{s \in I: s \le \eps\}$ and $I_L = \{s \in I: s > \eps\}$.
* $k = \floor{\eps \Size(I_L)} + 1$.
* $(I_1, I_2) = \operatorname{linear-grouping}(I_L, k)$.
* $P_1 = \operatorname{exactBinPack}(I_1)$.
* Pack each item in $I_2$ in a separate bin. Let $P_2$ be the resulting packing.
* $P' = P_1 + P_2$ (i.e. pack $I_1 + I_2$ using $|P_1| + |P_2|$ bins).
* Use $P'$, which is a packing of $I_1 + I_2$, to get a packing $P$ for $I_L$.
  This can be done because $I_L \preceq I_1 + I_2$.
* Add $I_S$ to $P$ using first-fit to get packing $Q$. Return $Q$.

In this algorithm, $P$ is a packing of $I_L$ and $Q$ is a packing of $I$.

## Running time and approximation ratio

Since $I_L$ has items of size $> \eps$,
\[ \Size(I_L) \ge \eps |I_L| \implies |I_L| \le \frac{\Size(I_L)}{\eps} \]

The number of distinct items in $I_1$ is
\[ \ceil{\frac{|I_L|}{k}}
\le \ceil{\frac{\Size(I_L)/\eps}{\floor{\eps \Size(I_L)} + 1}}
\le \ceil{\frac{1}{\eps^2}} \]
The maximum number of items a bin can accommodate is $\ceil{\frac{1}{\eps}}-1$.
So the `exactBinPack` algorithm runs in time $O((n+1)^R R/\eps^2)$,
where $R = \ceil{1/\eps}^{\ceil{1/\eps^2}}$.

By the property of linear grouping, we get $I_1 \preceq I_L$. Therefore,
\begin{align}
|P| &= |P_1| + |P_2| \le \Opt(I_1) + k-1
\\ &\le \Opt(I_L) + \eps \Size(I_L)
\le (1+\eps)\Opt(I_L)
\\ &\le (1+\eps)\Opt(I)
\end{align}

Since $Q$ is obtained by adding $I_S$ to $P$ via first-fit,
\begin{align}
|Q| &\le \max\left(|P|, \frac{1}{1-\eps}\Size(I)+1\right)
\\ &\le \max\left( (1+\eps)\Opt(I), \frac{1}{1-\eps}\Opt(I)+1 \right)
\\ &\le \frac{1}{1-\eps}\Opt(I)+1
\end{align}
