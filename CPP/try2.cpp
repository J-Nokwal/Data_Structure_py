#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
public:
    bool canPlaceFlowers(vector<int> &fb, int n)
    {
        int ln = fb.size();
        int pt = 0, last = 0;
        // for (int i=0;i<n;i++){}
        while (pt < ln - 1)
        {
            if (pt == ln || n == 0)
                break;
            if (fb[pt]){
                
            }
        }
        if (n == 0)
        {
            return true;
        }
        return false;
    }
};
int main()
{

    Solution a;
    vector<int> fb = {1, 0, 0, 0, 1};
    a.canPlaceFlowers(fb, 1);
}