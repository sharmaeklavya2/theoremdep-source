A directed graph $G$ is the pair $(V, E)$, where $E$ contains some ordered pairs on $V$.
I.e. $E \subseteq V \times V$.

An undirected graph $G$ is the pair $(V, E)$, where $E$ contains some 2-element subsets of $V$.
These subsets are often denoted as $(u, v)$ instead of $\{u, v\}$.

When $E$ is allowed to be a multi-set (a set which can have repeated elements),
we get directed multigraphs or undirected multigraphs.

### Definitions

* $V$ is called the set of **vertices**.
* $E$ is called the set of **edges**.
* If $(u, v) \in E$, then $u$ is **adjacent to** $v$ and $v$ is **adjacent to** $u$.
$u$ and $v$ are said to be **neighbors**.
* The edge $(u, v)$ is called a **loop** iff $u = v$.
A graph with no loops is called **loop-free** or **simple**.
* $G' = (V', E')$ is a **subgraph** of $G = (V, E)$ iff
$G'$ is a graph and $V' \subseteq V$ and $E' \subseteq E$.
* If $G = (V, E)$ and $V' \subseteq V$, the **subgraph of $G$ induced by $V'$**
is the subgraph $G' = (V', E \cap (V' \times V'))$.

#### Definitions for directed graphs

* The edge $(u, v)$ is **from $u$ to $v$**.
* For $e = (u, v) \in E$, $u$ and $v$ are **endpoints** of $e$.
  $u$ is the **source** of $e$ and $v$ is the **destination** or **target** of $v$.
* $e = (u, v) \in E$ means $e$ is
    * **incident from** $u$.
    * **incident to** $v$.
    * **incident on** $u$ and $v$.
* The number of edges incident to $v$ is the **in-degree** of $v$, denoted as $\operatorname{indeg}_G(v)$.
* The number of edges incident from $v$ is the **out-degree** of $v$, denoted as $\operatorname{outdeg}_G(v)$.
* The sum of in-degree and out-degree is called **degree**, denoted as $\deg_G(v)$.
* The **undirected version** of a directed graph is an undirected graph obtained
by removing the direction of every edge in the directed graph.

#### Definitions for undirected graphs

* The edge $(u, v)$ is **between $u$ and $v$**.
* For $e = (u, v) \in E$, $u$ and $v$ are **endpoints** of $e$.
* $e = (u, v) \in E$ means $e$ is **incident on** $u$ and $v$.
* The number of edges incident on $v$ is called the **degree** of $v$,
denoted as $\operatorname{deg}_G(v)$.
