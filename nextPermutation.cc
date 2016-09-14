#include <iostream>
#include <vector>
#include <algorithm> 
#include <iterator>     // std::advance

using namespace std;
void nextPermutation(vector<int>& nums);
int findDecreasingIndex(const vector<int>& nums);
int findSwapIndex(const vector<int>& nums, const int tmp);

void nextPermutation(vector<int>& nums) {
	if (nums.size() == 0) {
		return;
	}
	int decreasingIndex = findDecreasingIndex(nums);
	
	// swap
	if (decreasingIndex != -1) {
		int tmp = nums[decreasingIndex];
		int swapIndex = findSwapIndex(nums, tmp);
		nums[decreasingIndex] = nums[swapIndex];
		nums[swapIndex] = tmp;
	}

	auto beginReverseItr = nums.begin();
	for (int i = 0; i < decreasingIndex + 1; ++i) {
		++beginReverseItr;
	}

	reverse(beginReverseItr, nums.end());
}

int findDecreasingIndex(const vector<int>& nums) {
	for (int i = nums.size() - 1; i > 0; --i) {
		if (nums[i - 1] < nums[i]) {
			return i - 1;
		}
	}
	return -1;
}

int findSwapIndex(const vector<int>& nums, const int tmp) {
	for (int i = nums.size() - 1; i >= 0; --i) {
		if (nums[i] > tmp) {
			return i;
		}
	}
	return 0;
}

int main(int argc, char const *argv[])
{
	vector<int> myVec;
	myVec.push_back(2);
	myVec.push_back(7);
	myVec.push_back(5);
	myVec.push_back(3);
	myVec.push_back(1);

	nextPermutation(myVec);

	for (auto e: myVec) {
		cout << e << " ";
	}
	cout << endl;
	return 0;
}