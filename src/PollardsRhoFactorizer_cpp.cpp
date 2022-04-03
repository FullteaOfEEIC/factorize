#include "utils.hpp"

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>
#include <memory>
using namespace std;
using Bint = boost::multiprecision::cpp_int;

Bint f(Bint const& x, Bint const& c, Bint const& n);


class LinkedList{
    public:
        LinkedList(Bint value_);
        ~LinkedList();
        Bint getValue();
        LinkedList* getAfter();
        void setAfter(LinkedList* after_);
    private:
        Bint value;
        LinkedList* after;
};

LinkedList::LinkedList(Bint value_){
    value = value_;
    after = nullptr;
}

LinkedList::~LinkedList(){
    ;
}

Bint LinkedList::getValue(){
    return value;
}

LinkedList* LinkedList::getAfter(){
    return after;
}

void LinkedList::setAfter(LinkedList* after_){
    after = after_;
}



string PollardsRhoFactorizer_cppfunc(string s, long c_){
    Bint n(s);
    Bint c(c_);
    LinkedList* x = new LinkedList(Bint(2));
    LinkedList* y = new LinkedList(f(x->getValue(), c, n));
    x->setAfter(y);
    Bint d = gcd(abs(x->getValue()-y->getValue()), n);
    while(d==1){
        LinkedList* z1 = new LinkedList(f(y->getValue(), c, n));
        LinkedList* z2 = new LinkedList(f(z1->getValue(), c, n));
        y->setAfter(z1);
        z1->setAfter(z2);
        y = z2;
        x = x->getAfter();
        d = gcd(abs(x->getValue()-y->getValue()), n);
    }


    if(d<n){
        return d.str();
    }
    else{
        return "1";
    }
}

Bint f(Bint const& x, Bint const& c, Bint const& n){
    return (x*x+c)%n;
}
