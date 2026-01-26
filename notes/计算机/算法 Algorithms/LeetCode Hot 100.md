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
## sort 排序
```C++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hashTable;
        for(string& str : strs) {
            string key = str;
            sort(key.begin(),key.end());
            hashTable[key].emplace_back(str);
        }
        vector<vector<string>> ans;
        for(auto it = hashTable.begin(); it != hashTable.end(); ++it) {
            ans.emplace_back(it->second);
        }
        return ans;
    }
};
```

## count 计数
```C++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> map;
        for(string str:strs) {
            int counts[26] = {0};
            for(char c:str) {
                counts[c-'a']++;
            }
            string key = "";
            for(int i = 0;i<26;++i) {
                if(counts[i]!=0) {
                    key.push_back(i+'a');
                    key.push_back(counts[i]);
                }
            }
            map[key].push_back(str);
        }
        vector<vector<string>> res;
        for(auto& p:map) {
            res.push_back(p.second);
        }
        return res;
    }
};
```

```C++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 自定义对 array<int, 26> 类型的哈希函数
        auto arrayHash = [fn = hash<int>{}] (const array<int, 26>& arr) -> size_t {
            return accumulate(arr.begin(), arr.end(), 0u, [&](size_t acc, int num) {
                return (acc << 1) ^ fn(num);
            });
        };

        unordered_map<array<int, 26>, vector<string>, decltype(arrayHash)> mp(0, arrayHash);
        for (string& str: strs) {
            array<int, 26> counts{};
            int length = str.length();
            for (int i = 0; i < length; ++i) {
                counts[str[i] - 'a'] ++;
            }
            mp[counts].emplace_back(str);
        }
        vector<vector<string>> ans;
        for (auto it = mp.begin(); it != mp.end(); ++it) {
            ans.emplace_back(it->second);
        }
        return ans;
    }
};
```

# 3、longestConsecutive 最长连续子序列
## brute force
```C++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0; // 处理空数组，避免后续越界
        
        sort(nums.begin(), nums.end());
        int maxCountSize = 1; // 至少有1个元素时，最小长度是1
        int currentCount = 1; // 当前连续序列长度
        
        // 遍历数组（从第2个元素开始）
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i-1]) {
                // 跳过重复元素
                continue;
            } else if (nums[i] == nums[i-1] + 1) {
                // 连续，长度+1
                currentCount++;
            } else {
                // 不连续，更新最大值，重置当前长度
                maxCountSize = max(maxCountSize, currentCount);
                currentCount = 1;
            }
        }
        
        // 最后一次更新（避免最后一段连续序列没统计）
        maxCountSize = max(maxCountSize, currentCount);
        return maxCountSize;
    }
};
```
## hash
```C++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set;//用unordered_set不用unordered_map
        for (const int& num : nums) {
            num_set.insert(num);//去重
        }

        int longestStreak = 0;

        for (const int& num : num_set) {
            if (!num_set.count(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (num_set.count(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                longestStreak = max(longestStreak, currentStreak);
            }
        }

        return longestStreak;           
    }
};
```

# 4、moveZeroes 移动零
## double ptr
```C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size(), left = 0, right = 0;
        while (right < n) {
            if (nums[right]) {
                swap(nums[left], nums[right]);
                left++;
            }
            right++;
        }
    }
};
```

# 5、maxArea 盛水最多的容器
## double ptr + Greedy
```C++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int maxWater = (right-left)*min(height[left],height[right]);
        while(left < right) {
            //核心贪心策略
            if(height[left]<height[right]) left++;
            else right--;
            maxWater=max(maxWater,(right-left)*min(height[left],height[right]));
        }
        return maxWater;
    }
};
```

