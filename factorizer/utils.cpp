#include <boost/multiprecision/cpp_int.hpp>
#include <cmath>
#include "utils.hpp"

using namespace std;
using Bint = boost::multiprecision::cpp_int;

Bint isqrt(Bint n){
    return boost::multiprecision::sqrt(n);
}