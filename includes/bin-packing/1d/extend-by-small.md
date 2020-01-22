Let $I$ be a 1D bin-packing instance.
Let $\operatorname{size}(S) = \sum_{i=1}^n s_i$.

Let $I_L = \{s \in I: s > \epsilon\}$ and $I_S = \{s \in I: s \le \epsilon\}$.
Let there be a packing of $I_L$ into $m$ bins.
Then we can use that packing to get a packing of $I$ into at most
$\max(m, \frac{1}{1-\epsilon}\operatorname{size}(I)+1)$ bins.

## Proof

The first-fit algorithm packs items into the first bin in which the item can be packed.
We'll take the packing of $I_L$ and add small items using the first-fit algorithm.
Let $m'$ be the number of bins used.

If all small items fit without using any new bins, then $m' = m$.

If some new bins had to be opened to fit some small items,
then every bin except that last must have empty space $< \epsilon$.
Therefore,
\[ \operatorname{size}(I) \ge (m'-1)(1-\epsilon)
\implies m' \le \frac{1}{1-\epsilon}\operatorname{size}(I)+1 \]

Therefore, $m' \le \max(m, \frac{1}{1-\epsilon}\operatorname{size}(I)+1)$.
