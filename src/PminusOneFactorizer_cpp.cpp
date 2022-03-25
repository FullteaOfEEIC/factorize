#include "utils.hpp"

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;
using Bint = boost::multiprecision::cpp_int;

//return f s.t. q^f<M<=q^(f+1)
unsigned long get_f(unsigned long q, unsigned long M);

string PminusOneFactorizer_step1_cppfunc(string s, unsigned long M){
    Bint n(s);
    Bint A("2");
    if(n%A==0){
        return A.str();
    }
    vector<bool> v(M+1, true);
    v.at(0) = false;
    v.at(1) = false;
    unsigned long sqrt_M = (long)sqrt(M);
    for(unsigned long i=2;i<=M;i++){
        if(!v.at(i)){
            continue;
        }
        unsigned long f = get_f(i, M);
        Bint Mp = pow(Bint(i), f);
        A = powm(A, Mp, n);
        if(i>sqrt_M+1){continue;}
        for(unsigned long k=2;k*i<=M;k++){
            v.at(k*i) = false;
        }
    }
    Bint retval = gcd(A-1, n);
    return retval.str();
}

string PminusOneFactorizer_step2_cppfunc(string s, unsigned long M){
    return "1";
}


unsigned long get_f(unsigned long q, unsigned long M){
    unsigned long f = log(M)/log(q);
    if(pow(q,f)==M){
        return f-1;
    }
    else{
        assert(pow(q,f)<M and M<=pow(q,f+1));
        return f;
    }
}