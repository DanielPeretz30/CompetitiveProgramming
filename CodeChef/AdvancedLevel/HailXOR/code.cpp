//
//  Vac_2.cpp
//  codechef_1
//
//  Created by Daniel peretz on 09/12/2020.
//

#include <limits>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
using ll = long long;
using namespace std;

int count_bits(ll x);
int Find_MSB(ll n);



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int T;
    cin>> T;
    for (int t = 1; t<=T; t++) {
        ll n,x;
        cin>>n>>x;
        vector<ll> A(n);
        for (int i = 0; i<n; i++) {
            cin>>A[i];
        }
        ll light = 0;
        for (int i = 0; i<n; i++) {
            if (i == n-1) {
                A[n-1] = A[n-1]^light;
                if (x%2 != 0) {
                        ll num = (Find_MSB(A[n-2])!= 0)? Find_MSB(A[n-2]) : 1 ;
                    if (num == 1 && n>=3) {
                        A[n-1] = A[n-1];
                    }
                    else{
                        A[n-1] = A[n-1]^num;
                        A[n-2] = A[n-2]^num;
                    }
                }
                x = 0;
                break;
            }
            ll common_bits = A[i]&light;
            A[i] = A[i]^common_bits;
            light = light^common_bits;
            // till here is free //
            ll remain_bits = count_bits(A[i]);
            if (remain_bits <= x) {
                light = light^A[i];
                A[i] = 0;
                x = x - remain_bits;
            }
            else{
                for (int j = 1; j<=x; j++) {
                    ll num = Find_MSB(A[i]);
                    A[i] = A[i]^num;
                    light = light^num;
                }
                x = 0;
            }
        }

               
        // print //
        for (int i = 0; i<n; i++) {
            cout<<A[i] << " ";
        }
        cout<<endl;
    }
    
return 0;
}

int count_bits(ll x){
    int count = 0;
    while (x) {
        count += x & 1;
        x >>= 1;
    }
    return count;
}

int Find_MSB(ll n)
{
    if (n == 0)
        return 0;
    
    int msb = 0;
    n = n / 2;
    while (n != 0) {
        n = n / 2;
        msb++;
    }
    return (1 << msb);
}

