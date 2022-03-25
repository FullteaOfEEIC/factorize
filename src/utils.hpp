#ifndef UTILS_HPP_FACTORIZER_4e17c669_cf51_4c34_8ac1_ae3306060740
#define UTILS_HPP_FACTORIZER_4e17c669_cf51_4c34_8ac1_ae3306060740

#include <boost/multiprecision/cpp_int.hpp>
using Bint = boost::multiprecision::cpp_int;

unsigned long ilog(Bint n);

Bint jacobi_symbol(Bint a, Bint p);
Bint next_prime(Bint n);

#define ZERO Bint("0")
#define ONE Bint("1")
#define TWO Bint("2")
#define MINUS_ONE Bint("-1")


#endif // UTILS_HPP_FACTORIZER_4e17c669_cf51_4c34_8ac1_ae3306060740