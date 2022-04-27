#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main()
{
    cout << "Hello, world!";
    unordered_map<int, int> mp;
    // vector<int> ct = {1, 1, 2, 2, 3, 3};
    vector<int> ct = {6,6,6,6};
    int ln = ct.size();
    for (int i = 0; i < ln; i++)
    {
        if (mp.find(ct[i]) == mp.end())
        {
            mp.insert({ct[i], 1});
        }
        else
        {
            (mp.find(ct[i]))->second += 1;
        }
    }
    if (mp.size() >= ln / 2)
    {
        cout<< ln / 2;
    }
    cout<<mp.size();
    return 0;
}