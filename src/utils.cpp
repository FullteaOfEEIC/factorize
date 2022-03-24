#include "utils.hpp"

#include <boost/multiprecision/cpp_int.hpp>
#include <cmath>
#include <cassert>

using namespace std;
using Bint = boost::multiprecision::cpp_int;

Bint isqrt(Bint n){
    return boost::multiprecision::sqrt(n);
}

unsigned long ilog(Bint n){
    unsigned long result = 0;
    while(n>0){
        n=n/2;
        result++;
    }
    return result;
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

Bint jacobi_symbol(Bint a, Bint p){
    //returns (a/p)
    //https://en.wikipedia.org/wiki/Jacobi_symbol
    assert(p%2==1);
    a = a%p; // (12) p43 [Wada 2001]
    if(a==1){ // (11) p43 [Wada 2001]
        return ONE;
    }
    else if(a==-1){ // (14) p43 [Wada 2001]
        if(a%4==1){
            return ONE;
        }
        else{
            return MINUS_ONE;
        }
    }
    else if(a==2){ // (15) p43 [Wada 2001]// (15) p43 [Wada 2001]
        switch(a%8){
            case 1:
            case 7:
                return ONE;
            case 3:
            case 5:
                return MINUS_ONE;
        }
    }

    if(a%2==0){ // (13) p43 [Wada 2001]
        return jacobi_symbol(2, p) * jacobi_symbol(a/2, p);
    }
    else{ // (16) p43 [Wada 2001]
        assert(euclidean_gcd(a,p)==1);
        if(a%4==1 or p%4==1){
            return jacobi_symbol(p, a);
        }
        else{
            return MINUS_ONE * jacobi_symbol(p, a);
        }
    }
}