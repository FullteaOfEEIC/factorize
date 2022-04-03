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
vector<unsigned long> generate_primes(unsigned long MAX);

string PminusOneFactorizer_step1_cppfunc(string s, unsigned long M){
    Bint n(s);
    Bint A("2");
    if(n%A==0){
        return A.str();
    }
    for(unsigned long p : generate_primes(M)){
        unsigned long f = get_f(p, M);
        Bint Mp = pow(Bint(p), f);
        A = powm(A, Mp, n);
    }
    Bint retval = gcd(A-1, n);
    return retval.str();
}

string PminusOneFactorizer_step2_cppfunc(string s, unsigned long M, unsigned long L){
    Bint n(s);
    Bint A("2");
    if(n%A==0){
        return A.str();
    }
    for(unsigned long p : generate_primes(L)){
        if(p<M){
            unsigned long f = get_f(p, M);
            Bint Mp = pow(Bint(p), f);
            A = powm(A, Mp, n);
        }
        else{
            Bint AK = powm(A, p, n);
            Bint candidate = gcd(AK-1, n);
            if(1<candidate and candidate<n){
                return candidate.str();
            }
        }
    }
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

vector<unsigned long> generate_primes(unsigned long MAX){ // we have to make this more smart...
    vector<bool> v(MAX+1, true);
    v.at(0) = false;
    v.at(1) = false;
    vector<unsigned long> retval;
    retval.clear();
    unsigned long sqrt_MAX = (unsigned long)sqrt(MAX);
    for(unsigned long i=2;i<=MAX;i++){
        if(!v.at(i)){
            continue;
        }   
        retval.push_back(i);
        if(i>sqrt_MAX+1){continue;}
        for(unsigned long k=2;k*i<=MAX;k++){
            v.at(k*i) = false;
        }
    }
    return retval;
}