# 6、thressSum 三数之和
## double ptr
```C++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        // 枚举 a
        for (int first = 0; first < n; ++first) {
            // 需要和上一次枚举的数不相同
            if (first > 0 && nums[first] == nums[first - 1]) {
                continue;
            }
            // c 对应的指针初始指向数组的最右端
            int third = n - 1;
            int target = -nums[first];
            // 枚举 b
            for (int second = first + 1; second < n; ++second) {
                // 需要和上一次枚举的数不相同
                if (second > first + 1 && nums[second] == nums[second - 1]) {
                    continue;
                }
                // 需要保证 b 的指针在 c 的指针的左侧
                while (second < third && nums[second] + nums[third] > target) {
                    --third;
                }
                // 如果指针重合，随着 b 后续的增加
                // 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if (second == third) {
                    break;
                }
                if (nums[second] + nums[third] == target) {
                    ans.push_back({nums[first], nums[second], nums[third]});
                }
            }
        }
        return ans;
    }
};
```

# 7、trap接雨水
## DP
逐一记录每个坐标i处的maxleft和maxright
```C++
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0) {
            return 0;
        }
        vector<int> leftMax(n);
        leftMax[0] = height[0];
        for (int i = 1; i < n; ++i) {
            leftMax[i] = max(leftMax[i - 1], height[i]);
        }

        vector<int> rightMax(n);
        rightMax[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            rightMax[i] = max(rightMax[i + 1], height[i]);
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += min(leftMax[i], rightMax[i]) - height[i];
        }
        return ans;
    }
};
```
## Single Stack
```C++
class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        stack<int> stk;
        int n = height.size();
        for (int i = 0; i < n; ++i) {
            while (!stk.empty() && height[i] > height[stk.top()]) {
                int top = stk.top();
                stk.pop();
                if (stk.empty()) {
                    break;
                }
                int left = stk.top();
                int currWidth = i - left - 1;
                int currHeight = min(height[left], height[i]) - height[top];
                ans += currWidth * currHeight;
            }
            stk.push(i);
        }
        return ans;
    }
};
```
## Double Ptr
### 暴力双指针
对每个坐标i，求其左右max
```C++
class Solution {
public:
    int trap(vector<int>& height) {
        int sum = 0;
        for (int i = 0; i < height.size(); i++) {
            // 第一个柱子和最后一个柱子不接雨水
            if (i == 0 || i == height.size() - 1) continue;

            int rHeight = height[i]; // 记录右边柱子的最高高度
            int lHeight = height[i]; // 记录左边柱子的最高高度
            for (int r = i + 1; r < height.size(); r++) {
                if (height[r] > rHeight) rHeight = height[r];
            }
            for (int l = i - 1; l >= 0; l--) {
                if (height[l] > lHeight) lHeight = height[l];
            }
            int h = min(lHeight, rHeight) - height[i];
            if (h > 0) sum += h;
        }
        return sum;
    }
};
```
### 改进双指针
注意到下标 i 处能接的雨水量由 $leftMax[i]$ 和 $rightMax[i]$ 中的最小值决定。由于数组 $leftMax$ 是从左往右计算，数组 $rightMax$ 是从右往左计算，因此可以使用双指针和两个变量代替两个数组。

维护两个指针 $left$ 和 $right$，以及两个变量 $leftMax$ 和 $rightMax$，初始时 $left=0,right=n−1,leftMax=0,rightMax=0$。指针 $left$ 只会向右移动，指针 $right$ 只会向左移动，在移动指针的过程中维护两个变量 $leftMax$ 和 $rightMax$ 的值。

当两个指针没有相遇时，进行如下操作：

- 使用 $height[left]$ 和 $height[right]$ 的值更新 $leftMax$ 和 $rightMax$ 的值；

- 如果$height[left]<height[right]$，则必有 $leftMax<rightMax$，下标 $left$处能接的雨水量等于 $leftMax−height[left]$，将下标 $left$ 处能接的雨水量加到能接的雨水总量，然后将 $left$ 加 1（即向右移动一位）；

- 如果 $height[left]≥height[right]$，则必有 $leftMax≥rightMax$，下标 $right$ 处能接的雨水量等于 $rightMax−height[right]$，将下标 $right$ 处能接的雨水量加到能接的雨水总量，然后将 $right$ 减 1（即向左移动一位）。

