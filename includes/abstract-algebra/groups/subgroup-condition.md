Let $H$ be a subset of $G$. $H$ is a subgroup of $G$ iff

* $H$ is closed under $*$.
* $\operatorname{id}(G) \in H$.
* $\forall h \in H, h^{-1} \in H$.

## Proof

* Closure: Given.

* Associativity: True since $H$ inherits its operator from $G$.

* Identity: Let $e_G = \operatorname{id}(G)$ and $e_H = \operatorname{id}(H)$ (if it exists).
  We'll prove both sides of the implication:

    * $\forall h \in H, he_G = e_Gh = h$ because $h \in G$.
      Since identity of a group is unique, $e_G \in H \Rightarrow e_H \textrm{ exists}$.
    * Now assume that $e_H$ exists.
      $e_He_H = e_H$ because $e_H = \operatorname{id}(H)$.
      $e_He_G = e_H$ because $e_G = \operatorname{id}(G)$ and $e_H \in G$.
      Therefore, $e_G = e_H \Rightarrow e_G \in H$.

* Inverse: Since inverse is unique in $G$, only the inverse in $G$ has the possibility of being an inverse in $H$.
