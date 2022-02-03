// { Driver Code Starts
//Initial template for C++


#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution{
    public:
    string ExcelColumn(int N)
   {
       // Your code goes here
       char a[26];
       for(int i=0;i<26;i++){
           a[i]=char(65+i);
       }
       int t=N,y;
       string res="";
       while(t>0){
           y=(t-1)%26;
           res=a[y]+res;
           t=(t-1)/26;
       }
       return res;
   }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        Solution ob;
        cout<<ob.ExcelColumn(n)<<endl;
    }
    return 0;
}
      // } Driver Code Ends