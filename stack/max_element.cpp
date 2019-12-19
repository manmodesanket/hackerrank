#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define MIN -99999

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<int> arr;
    int t;
    cin>>t;
    int max = MIN;
    for(int i = 0 ; i < t; i++)
    {
        int q;
        cin >> q;
        if(q == 1)
        {
            int e;
            cin >> e;
            arr.push_back(e);
            if(max < e)
            {
                max = e;
            }
        }
        else if(q == 2)
        {
            if(arr.size() > 0)
            {
                arr.pop_back();
                //max = *max_element(arr.begin(), arr.end());
            }
            if(arr.size() == 0)
                max = MIN;
            else
                max = *max_element(arr.begin(), arr.end());
        }
        else
        {
            if(arr.size() > 0)
                cout << max << endl;   
        }
    }  
    return 0;
}
