#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool contains(const vector<int>& nums, const int element) {
	int n = nums.size();
	for (int i = 0; i < n; ++i) {
		if (nums[i] == element) {
			return true;
		}
	}
	return false;
}
void printVector(vector<int>& nums) {
	cout << "[ ";
	for (auto itr = nums.begin(); itr != nums.end(); ++itr) {
		cout << *itr << " ";
	}

	cout << "]" << endl;
}

int combinationSum4Rec(vector<int>& nums, int target) {
	if (nums.size() == 0) {
		return 0;
	}
	if (target == 0) {
		return 1;
	}

	int sum = 0;
	sort(nums.begin(), nums.end());

	for (int i = 0; i < nums.size(); ++i) {
		if (nums[i] <= target) {
			sum += combinationSum4Rec(nums, target - nums[i]);
		} else {
			break;
		}
	}
	return sum;
}

int combinationSum4(vector<int>& nums, int target) {
	sort(nums.begin(), nums.end());
	vector<int> table;
	// base case
	for (int i = 0; i < target + 1; ++i) {
		if (contains(nums, i)) {
			table.push_back(1);
		} else {
			table.push_back(0);
		}
	}

	for (int i = 0; i <= target; ++i) {
		for (int j = 0; j < i; ++j) {
			if (contains(nums, j)) {
				table[i] += table[i - j];
			}
		}
	}
	return table[target];
}



int main(int argc, char const *argv[])
{
	/* code */
	const int arr[] = {1,2,3};
	vector<int> vec(arr, arr + sizeof(arr) / sizeof(arr[0]));
	cout << combinationSum4(vec, 4) << endl;
	return 0;
}
