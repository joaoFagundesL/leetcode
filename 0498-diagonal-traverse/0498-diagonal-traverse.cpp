// --------------------------------------------------<TEMPLATE>-------------------------------------------------- 
// --------------------<optimizations>-------------------- 
 
/* 
#pragma GCC optimize("Ofast,unroll-loops") 
#pragma GCC target("avx,avx2,fma") 
*/  

// ---------------</HEADERS and NAMESPACES>--------------- 
#include <bits/stdc++.h>
#define ff                      first
#define ss                      second
#define pb                      push_back
#define forn(i, j, k, in)       for (int i = j; i < k; i += in)
#define rfor(i, j, k, in)       for (int i = j; i >= k; i -= in)
#define fora(x, a)              for (auto &x : a)
#define sz(a)                   int((a).size()) 
#define all(cont)               cont.begin(), cont.end()
using namespace std;

// >
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vii;
typedef vector<vi> vvi;
typedef map<int, int> mpii;
typedef set<int> seti;

// >
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int uint64;

// ------------------</DEBUGGING STUFF>------------------- 
#define debug(x)        cout << '>' << #x << ':' << x << endl;

// ----<PRINTF>----- 
#define pf              printf 
#define pfi(x)          printf("%d\n",x); 
#define pfi2(x,y)       printf("%d %d\n",x,y); 
#define pfi3(x,y,z)     printf("%d %d %d\n",x,y,z); 
template <class T>
void print_v(vector<T> &v) { cout << "{ "; fora(x,v) cout << x << " "; cout << "\b}" << endl; }

class Solution {
public:
        vi findDiagonalOrder(vvi& mat) {
                map<int, vi> hash;
                int n = sz(mat), m = sz(mat[0]);
                vi ans;
                
                forn(i, 0, n, 1) {
                       forn(j, 0, m, 1) {
                                // the sum represents each diagonal
                                hash[i+j].pb(mat[i][j]);
                        }
                }
                
                fora(pair, hash) {
                        int len = sz(pair.ss);
                        // even number = go up
                        if(!(pair.ff & 1)) {
                                rfor(i,len-1,0,1) {
                                        ans.pb(pair.ss[i]);
                                }
                        } else {
                                forn(i,0,len,1) {
                                        ans.pb(pair.ss[i]);
                                }
                        }
                }

                return ans;
    }
};