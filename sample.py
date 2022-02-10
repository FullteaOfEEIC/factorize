from factorizer import BruteForceFactorizer
divider = BruteForceFactorizer(timeout=5)
facts = divider.factorize(221)
print(facts)
