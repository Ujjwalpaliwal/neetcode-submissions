class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        for(int x:nums){
            freq[x]++;
        }
        // create a buckets
        vector<vector<int>> bucket(nums.size()+1);
        for(auto&[num,count]:freq){
            bucket[count].push_back(num);
        }
        // takke top k
        vector<int> ans;
        for(int i=nums.size();i>=1&&ans.size()<k;i--){
            for (int num : bucket[i]) {
                ans.push_back(num);

                if (ans.size() == k) {
                    break;
                }
            }
        }
        return ans;
        }
    
};
