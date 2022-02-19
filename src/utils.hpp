#ifndef UTILS_HPP_FACTORIZER_4e17c669_cf51_4c34_8ac1_ae3306060740
#define UTILS_HPP_FACTORIZER_4e17c669_cf51_4c34_8ac1_ae3306060740

#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
using Bint = boost::multiprecision::cpp_int;

Bint isqrt(Bint n);

unsigned long ilog(Bint n);

Bint euclidean_gcd(Bint a, Bint b);

#endif // UTILS_HPP_FACTORIZER_4e17c669_cf51_4c34_8ac1_ae3306060740