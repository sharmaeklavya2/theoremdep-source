Let $R$ be a commutative ring. Then $R[x]$ is a commutative ring.

## Proof

Let $p, q, r \in R[x]$.

* Closure of addition:

    If $p = 0$, $p+q = q \in R[x]$. If $q = 0$, $p+q = p \in R[x]$.

    $(p+q)_i = p_i + q_i \in R$.
    $\deg(p+q) \le \max(\deg(p), \deg(q))$.
    Therefore, $p+q \in R[x]$.

* Associativity of addition:

    \begin{align}
    & (p+(q+r))_i = p_i + (q+r)_i
    \\ &= p_i + (q_i + r_i) = (p_i + q_i) + r_i
    \\ &= (p+q)_i + r_i = ((p+q)+r)_i
    \end{align}

* Commutativity of addition: $(p+q)_i = p_i + q_i = q_i + p_i = (q+p)_i$.
* Additive identity: $(0+p)_i = 0_i + p_i = 0 + p_i = p_i$.
* Additive inverse: $(-p)_i = -p_i$. Therefore, $(p+(-p))_i = p_i + (-p_i) = 0 = 0_i$.

Therefore, $R[x]$ is an abelian group under addition.

* Closure of multiplication:

    If $p = 0$ or $q = 0$, $pq = 0 \in R[x]$.

    $(pq)_i = \sum_{j=0}^i p_jq_{i-j} \in R$ and
    $\deg(pq) \le \deg(p) + \deg(q)$.
    Therefore, $pq \in R[x]$.

* Associativity of multiplication: $(pq)_i = \sum_{j=0}^i p_jq_{i-j} \in R$.

    \begin{align}
    & ((pq)r)_i
    \\ &= \sum_{j=0}^i (pq)_jr_{i-j}
    \\ &= \sum_{j=0}^i (pq)_jr_{i-j}
    \\ &= \sum_{j=0}^i \left( \sum_{k=0}^j p_k q_{j-k} \right) r_{i-j}
    \\ &= \sum_{j=0}^i \sum_{k=0}^j p_k q_{j-k}r_{i-j} \tag{distributivity in $R$}
    \\ &= \sum_{k=0}^i \sum_{j=k}^i p_k q_{j-k}r_{i-j}
    \\ &= \sum_{k=0}^i \sum_{t=0}^{i-k} p_k q_t r_{i-k-t}
    \\ &= \sum_{k=0}^i p_k \left( \sum_{t=0}^{i-k} q_t r_{i-k-t} \right) \tag{distributivity in $R$}
    \\ &= \sum_{k=0}^i p_k (qr)_{i-k}
    \\ &= (p(qr))_i
    \end{align}

* Commutativity of multiplication:

    \begin{align}
    & (ab)_i
    \\ &= \sum_{j=0}^i a_jb_{i-j}
    \\ &= \sum_{j=0}^i b_{i-j}a_j \tag{$\because$ $R$ is commutative}
    \\ &= \sum_{k=0}^i b_ka_{i-k} \tag{$k = i - j$}
    \\ &= (ba)_i
    \end{align}

* Distributivity:

    \begin{align}
    & (p(q+r))_i
    \\ &= \sum_{j=0}^i p_j (q+r)_{i-j}
    \\ &= \sum_{j=0}^i p_j (q_{i-j} + r_{i-j})
    \\ &= \sum_{j=0}^i (p_jq_{i-j} + p_jr_{i-j}) \tag{distributivity in $R$}
    \\ &= \sum_{j=0}^i p_jq_{i-j} + \sum_{j=0}^i p_jr_{i-j} \tag{additive commutativity in $R$}
    \\ &= (pq)_i + (pr)_i
    \\ &= (pq+pr)_i
    \end{align}

    Distributivity in the other direction can be proved similarly.
