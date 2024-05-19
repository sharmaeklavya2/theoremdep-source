<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\WMMS}{\mathrm{WMMS}}$
$\newcommand{\pessShare}{\mathrm{pessShare}}$
</span>
Let $([n], [m], V, w)$ be a fair division instance of indivisible items
(each agent $i$ has entitlement $w_i$).
If $v_i$ is superadditive, then $\WMMS_i ≤ w_iv_i([m])$ and $\pessShare_i ≤ w_iv_i([m])$.

## Proof

Let $P$ be agent $i$'s WMMS partition. Then
\[ \frac{\WMMS_i}{w_i} = \min_{j=1}^n \frac{v_i(P_j)}{w_j}
    ≤ \sum_{j=1}^n w_j\left(\frac{v_i(P_j)}{w_j}\right) ≤ v_i([m]). \]

Let $P$ be agent $i$'s $\ell$-out-of-$d$-partition.
Then her $\ell$-out-of-$d$-share is at most
\[ \frac{\ell}{d}\sum_{j=1}^n v_i(P_j) ≤ \frac{\ell}{d}v_i([m]). \]
\[ \pessShare_i \defeq \sup_{1 ≤ \ell ≤ d: \ell/d ≤ w_i} \ell\textrm{-out-of-}d\textrm{-share}_i
    ≤ \sup_{1 ≤ \ell ≤ d: \ell/d ≤ w_i} (\ell/d)v_i([m]) ≤ w_iv_i([m]). \]
