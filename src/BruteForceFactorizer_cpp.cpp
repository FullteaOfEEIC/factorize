#include "utils.hpp"

#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>
using namespace std;
using Bint = boost::multiprecision::cpp_int;

string BruteForceFactorizer_cppfunc(string s){
    Bint n(s);
    Bint sqrt_n = boost::multiprecision::sqrt(n);
    for(Bint i=2;i<=sqrt_n+1;i++){
        if(n%i==0){
            return i.str();
        }
    }
    return "1";
}
