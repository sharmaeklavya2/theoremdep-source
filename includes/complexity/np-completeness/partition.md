The partition problem is in NP because we can use the partitioning as a certificate.
To validate the certificate, just check if the partitions are disjoint, span the original set
and have the same sum.

The partition problem is NP-hard because it can be reduced in polynomial time to the subset-sum problem.
Proving this theorem is given as exercise 34.5-5 in CLRS edition 3, page 1101.
See [solutions by Bodnar and Lohr](https://sites.math.rutgers.edu/~ajl213/CLRS/Ch34.pdf).
