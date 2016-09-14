#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void printVector(vector<string>& nums) {
	cout << "[ ";
	for (auto itr = nums.begin(); itr != nums.end(); ++itr) {
		cout << *itr << " ";
	}
	cout << "]" << endl;
}

vector<string> initDict() {
	vector<string> dict;
	dict.clear();
	dict.push_back("");
	dict.push_back("");
	dict.push_back("abc");
	dict.push_back("def");
	dict.push_back("ghi");
	dict.push_back("jkl");
	dict.push_back("mno");
	dict.push_back("pqrs");
	dict.push_back("tuv");
	dict.push_back("wxyz");
	return dict;
}

vector<string> letterCombinations(string digits) {
	if (digits.length() == 0) {
		vector<string> res;
		res.clear();
		return res;
	}

	vector<string> dict = initDict();
	int digit = stoi(digits.substr(0,1), nullptr);
	string letters = dict[digit];

	if (digits.length() == 1) {
		vector<string> res;
		res.clear();
		for (int i = 0; i < letters.length(); ++i) {
			res.push_back(letters.substr(i,1));
		}
		return res;
	}
	// vector to store final answers
	vector<string> ans;
	ans.clear();

	vector<string> res = letterCombinations(digits.substr(1));
	for (auto itr = res.begin(); itr != res.end(); ++itr) {
		string combinedPart = *itr;
		for (int i = 0; i < letters.length(); ++i) {
			string letter = letters.substr(i, 1);
			string tmp = combinedPart;
			tmp.insert(0, letter);
			ans.push_back(tmp);
		}
	}
	return ans;
}


int main(int argc, char const *argv[])
{
	string str = "23";
	vector<string> ans = letterCombinations(str);
	printVector(ans);
	return 0;
}