#include <iostream>
#include <vector>
using namespace std;

int integerBreak(int n) {
	// if (n == 0) {
	// 	return 0;
	// }
	// if (n == 1) {
	// 	return 1;
	// }

	// int maxProd = 1;
	// for(int i = 1; i < min(6, n); ++i) {
	// 	int prod = max(integerBreak(n - i), n - i);

	// 	if (i * prod > maxProd) {
			
	// 		maxProd = i * prod;
	// 		// cout << maxProd << " at i =" << i << " n =" << n << endl;
	// 	}
	// }
	// return maxProd;

	vector<int> prodTable;
	for (int i = 0; i < n + 1; ++i) {
		prodTable.push_back(0);
	}

	prodTable[1] = 1;

	for (int i = 2; i < n + 1; ++i) {
		int maxProd = 1;
		for (int j = 1; j < min(6, i); ++j) {
			int prod = max(prodTable[i - j], i - j);
			
			if (j * prod > maxProd) {
				maxProd = j * prod;
			}
			
		}
		prodTable[i] = maxProd;
	}

	return prodTable[n];
}

int main(int argc, char const *argv[])
{
	/* code */
	cout << integerBreak(10) << endl;
	return 0;
}