当两个指针相遇时，即可得到能接的雨水总量。
```C++
class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        int left = 0, right = height.size() - 1;
        int leftMax = 0, rightMax = 0;
        while (left < right) {
            leftMax = max(leftMax, height[left]);
            rightMax = max(rightMax, height[right]);
            if (height[left] < height[right]) {
                ans += leftMax - height[left];
                ++left;
            } else {
                ans += rightMax - height[right];
                --right;
            }
        }
        return ans;
    }
};
```

# 8、lengthOfLongestSubstring无重复字符的最长子串
```C++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // 哈希集合，记录每个字符是否出现过
        unordered_set<char> occ;
        int n = s.size();
        // 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        int rk = -1, ans = 0;
        // 枚举左指针的位置，初始值隐性地表示为 -1
        for (int i = 0; i < n; ++i) {
            if (i != 0) {
                // 左指针向右移动一格，移除一个字符
                occ.erase(s[i - 1]);
            }
            while (rk + 1 < n && !occ.count(s[rk + 1])) {
                // 不断地移动右指针
                occ.insert(s[rk + 1]);
                ++rk;
            }
            // 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1);
        }
        return ans;
    }
};
```

# 9、findAnagrams找到字符串中的所有字母异位词
## Brute Force
```C++
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> ans;
        int length = p.size();
        vector<int> hash(26);
        vector<int> zero(26,0);
        if(length>s.size()) return ans;
        for(int i=0; i<length; ++i) {
            hash[p[i]-'a']++;
        }
        for(int i=0; i<s.size()-length+1; ++i) {
            vector<int> temp = hash;
            for(int j=0; j<length; ++j) {
                temp[s[i+j]-'a']--;
            }
            if(temp == zero) ans.push_back(i);
        }
        return ans;
    }
};
```
## Sliding Window
```C++
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int sLen = s.size(), pLen = p.size();

        if (sLen < pLen) {
            return vector<int>();
        }

        vector<int> ans;
        vector<int> sCount(26);
        vector<int> pCount(26);
        for (int i = 0; i < pLen; ++i) {
            ++sCount[s[i] - 'a'];
            ++pCount[p[i] - 'a'];
        }

        if (sCount == pCount) {
            ans.emplace_back(0);
        }

        for (int i = 0; i < sLen - pLen; ++i) {
            --sCount[s[i] - 'a'];
            ++sCount[s[i + pLen] - 'a'];

            if (sCount == pCount) {
                ans.emplace_back(i + 1);
            }
        }

        return ans;
    }
};
```
## Optimized Sliding Window
```C++
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int sLen = s.size(), pLen = p.size();

        if (sLen < pLen) {
            return vector<int>();
        }

        vector<int> ans;
        vector<int> count(26);
        for (int i = 0; i < pLen; ++i) {
            ++count[s[i] - 'a'];
            --count[p[i] - 'a'];
        }

        int differ = 0;
        for (int j = 0; j < 26; ++j) {
            if (count[j] != 0) {
                ++differ;
            }
        }

        if (differ == 0) {
            ans.emplace_back(0);
        }

        for (int i = 0; i < sLen - pLen; ++i) {
            if (count[s[i] - 'a'] == 1) {  // 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
                --differ;
            } else if (count[s[i] - 'a'] == 0) {  // 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
                ++differ;
            }
            --count[s[i] - 'a'];

            if (count[s[i + pLen] - 'a'] == -1) {  // 窗口中字母 s[i+pLen] 的数量与字符串 p 中的数量从不同变得相同
                --differ;
            } else if (count[s[i + pLen] - 'a'] == 0) {  // 窗口中字母 s[i+pLen] 的数量与字符串 p 中的数量从相同变得不同
                ++differ;
            }
            ++count[s[i + pLen] - 'a'];
            
            if (differ == 0) {
                ans.emplace_back(i + 1);
            }
        }

        return ans;
    }
};
```
