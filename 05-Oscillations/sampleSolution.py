import math
import itertools

l=list(map(int, input().strip().split()))

signum = lambda z : int(z/math.fabs(z))

deltas=[l[i+1]-l[i] for i in range(0, len(l)-1)]

delta_signs=[signum(i) for i in deltas]

lengths_of_groups = [len([*y]) for x, y in itertools.groupby(delta_signs)]

print("true" if len(set(lengths_of_groups))==1 else "false")

