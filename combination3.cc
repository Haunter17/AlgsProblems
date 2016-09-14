#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void printVector(const vector<vector<int> >& coll) {
	cout << "[ ";
	for (auto itr = coll.begin(); itr != coll.end(); ++itr) {
		vector<int> vec = *itr;
		cout << "[ ";
		for (auto it = vec.begin(); it != vec.end(); ++it) {
			cout << *it << " ";
		}
		cout << "] ";
	}

	cout << "]" << endl;
}

void combination(vector<int>& coll, int k, int n, vector<int>& curr, 
	int level, vector<vector<int> >& res) {
	if (k == 0 && n == 0) {
		res.push_back(curr);
	} else if (k == 0 || n == 0) {
		return;
	} else {
		for (int i = level; i < coll.size(); ++i) {
			if (coll[i] <= n) {
				curr.push_back(coll[i]);
				// if (i == 3) {
				// 	cout << "i " << i << " level " << level << endl;
				// }
				combination(coll, k - 1, n - coll[i], curr, i + 1, res);
				curr.pop_back();
			}	
		}
	}
}

vector<vector<int> > combinationSum3(int k, int n) {
	vector<vector<int> > res;
	res.clear();
	vector<int> coll;
	for (int i = 1; i < 10; ++i) {
		coll.push_back(i);
	}
	vector<int> curr;
	curr.clear();

	combination(coll, k, n, curr, 0, res);
	return res;
}

int main(int argc, char const *argv[])
{
	/* code */
	vector<vector<int> > res = combinationSum3(3,9);
	printVector(res);
	return 0;
}
