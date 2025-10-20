#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N = 0, M = 0, T = 0, qtd = 0;
    cin >> N >> M; // lê N e M separados por espaço

    vector<int> embalagens(N);
    vector<int> brinquedos(M);

    for (int i = 0; i < N; i++)
    {
        cin >> embalagens[i];
    }
    for (int i = 0; i < M; i++)
    {
        cin >> brinquedos[i];
    }

    // ordena os vetores em ordem crescente
    sort(brinquedos.begin(), brinquedos.end());
    sort(embalagens.begin(), embalagens.end());

    for (int i = 0, j = 0; i < N && j < M; i++, j++)
    {
        if (embalagens[i] >= brinquedos[j])
            qtd++;
        else
            j--; // volta o índice do brinquedo para tentar com a próxima embalagem
    }

    cout << qtd << endl;
    return 0;
}
