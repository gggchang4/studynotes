# 1、twoSum 两数之和
## brute force
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        for(int i=0; i<nums.size()-1; ++i) {
            for(int j=i+1; j<nums.size(); ++j) {
                if(nums[i]+nums[j]==target) {
                    ans.push_back(i);
                    ans.push_back(j);
                }
            }
        }
        return ans;
    }
};
```
## hash
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hashTable;
        for(int i=0; i<nums.size(); ++i) {
            auto it = hashTable.find(target - nums[i]);
            if(it != hashTable.end()) {
                return {it->second,i};
            }
            hashTable[nums[i]] = i;
        }
    }
};
```

# 2、groupAnagrams字母异位词分组
