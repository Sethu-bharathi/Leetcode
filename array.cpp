#include <iostream>
#include <vector>
using namespace std;

void roots(int a,int b,int c){
    int x=(b*b)-(4*a*c);
    if(x>=0){
        int x1=(-b-x)/(2*a),x2=(-b+x)/(2*a);
        cout<<x1<<" "<<x2;
    }
    else
        cout<<"Imaginary";
}
int main(){
    roots(1,5,6);
    return 0;
}
