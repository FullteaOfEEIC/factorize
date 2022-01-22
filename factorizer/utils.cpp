#include <boost/multiprecision/cpp_int.hpp>
#include <cmath>
#include "utils.hpp"

using namespace std;
using Bint = boost::multiprecision::cpp_int;

Bint isqrt(Bint n){
    return boost::multiprecision::sqrt(n);
}

Bint euclidean_gcd(Bint a, Bint b){
    if(a < b) return euclidean_gcd(b, a);
    if(b==0){
        return a;
    }

    Bint r;
    r = a%b;
    while(r){
        a = b;
        b = r;
        r = a%b;
    }
    return b;
}
