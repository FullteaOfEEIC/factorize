from factorizer import BruteForceFactorizer
divider = BruteForceFactorizer(timeout=5)
d=divider.factorize(221)
print(d)
d=divider.factorize(144483604528043653279487)
print(d)
