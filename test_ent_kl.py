import numpy as np
from scipy import stats


def ent(w):
	return stats.entropy(w, None, 2)


def kl(w1,w2):
    return stats.entropy(w1, w2, 2)


p1 = np.array([0.5, 0.5])
p2 = np.array([1.0, 0])
p3 = np.array([0.991, 0.01])


print("entropy")
print(ent(p1))
print(ent(p2))
print(ent(p3))

print("kl divergence")
print(kl(p1, p1))
print(kl(p1, p2))
print(kl(p1, p3))
print(kl(p2, p3))
