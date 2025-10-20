#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N = 0, R = 0, T = 0, qtd = 0;
    cin >> N >> R; // lê N e R separados por espaço

    vector<int> arr(N);
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    if (R < arr[0])
        qtd = 0;
    else if (R == arr[0])
        qtd = 1;
    else
    {
        for (int i = 0; i < N; i++)
        {
            T += arr[i];
            if (T <= R)
                qtd += 1;
            else
                break;
        }
    }

    cout << qtd << endl;
    return 0;
}
