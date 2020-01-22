The subset-sum problem is in NP because we can use
the subset of items which sum to the target as the certificate.
To verify the certificate, just check that each element is in the original (multi-)set,
has not been repeated (more times than in the original set) and that they sum to the target.

Subset-sum is NP-hard because it can be reduced in polynomial-time to 3-sat.
See CLRS ed3, Theorem 34.15, page 1097 for proof.
