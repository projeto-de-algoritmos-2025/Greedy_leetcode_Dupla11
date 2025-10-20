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
    // ordena o vetor em ordem crescente
    sort(arr.begin(), arr.end());

    if (R < arr[0])
        // se a quantia de dinheiro for menor que o gibi mais barato
        qtd = 0;
    else if (R == arr[0])
        // se a quantia de dinheiro for igual ao gibi mais barato
        qtd = 1;
    else
    { // se a quantia de dinheiro for maior que o gibi mais barato
        for (int i = 0; i < N; i++)
        {
            // acumula o total gasto com gibis
            T += arr[i];
            if (T <= R)
                // se ainda houver dinheiro suficiente para comprar o gibi
                // aumenta a quantidade de gibis comprados
                qtd += 1;
            else
                // se não houver dinheiro suficiente para comprar mais gibis, encerra o loop
                break;
        }
    }

    cout << qtd << endl;
    return 0;
}
