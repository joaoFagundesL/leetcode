// --------------------------------------------------<TEMPLATE>-------------------------------------------------- 
// --------------------<optimizations>-------------------- 
 
/* 
#pragma GCC optimize("Ofast,unroll-loops") 
#pragma GCC target("avx,avx2,fma") 
*/  

// ---------------</HEADERS and NAMESPACES>--------------- 
#include <bits/stdc++.h>
#include <iostream>
#define ff                      first
#define ss                      second
#define pb                      push_back
#define mt                      make_tuple
#define mk                      make_pair
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
typedef unordered_map<int,int>upii;
typedef unordered_map<char,int>upci;
typedef map<int, vi> mpiv;
typedef set<int> seti;
typedef tuple<int, int> tii;
typedef tuple<int, int, int> tiii;

// >
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int uint64;

// ------------------</DEBUGGING STUFF>------------------- 
void dbg_out() { cout << endl; }
template<typename Head, typename... Tail>
void dbg_out(Head H, Tail... T) { cout << ' ' << H; dbg_out(T...); }
#define dbg(...) cout << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)

// ----<PRINTF>----- 
#define pf              printf 

template <class T>
void print_v(vector<T> &v) { cout << "{ "; fora(x,v) cout << x << " "; cout << "\b}" << endl; }

template<typename KeyType, typename ValueType>
bool contains(const KeyType& key, const unordered_map<KeyType, ValueType>& map) {
    return map.find(key) != map.end();
}

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        upci required,freq;
        vi ans;
        int n=sz(s),m=sz(p),cnt=0;
    
        fora(e,p)
            required[e]++;
        
        forn(i,0,m,1){
            if(contains(s[i],required)){
                freq[s[i]]++;
                if(freq[s[i]]<=required[s[i]])
                    ++cnt;
            }
        }

        if(cnt==m)
            ans.pb(0);
        
        int start=0,end=m;
        while(end<n){
            if(contains(s[start], required)) {
                freq[s[start]]--;
                if(freq[s[start]] < required[s[start]])
                    --cnt;
            }
            if(contains(s[end], required)){
                freq[s[end]]++;
                if(freq[s[end]] <= required[s[end]]){
                    ++cnt;
                }
             }
            end++;start++;
            if(cnt == m)
                ans.pb(start);
        }

        return ans;
    }
};