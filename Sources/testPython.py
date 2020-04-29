import math
import itertools

for a, b in itertools.product(range(5, 90, 5), range(1, 100)):
    if math.gcd(a, b) == 5 and a * b // math.gcd(a, b) == 90:
        print("a={},b={}".format(a, b))
        continue
