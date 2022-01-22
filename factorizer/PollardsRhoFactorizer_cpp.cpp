#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include "utils.hpp"
using namespace std;
using Bint = boost::multiprecision::cpp_int;

Bint f(Bint *x, Bint *n);
struct LinkedList{
    Bint value;
    LinkedList *after;
}typedef LinkedList;


string PollardsRhoFactorizer_cppfunc(string s){
    Bint n(s);
    
    LinkedList z1, z2;
    LinkedList *x = new LinkedList;
    LinkedList *y = new LinkedList;
    x->value = 2;
    y->value = f(&(x->value), &n);
    x->after = y;

    Bint d = euclidean_gcd(abs(x->value-y->value), n);
    Bint i=1;
    while(d==1){
        LinkedList *z1 = new LinkedList;
        LinkedList *z2 = new LinkedList;
        y->after = z1;
        z1->after = z2;
        z1->value = f(&(y->value), &n);
        z2->value = f(&(z1->value), &n);
        y = z2;
        LinkedList *tmp = x;
        x = x->after;
        delete tmp;
        d = euclidean_gcd(abs(x->value-y->value), n);
        i++;
    }


    if(d<n){
        return d.str();
    }
    else{
        return "1";
    }
}

Bint f(Bint *x, Bint *n){
    return (boost::multiprecision::pow(*x,(unsigned)2)+1)%(*n);
}
