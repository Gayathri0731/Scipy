import numpy as np
import scipy.special as special

# Cube root
print("cube root: ", special.cbrt(np.array([64,125,729])))

# 10^x
print("exp 10: ", special.exp10([2,3]))

# combinations : special.comb(N,k) where
# N is an object
# K is no.of.object being picked (order does not matter)
print("combinations: ",special.comb(10,3))

# Permutations : special.perm(N,k) where
# N is an object
# K is no.of.object being picked (order matters)
print("permutations: ",special.perm(10,3))

# LogSumExp : computes the log of the sum of exponentials of inputs elements
# input : [x1,x2,x3,x4]
# O/p : log e((e^x1,e^x2,...,e^x4))
print("LogSumExp: ", special.logsumexp([1,2,3,4]))

# Lambert w function
# Defined as inverse of x*(e^x)
# w(z) is such that z=w(z)*(e^w(z)) where
# z is complex number
print("w(1): ", special.lambertw(1))