# factorize

This is a simple factorization tool.

Here is the simplest example.

```usage.py
from factorizer import BruteForceFactorizer
divider = BruteForceFactorizer() 
divider.factorize(57) # Devide number in order, starting with 2, 3, 4, 5...
#>>>(3,19)
```

# Install
## Requirements
 - boost
 
 if you are using apt, you can install with
 ```
 apt install libboost-dev
 ```

 ## Install
 You can just use pip to install
 ```
pip install git+https://github.com/FullteaOfEEIC/factorizer.git
 ```
 
 # Usage